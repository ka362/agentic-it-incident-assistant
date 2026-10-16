from tools.status_tool import check_application_status
from tools.log_tool import search_logs
from tools.knowledge_tool import search_knowledge_base
from tools.incident_tool import create_incident



application_name = "Payment API"

status = check_application_status(application_name)
print("Status:", status)

errors = search_logs(application_name)
print("Errors:", errors)

#looping error

for error in errors:
    result = search_knowledge_base(error)
    # if error in search_knowledge_base:
        

print(result)

