import type { HTMLBundle } from "bun"

import { file, env, serve, randomUUIDv7 } from "bun"
import { Database } from "bun:sqlite"
import { join } from "node:path"

import pageLogin from "./login.html"
import pageProfile from "./profile.html"

async function read_content(endpoint: HTMLBundle | string): Promise<any> {
    if (typeof endpoint === "string") {
        const html = await file(join(import.meta.dir, endpoint)).text()
        const contentType = `text/${endpoint.split(".").pop()}`
        if (["text/html", "text/css"].includes(contentType)) {
            return () => new Response(html, { headers: { "Content-Type": contentType } })
        }
        return () => new Response(null, { status: 500 })
    }

    return endpoint
}

const statics = {
    login: await read_content(pageLogin),
    profile: await read_content(pageProfile),
    tailwind: await read_content("./tailwind.css")
}

const sql = await file("db.sql").text()
const db = new Database(":memory:")

db.exec(sql)

const PORT = env.PORT ?? 8080
const HOST = env.HOST ?? "0.0.0.0"

console.log(`Listening at http://${HOST}:${PORT}`)

serve({
    port: PORT,
    hostname: HOST,
    development: false,
    routes: {
        "/": () => Response.redirect("login", 302),
        "/api/session": {
            GET: async (req) => {
                const sessionId = req.cookies.get("ecw4-session")
                if (!sessionId) return new Response("Unauthorized", { status: 401 })

                const session = db.query("SELECT 1 FROM session WHERE session_id = ?").get(sessionId)
                return session ? new Response("OK", { status: 200 }) : new Response("Unauthorized", { status: 401 })
            }
        },
        "/api/login": {
            POST: async (req) => {
                const { username, password } = await req.json() as { username: string, password: string }
                if (!username || !password) return new Response("Bad Request", { status: 400 })

                // Vulnerability SQL Injection
                const user = db.query(`SELECT user_id FROM user WHERE username = '${username}' AND password = '${password}'`).get() as { user_id: number } | null

                if (!user) return new Response("Unauthorized", { status: 401 })

                const sessionId = randomUUIDv7()
                db.query("INSERT INTO session (session_id, user_id) VALUES (?, ?)").run(sessionId, user.user_id)

                req.cookies.set("ecw4-session", sessionId)

                return Response.json({ status: "OK", redirect: "profile" }, { status: 200 })
            }
        },
        "/api/logout": {
            POST: async (req) => {
                const sessionId = req.cookies.get("ecw4-session")
                if (!sessionId) return new Response("Unauthorized", { status: 401 })

                db.query("DELETE FROM session WHERE session_id = ?").run(sessionId)
                req.cookies.delete("ecw4-session")

                return Response.json({ status: "OK", redirect: "login" }, { status: 200 })
            }
        },
        "/api/profile": {
            GET: async (req) => {
                const sessionId = req.cookies.get("ecw4-session")
                if (!sessionId) return new Response("Unauthorized", { status: 401 })

                const user = db.query(`
                    SELECT session.user_id, user.username, user.description
                    FROM session
                    JOIN user ON session.user_id = user.user_id
                    WHERE session.session_id = ?
                `).get(sessionId) as {
                    user_id: number
                    username: string
                    description: string
                } | null

                if (!user) return new Response("Unauthorized", { status: 401 })

                return Response.json({ status: "OK", user }, { status: 200 })
            }
        },
        "/api/health": () => Response.json({ status: "OK" }, { status: 200 }),
        "/login": statics.login,
        "/profile": statics.profile,
        "/tailwind.css": statics.tailwind
    }
})
