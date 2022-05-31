import numpy as np

#Pasar a minutos
def convert_to_minutes(time):
    time_lst = time.split(':')
    if len(time_lst) == 2:
        return ((int(time_lst[1])/60) + (int(time_lst[0])))
    if len(time_lst) == 3:
        return ((int(time_lst[0])*60) + int(time_lst[1]) + (int(time_lst[2]) / 60))

#Limpiar DataFrame
def clean_df(df):
    df.replace('', np.nan, inplace=True)
    df.dropna(thresh=2, inplace=True)
    df.drop(columns=['Pnt', 'Prev', 'UCI', '▼▲', 'Rnk', 'Team'], inplace=True)
    df.dropna(axis=1, inplace=True)
    df.reset_index(inplace=True)
    df.drop(columns=['index'], inplace=True)
    df['Minutes'] = df['Time'].apply(convert_to_minutes)
    df["Minutes"] = df["Minutes"].round(2)
    return df

