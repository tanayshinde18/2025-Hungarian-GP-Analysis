import pandas as pd


laps_merged=pd.read_csv('data/2025_Hungary_race_merged.csv')

# print(laps_merged.columns)

def assign_stints(df):
    df=df.sort_values(['DriverNumber','LapNumber'])
    stint_number=[]
    current_stint={}

    for _, row in df.iterrows():
        driver=row['DriverNumber']
        compound=row['Compound']

        if driver not in current_stint:
            current_stint[driver]={"compound":compound,"stint":1}
        else:
            if compound!=current_stint[driver]["compound"]:
                current_stint[driver]["stint"]+=1
                current_stint[driver]["compound"]=compound
        
        stint_number.append(current_stint[driver]["stint"])
    
    df['StintNumber']=stint_number

    print('Stints have been added')
    return df

laps_stints=assign_stints(laps_merged)
laps_stints.to_csv('data/2025_Hungary_race_laps_with_stint.csv', index=False)


print(" Analysis-ready dataset saved to data/..")
