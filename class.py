import pandas as pd

filename = "./big-mac-full-index.csv"
df = pd.read_csv(filename)

query = f"(iso_a3 == 'MEX')"   
mxn_df = df.query(query)
min_idx = mxn_df['dollar_price'].idxmin()

#print(mxn_df)
#print(mxn_df.loc[min_idx])
#print(round(mxn_df['dollar_price'].mean(),2))

#for index, row in mxn_df.iterrows():
 #   print(mxn_df['name'][index])

#Iterating with apply() is recommended 
# Pandas vectorization is a faster and more efficient approach; utilizes less memory

def get_new_country_name(row):
    new_country_name = f"{row['name']} ({row['iso_a3']})"
    print(new_country_name)
    # or return new_country_name

df.apply(get_new_country_name,axis=1)

#df['new name'] = df.apply(get_new_country_name,axis=1)
#print(df['new name'])
#Ues the above method uf returning results from the function