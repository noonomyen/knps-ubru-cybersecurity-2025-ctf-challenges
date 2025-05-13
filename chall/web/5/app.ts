import type { HTMLBundle } from "bun"

import { file, env, serve } from "bun"
import { Database } from "bun:sqlite"
import { join } from "node:path"

import pageMenu from "./menu.html"

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
    menu: await read_content(pageMenu),
    tailwind: await read_content("tailwind.css")
}

const sql = await file("db.sql").text()
const db = new Database(":memory:")

db.exec(sql)

const PORT = env.PORT ?? 8080
const HOST = env.HOST ?? "0.0.0.0"

console.log(`Listening at http://${HOST}:${PORT}`)

interface Menu {
    id: string
    name: string
    description: string
    price: number
}

serve({
    port: PORT,
    hostname: HOST,
    development: false,
    reusePort: true,
    routes: {
        "/": () => Response.redirect("menu", 302),
        "/api/menu": {
            GET: async (req) => {
                let menu: Menu[] = []

                const search = new URL(req.url).searchParams.get("search")

                // Vulnerability SQL Injection
                if (search) menu = db.query(`SELECT * FROM menu WHERE name LIKE '%${search}%'`).all() as Menu[]
                else menu = db.query("SELECT * FROM menu").all() as Menu[]

                return Response.json({ status: "OK", menu: menu }, { status: 200 })
            }
        },
        "/api/health": () => Response.json({ status: "OK" }, { status: 200 }),
        "/menu": statics.menu,
        "/tailwind.css": statics.tailwind
    }
})
