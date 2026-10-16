
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from tools.status_tool import check_application_status
from tools.log_tool import search_logs
from tools.knowledge_tool import search_knowledge_base
from tools.incident_tool import create_incident


class IncidentState(TypedDict, total=False):
    application_name: str
    status: str
    errors: list[str]
    kb_results: list[dict]
    decision: str
    incident_id: str

def status_node(state: IncidentState):
    application_name = state["application_name"]

    status = check_application_status(application_name)

    return {"status": status}

def route_decision(state: IncidentState):

    if state["decision"] == "HIL":
        return "hil"

    return "end"

def log_node(state: IncidentState):

    application_name = state["application_name"]

    errors = search_logs(application_name)

    return {"errors": errors}

def knowledge_node(state: IncidentState):

    kb_results = []

    for error in state["errors"]:

        result = search_knowledge_base(error)

        if result != "Knowledge not found":
            kb_results.append({
                "error_code": error,
                "cause": result[0],
                "resolution": result[1]
            })

    return {"kb_results": kb_results}



def decision_node(state: IncidentState):

    errors = state["errors"]
    kb_results = state["kb_results"]

    if not errors:
        return {"decision": "NO_ERRORS"}

    known_errors = [item["error_code"] for item in kb_results]

    for error in errors:
        if error not in known_errors:
            return {"decision": "HIL"}

    return {"decision": "RESOLVED"}


def hil_node(state: IncidentState):

    known_errors = [
        item["error_code"]
        for item in state["kb_results"]
    ]

    unknown_errors = [
        error for error in state["errors"]
        if error not in known_errors
    ]

    error_code = unknown_errors[0]

    incident_id = create_incident(
        state["application_name"],
        error_code
    )

    return {
        "incident_id": incident_id,
        "decision": "HIL"
    }


# Create LangGraph workflow
workflow = StateGraph(IncidentState)

# Register nodes
workflow.add_node("status", status_node)
workflow.add_node("logs", log_node)
workflow.add_node("knowledge", knowledge_node)
workflow.add_node("decision", decision_node)
workflow.add_node("hil", hil_node)

# Connect nodes
workflow.add_edge(START, "status")
workflow.add_edge("status", "logs")
workflow.add_edge("logs", "knowledge")
workflow.add_edge("knowledge", "decision")

# Conditional routing
workflow.add_conditional_edges(
    "decision",
    route_decision,
    {
        "hil": "hil",
        "end": END
    }
)

workflow.add_edge("hil", END)

# Compile graph
app = workflow.compile()


# Test
if __name__ == "__main__":

    result = app.invoke({
        "application_name": "Payment API"
    })

    print("Application:", result["application_name"])
    print("Status:", result["status"])
    print("Errors:", result["errors"])
    print("Knowledge:", result["kb_results"])
    print("Decision:", result["decision"])
    print("Incident ID:", result.get("incident_id", "Not required"))
