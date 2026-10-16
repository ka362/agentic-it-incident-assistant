import pandas as pd

df = pd.read_csv("data/application_status.csv")
print(df)

# function for app_status

def check_application_status (application_name):
    #application = application_name
    for index,row in df.iterrows():
        if row["application"] == application_name:
            return row ["status"]
            
    return "application not found"
        # else:
        #     return "application not found"
print(check_application_status("Customer Portal"))