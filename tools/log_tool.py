import pandas as pd
df = pd.read_csv("data/application_logs.csv")
print(df.head)

#search logs

def search_logs(application_name):
    errors = []
    for index,row in df.iterrows():
        if row["application"] == application_name and row["level"] == "ERROR":
        #     return application_name
        # if row["level"] == error:
            errors.append(row["error_code"])
            return errors

print(search_logs("Payment API"))
               

