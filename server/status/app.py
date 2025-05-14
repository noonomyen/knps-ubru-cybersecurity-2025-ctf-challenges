from flask import Flask, render_template
from docker import DockerClient
from docker.models.containers import Container

app = Flask(__name__)
client = DockerClient(base_url="unix://var/run/docker.sock")

@app.route("/")
def status():
    containers_info = []

    try:
        containers: list[Container] = client.containers.list(all=True)
        for container in containers:
            if "com.docker.compose.project" not in container.labels or container.labels["com.docker.compose.project"] != "server":
                continue
            containers_info.append({
                "name": container.name,
                "short_id": container.short_id,
                "image": container.image.tags[0] if hasattr(container.image, "tags") and len(container.image.tags) != 0 else str(container.image), # type: ignore
                "status": container.status
            })
    except Exception as e:
        return f"Error: {str(e)}", 500

    return render_template("index.html", containers=containers_info)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=False)
