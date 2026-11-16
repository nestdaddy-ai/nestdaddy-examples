"""Step 1: the smallest useful MCP server. One tool: the feeds this server knows."""
from mcp.server.mcpserver import MCPServer

mcp = MCPServer("feeds")

FEEDS = {
    "hacker news": "https://hnrss.org/frontpage",
    "bbc world": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "the verge": "https://www.theverge.com/rss/index.xml",
}


@mcp.tool()
def list_feeds() -> dict:
    """Names and URLs of the news feeds this server can read."""
    return FEEDS


if __name__ == "__main__":
    mcp.run()
