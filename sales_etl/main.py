import pandas as pd
from extract import extract_data
from transform import transform_data
from load import load_data

def etl_process():
    path_a = 'order_region_a.csv'
    path_b = 'order_region_b.csv'

    df_a = extract_data(path_a)
    df_b = extract_data(path_b)

    df_a = transform_data(df_a, 'A')
    df_b = transform_data(df_b, 'B')

    df_combined = pd.concat([df_a, df_b], ignore_index=True)

    # Load data into MySQL database
    load_data(df_combined, host='localhost', user='root', password='mysql', database='maiora_assessment')

if __name__ == "__main__":
    etl_process()
