import pandas as pd

df = pd.read_csv("pokemon_data.csv")
#for excel files(xlsx) pd.read_excel

### Rows
print(df.iloc[1:4])
print(df.iloc[2, 1])

## Get all rows = to a value

print(df.loc[df['Type 1'] == "Fire"])
print(df.describe()) #Statistical values for the date

print(df.sort_values(['Type 1', 'HP'], ascending=[1,0]))  #Type 1 goes A-Z ascending and Hp goe from hight=est to lowest descending

### Making Changes to the date

#Look how to get index of the dataframe

#Adding a column
df['Total'] = df.iloc[:, 4:10].sum(axis=1)
print(df.head())
#droppiing a column
#df = df.drop(columns=['Total'])


#Rearranging your dataframe
cols = list(df.columns)
df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
print(df.head())

### Save your dataframe

df.to_csv('modified.csv', index=False) #False remove unwanted indexing

#df.to_excel
#def.to_csv('modified.txt', index=False, sep='\t')


### Filtering data

new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)] # Need to separate by parenthesis ()

#reseting the index
new_df = new_df.reset_index(drop=True) #drop removes old indices
print(new_df.head())

# Contains function needs a string

print(df.loc[~df['Name'].str.contains('Mega')]) #~ kinda means not

#Using the very powerful regular expressions python package
import re

print(df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex=True)].head()) # flag ignores the case of the string

# regex includes a load of different abbreviatins for stuff to find differnet word patterns in words, may be useful to look up

### Conditional changes

#df.loc[df['Total'] > 500, ['Generation', 'Legendary']] = ['Test 1', 'Test 2'] # dependent on a condition column valus are renamed
#loc and iloc are very useful




#### Aggregate Statistics (Groupby)

print(df.groupby(['Type 1']).mean().sort_values('Total', ascending=False))

df['count'] = 1
print(df.groupby(['Type 1']).count()['count'])
print(df.groupby(['Type 1', 'Type 2']).count()['count']) #subgroups aswell


#### Working with big data

#Print chunks of the dataframe
#for df in pd.read_csv('modified.csv', chunksize=5):
#    print("CHUNK_DF")
#    print(df)

#Create an empty dataframe that will be filled by a concatinate and other operations
new_df = pd.DataFrame(columns = df.columns)

for df in pd.read_csv('modified.csv', chunksize=5):
    results = df.groupby(['Type 1']).count()

    new_df = pd.concat([new_df, results], sort =False)

print(new_df)

print(df[::5])









