Project page for **MeshOctave: Split-and-Rewire Cascades for Mesh Generation**.

## Local preview

Run the no-cache development server from anywhere:

```bash
python3 scripts/serve_local.py
```

Then open <http://127.0.0.1:8000>. The server reads files directly from this
repository, so saved HTML, CSS, JavaScript, image, and mesh changes appear after
a normal browser refresh.

To expose the local preview through a temporary Cloudflare tunnel, keep the
development server running and start a second terminal:

```bash
cloudflared tunnel --url http://127.0.0.1:8000
```
