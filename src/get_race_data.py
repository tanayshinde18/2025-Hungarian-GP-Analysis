import fastf1
import os
import pandas as pd


os.makedirs('data/cache', exist_ok=True)
fastf1.Cache.enable_cache('data/cache') 

session= fastf1.get_session(2025, "Hungary","R")
session.load()

# print(f"the data for session.colmns is as folloes{session.results.columns}")
#laps =session.laps
#laps.to_csv('data/2025_Hungary_race_laps.csv',index=False)




# print("Data saved to data/ folder.")

results=session.results
results.to_csv('data/2025_Hungary_race_results.csv',index=False)

print("done with sessions.results")