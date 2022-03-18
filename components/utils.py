import pandas as pd
import os

path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'gender_data_clean.csv')

def load_data(path : str = path):

    raw_data = pd.read_csv(path, delimiter=";")

    agg_data = raw_data[raw_data.columns.difference(['Year'])].groupby(
        'Country').agg('mean')

    return raw_data, agg_data
