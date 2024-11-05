import pandas as pd

def transform_data(df, region):
    """Transform the data according to the business rules."""
    df['total_sales'] = df['QuantityOrdered'] * df['ItemPrice']
    df['region'] = region
    df['net_sale'] = df['total_sales'] - df['PromotionDiscount']
    
    df = df.drop_duplicates(subset='OrderId')

    df = df[df['net_sale'] > 0]

    return df
