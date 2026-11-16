"""An MCP server from scratch: any AI app can read RSS and Atom feeds with it. Free, no API key."""
import html
import urllib.request
import xml.etree.ElementTree as ET

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


@mcp.tool()
def read_feed(url: str, limit: int = 10) -> list[dict]:
    """Read an RSS or Atom feed and return its newest items: title, link and date.
    Use it for news, blogs, podcasts or any site that publishes a feed."""
    req = urllib.request.Request(url, headers={"User-Agent": "feeds-mcp/1.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        root = ET.fromstring(r.read())

    def field(node, *names):
        for child in node:
            if child.tag.split("}")[-1] in names:
                return html.unescape((child.text or child.get("href") or "").strip())
        return ""

    items = []
    for node in root.iter():
        if node.tag.split("}")[-1] in ("item", "entry"):
            items.append({
                "title": field(node, "title"),
                "link": field(node, "link"),
                "date": field(node, "pubDate", "updated", "published"),
            })
    return items[:limit]


if __name__ == "__main__":
    mcp.run()
