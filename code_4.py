import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    new_query = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}'"
    new_date_df = df.query(new_query)
    print(new_date_df['dollar_price'].mean().round(2))

def get_big_mac_price_by_country(country_code):
    new_query = f"iso_a3 == '{country_code}'"
    new_date_df = df.query(new_query)
    print(new_date_df['dollar_price'].mean().round(2))

def get_the_cheapest_big_mac_price_by_year(year):
    new_query = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    new_date_df = df.query(new_query)
    cheapest_price = float(new_date_df.iloc[-1]['dollar_price'])
    for index, row in new_date_df.iterrows():
        if float(row['dollar_price']) < cheapest_price:
            cheapest_price = round(float(row['dollar_price']),2)
            country = row['name']
            country_code = row['iso_a3']
        else:
            continue
    print('%s(%s): $%.2f' % (country, country_code, cheapest_price))

def get_the_most_expensive_big_mac_price_by_year(year):
    new_query = f"date >= '{year}-01-01' and date <= '{year}-12-31'"
    new_date_df = df.query(new_query)
    expensive_price = 0
    for index, row in new_date_df.iterrows():
        if float(row['dollar_price']) > expensive_price:
            expensive_price = round(float(row['dollar_price']),2)
            country = row['name']
            country_code = row['iso_a3']
        else:
            continue
    print('%s(%s): $%.2f' % (country, country_code, expensive_price))

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,'ARG')
    result_b = get_big_mac_price_by_country("MEX")
    result_c = get_the_cheapest_big_mac_price_by_year(2008)
    result_d = get_the_most_expensive_big_mac_price_by_year(2014)