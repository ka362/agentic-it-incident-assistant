import pandas as pd
df = pd.read_csv("data/knowledge_base.csv")
print(df.head)

#search logs

def search_knowledge_base(error_code):
    #errors = []
    for index,row in df.iterrows():
        if row["error_code"] == error_code: 
            return row["cause"],row["resolution"]
        # if row["level"] == error:
            # # # # errors.append(row["error_code"])
            # # # # return errors

print(search_knowledge_base("DB_CONNECTION_TIMEOUT"))
               

