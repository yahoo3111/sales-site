"""Dependency-free static server for the sales pages.

The deploy platform runs this file directly (python app.py). Flask stacks on
uppcoder proxy to the framework default port 5000, so this server binds every
port the platform might expect (80, 3000, 5000, 8000, 8080, plus $PORT).
Clean URLs (/freight-invoice-audit -> freight-invoice-audit.html), a /healthz
probe, and a plain 404 for anything else.
"""
import os
import threading
from http.server import SimpleHTTPRequestHandler
from socketserver import ThreadingTCPServer

ROOT = os.path.dirname(os.path.abspath(__file__))
PORTS = [80, 3000, 5000, 8000, 8080]
if os.environ.get("PORT"):
    PORTS.append(int(os.environ["PORT"]))


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def do_GET(self):
        path = self.path.split("?", 1)[0]
        if path == "/healthz":
            body = b"ok"
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        candidate = path.lstrip("/")
        if not candidate:
            candidate = "index.html"
        elif not os.path.splitext(candidate)[1]:
            html = os.path.join(ROOT, candidate + ".html")
            if os.path.isfile(html):
                candidate = candidate + ".html"
        if candidate and os.path.isfile(os.path.join(ROOT, candidate)):
            self.path = "/" + candidate
        super().do_GET()

    def log_message(self, *args):
        pass


def main():
    servers = []
    for port in dict.fromkeys(PORTS):
        try:
            servers.append(ThreadingTCPServer(("0.0.0.0", port), Handler))
        except OSError as exc:
            print("skip port %s: %s" % (port, exc))
    if not servers:
        raise SystemExit("no port could be bound: %s" % PORTS)
    threads = [threading.Thread(target=s.serve_forever, daemon=True) for s in servers]
    for t in threads:
        t.start()
    print("sales-site serving on %s" % [s.server_address[1] for s in servers])
    for s in servers:
        s.serve_forever()


if __name__ == "__main__":
    main()
