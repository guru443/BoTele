import pandas as pd

def tem():
    m= 'data.csv'
    df_data = pd.read_csv(m)
    # pd.set_option('display.max_rows')
    # print(df_data)    
    # print(type(df_data))

    minh = [df_data]
    return minh

tem()