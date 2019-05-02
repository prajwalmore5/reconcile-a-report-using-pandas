# --------------

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Code starts here
df = pd.read_csv(path)
df['state'] = df['state'].str.lower()
df['total'] = df['Jan'] + df['Feb'] + df['Mar']

sum_row = {col: df[col].sum() for col in df}
sum_df = pd.DataFrame(sum_row, index=["Total"])
df_final = df.append(sum_df)
# Code ends here


# --------------
import requests

# Code starts here

url = "https://en.wikipedia.org/wiki/List_of_U.S._state_abbreviations"
response = requests.get(url)
df1 = pd.read_html(response.content)[0]
df1 = df1[11:]
new_header = df1.iloc[0]
df1 = df1[1:]
df1.columns = new_header
df1['United States of America'].replace('DistrictofColumbia', 'District of Columbia') 
df1['United States of America'].replace('NewHampshire', 'New Hampshire') 
df1['United States of America'].replace('NewJersey', 'New Jersey')
df1['United States of America'].replace('NewMexico', 'New Mexico') 
df1['United States of America'].replace('NewYork', 'New York') 
df1['United States of America'].replace('NorthCarolina', 'North Carolina') 
df1['United States of America'].replace('NorthDakota', 'North Dakota')  
df1['United States of America'].replace('RhodeIsland', 'Rhode Island') 
df1['United States of America'].replace('SouthCarolina', 'South Carolina') 
df1['United States of America'].replace('SouthDakota', 'South Dakota')
df1['United States of America'].replace('WestVirginia', 'West Virginia')  
# Code ends here


# --------------
df1['United States of America'] = df1['United States of America'].astype(str).apply(lambda x: x.lower())
df1['US'] = df1['US'].astype(str)

# Code starts here
mapping = dict(zip(df1['United States of America'], df1['US']))
df_final.insert(loc=6, column='abbr', value = df_final['state'].map(mapping))
# Code ends here


# --------------
# Code stars here

df_final.at[6, 'abbr'] = 'MS'
df_final.at[10, 'abbr'] = 'TN'
# Code ends here


# --------------
# Code starts here

# Calculate the total amount
df_sub=df_final[["abbr", "Jan", "Feb", "Mar", "total"]].groupby("abbr").sum()
print(df_sub.shape)
# Add the $ symbol
formatted_df = df_sub.applymap(lambda x: "${:,.0f}".format(x))
print(formatted_df)
# Code ends here


# --------------
# Code starts here

# Calculate the sum
sum_row = df_sub[["Jan", "Feb", "Mar", "total"]].sum()

df_sub_sum = pd.DataFrame(data=sum_row).T
#apply $ to the sum 
df_sub_sum = df_sub_sum.applymap(lambda x: "${:,.0f}".format(x))

# append the sum
print(formatted_df)
final_table = formatted_df.append(df_sub_sum)
print(final_table)
# rename the index
final_table = final_table.rename(index={0: "Total"})
print(final_table)

# Code ends here    


# --------------
# Code starts here
df_sub['total'] = df_sub[["Jan", "Feb", "Mar"]].sum()
df_sub['total'].plot.pie(y='total', figsize=(5, 5))
# Code ends here


