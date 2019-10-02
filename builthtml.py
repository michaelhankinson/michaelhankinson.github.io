# start here
import pandas as pd

def getitdone():
    df = pd.read_csv('Data_files/ride_data', header=None)
    h_df = df.to_html()
    return h_df

getitdone