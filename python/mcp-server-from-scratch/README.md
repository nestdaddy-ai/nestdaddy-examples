# Build an MCP server from scratch (Python, free)

An MCP server is a small program that offers tools to AI apps like Claude Code, Claude Desktop, Cursor and VS Code.
This one reads any RSS or Atom feed, so the model can answer "what's on Hacker News right now?" with live links.
Standard library only, no API key. Video walkthrough: *How to Build an MCP Server from Scratch in Python* on
[YouTube @nestdaddy_search](https://www.youtube.com/@nestdaddy_search).

| File | Step |
|---|---|
| `step1_server.py` | The smallest server: one tool, `list_feeds`. |
| `server.py` | Final: `read_feed(url, limit)` reads any RSS/Atom feed (title, link, date). |

## Run it

```bash
pip install -r requirements.txt

# connect it to Claude Code
claude mcp add feeds -- python server.py

# then ask
claude -p "What's on the Hacker News front page right now? Give me the top 5 with links."
```

Claude Desktop / Cursor config:

```json
{
  "mcpServers": {
    "feeds": { "command": "python", "args": ["/full/path/to/server.py"] }
  }
}
```

Note: in version 2 of the MCP Python SDK, `FastMCP` was renamed to `MCPServer`
(`from mcp.server.mcpserver import MCPServer`). Older tutorials still show the v1 import.

Safety: tool descriptions are instructions the model follows. Only install MCP servers you trust and pin their versions.
