import pandas as pd

df = pd.read_csv("data/incidents.csv")

def create_incident(application_name, error_code):

    new_id = "INC" + str(1001 + len(df))

    new_incident = {
        "incident_id": new_id,
        "application": application_name,
        "error_code": error_code,
        "status": "OPEN",
        "assigned_to": "Support Team"
    }

    df.loc[len(df)] = new_incident
    df.to_csv("data/incidents.csv", index=False)

    return new_id


print(create_incident("Payment API", "UNKNOWN_ERROR_897"))