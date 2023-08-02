import pandas as pd

csv_file_path = '/filepath/final.csv'
df = pd.read_csv(csv_file_path)

df_melted = df.melt(id_vars=['ID column'], value_vars=['column 1','column 2', 'column 3', 'column N"'], var_name='Value_column', value_name='Value')
### Check column names and insert column names from your CSV

df_melted.drop(columns=['Room_Column'], inplace=True)
df_melted.sort_values(by=['Original Confirmation #'], inplace=True)
###Change the sort_values by setting to change the way it is sorted

df_melted.to_csv(csv_file_path, index=False)

