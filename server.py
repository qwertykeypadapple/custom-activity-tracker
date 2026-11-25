#!/usr/bin/env python3
"""Serve the tracker on http://localhost:5207 (static files only; data.json comes from make_aman.py)."""
import http.server, os

PORT = 5207
HERE = os.path.dirname(os.path.abspath(__file__))


class H(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=HERE, **kw)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *a):
        pass


if __name__ == "__main__":
    print(f"Code Days on http://localhost:{PORT}")
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
