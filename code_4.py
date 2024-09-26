import csv
import pandas as pd
big_mac_file = './big-mac-full-index.csv'
df = pd.read_csv(big_mac_file)

def get_big_mac_price_by_year(year, country_code):
    new_query = f"date >= '{year}-01-01' and date <= '{year}-12-31' and iso_a3 == '{country_code}'"
    new_date_df = df.query(new_query)
    print(new_date_df['dollar_price'].mean().round(2))

def get_big_mac_price_by_country(country_code):
    pass # Remove this line and code your function

def get_the_cheapest_big_mac_price_by_year(year):
    pass # Remove this line and code your function

def get_the_most_expensive_big_mac_price_by_year(year):
    pass # Remove this line and code your function

if __name__ == "__main__":
    result_a = get_big_mac_price_by_year(2010,'ARG')