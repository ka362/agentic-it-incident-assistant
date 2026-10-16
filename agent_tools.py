
from langchain_core.tools import tool

from tools.status_tool import check_application_status
from tools.log_tool import search_logs
from tools.knowledge_tool import search_knowledge_base
from tools.incident_tool import create_incident


@tool
def status_checker(application_name: str) -> str:
    """Check the current monitoring status of an application."""
    return str(check_application_status(application_name))


@tool
def log_searcher(application_name: str) -> list[str]:
    """Find ERROR log codes for an application."""
    return search_logs(application_name)


@tool
def knowledge_searcher(error_code: str) -> str:
    """Find the known cause and resolution for an error code."""
    return str(search_knowledge_base(error_code))


@tool
def incident_creator(application_name: str, error_code: str) -> str:
    """Create a support ticket for an unresolved incident. Use only when escalation is necessary."""
    return create_incident(application_name, error_code)


all_tools = [
    status_checker,
    log_searcher,
    knowledge_searcher,
    incident_creator
]


if __name__ == "__main__":
    print(status_checker.invoke({"application_name": "Payment API"}))
    print(log_searcher.invoke({"application_name": "Payment API"}))
    print(knowledge_searcher.invoke({"error_code": "DB_CONNECTION_TIMEOUT"}))