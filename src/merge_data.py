import pandas as pd

laps=pd.read_csv('data/2025_Hungary_race_laps.csv')

results=pd.read_csv('data/2025_Hungary_race_results.csv')


pit_counts=(
    laps[laps['PitInTime'].notna()].groupby('DriverNumber').size().reset_index(name='PitStopCount')
)

results=results.merge(pit_counts,on='DriverNumber',how='left')

results['PitStopCount']=results['PitStopCount'].fillna(0).astype(int)

laps_merged=laps.merge(results[['Abbreviation','DriverNumber','TeamName','Position','PitStopCount']],on='DriverNumber', how='left')

laps_merged.to_csv('data/2025_Hungary_race_merged.csv', index=False)