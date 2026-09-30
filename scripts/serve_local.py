#!/usr/bin/env python3
"""Serve the project directly from the repository with browser caching disabled."""

from __future__ import annotations

import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


class NoCacheRequestHandler(SimpleHTTPRequestHandler):
    def end_headers(self) -> None:
        self.send_header("Cache-Control", "no-store, no-cache, must-revalidate, max-age=0")
        self.send_header("Pragma", "no-cache")
        self.send_header("Expires", "0")
        super().end_headers()

    def list_directory(self, path: str):
        self.send_error(404, "Directory listing is disabled")
        return None


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bind", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=8000)
    args = parser.parse_args()

    handler = partial(NoCacheRequestHandler, directory=str(PROJECT_ROOT))
    server = ThreadingHTTPServer((args.bind, args.port), handler)
    print(f"Serving {PROJECT_ROOT} at http://{args.bind}:{args.port}")
    print("Caching is disabled; save files and refresh the browser to see updates.")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
