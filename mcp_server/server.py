
from pathlib import Path
import sys

# Make project root available for imports
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from mcp.server.fastmcp import FastMCP

from tools.status_tool import check_application_status
from tools.log_tool import search_logs
from tools.knowledge_tool import search_knowledge_base

mcp = FastMCP("IT Incident Support")


@mcp.tool()
def check_status(application_name: str) -> str:
    """Check the status of an application."""
    return str(check_application_status(application_name))


@mcp.tool()
def get_logs(application_name: str) -> list[str]:
    """Find error codes from application logs."""
    return search_logs(application_name)


@mcp.tool()
def search_kb(error_code: str) -> str:
    """Find the cause and suggested resolution for an error."""
    return str(search_knowledge_base(error_code))


if __name__ == "__main__":
    mcp.run(transport="stdio")
