# import seaborn as sns
# import matplotlib.pyplot as plt
# %matplotlib inline
# import numpy as np
import pandas as pd
import os as os
import json


# read csv file
path_parent = os.path.dirname(os.getcwd())
df=pd.read_csv('Data Sample/sandbox-installs.csv')

#convert to json
print("Generating Json file...")
to_json = df.to_dict(orient='records')
output = json.dumps(to_json)

file = open("Output/converted.json", "w")
file.write(output)
file.close()

print("Json file created in output folder")

#convert to sql

print("Generating sql insert statement...")

sql=""
for index, row in df.iterrows():
    print(row)
    sql = sql+"INSERT INTO sandboxtbl Values ("+"'"+str(row['user_pseudo_id'])+"','"+str(row['sku'])+"','"+str(row['app_version'])+"','"+str(row['geo_country'])+"','"+str(row['geo_region'])+"','"+str(row['geo_city'])+"','"+str(row['install_source'])+"','"+str(row['ua_name'])+"','"+str(row['ua_medium'])+"','"+str(row['ua_source'])+"','"+str(row['device_category'])+"','"+str(row['device_brand_name'])+"','"+str(row['device_model_name'])+"','"+str(row['device_os_hardware_model'])+"','"+str(row['device_os'])+"','"+str(row['device_os_version'])+"','"+str(row['idfa'])+"','"+str(row['idfv'])+"','"+str(row['is_limited_ad_tracking'])+"','"+str(row['device_language'])+"','"+str(row['device_time_zone_offset'])+"','"+str(row['timestamp_raw'])+"','"+str(row['table_date'])+"','"+str(row['is_returning_user'])+"','"+str(row['session_id'])+")\n"

print(sql)
f= open("Output/converted.sql","w+", encoding="utf-8")

f.write(sql)
f.close()
print("Sql file created in output folder")



