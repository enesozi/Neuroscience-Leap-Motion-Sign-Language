from Database.db_mongo import DB
import pandas as pd

db = DB()
data = db.get_train_data()
df = pd.DataFrame(data)
df.drop('_id', inplace=True, axis=1)
df.to_csv("train_data.csv", encoding='utf-8', index=False)