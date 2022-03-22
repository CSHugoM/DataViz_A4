import pandas as pd
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'gender_data_clean.csv')

def load_data(path : str = path):

    raw_data = pd.read_csv(path, delimiter=";")

    agg_data = raw_data[raw_data.columns.difference(['Year'])].groupby(
        'Country').agg('mean')

    return raw_data, agg_data

def compute_mean(data : pd.DataFrame, list_index : list, list_var : list):
    
    data_temp = data[list_var].reset_index()

    if list_index != None :
        data_select_rows = data_temp.iloc[list_index]
    else :
        data_select_rows = data_temp

    data_select_rows = data_select_rows.set_index('Country')
    data_select_rows = data_select_rows.astype(float)

    return data_select_rows.mean(axis=0).round(1).tolist()
