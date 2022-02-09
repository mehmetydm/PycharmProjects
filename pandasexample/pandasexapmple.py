import pandas as pd

df = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print(df)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']})
print(df)

df = pd.DataFrame({'Bob': ['I liked it.', 'It was awful.'],
              'Sue': ['Pretty good.', 'Bland.']},
             index=['Product A', 'Product B'])
print(df)
print("\n\n---------------------------\n\n")

df = pd.read_csv('data_oval.csv')
print(df.columns)
print(df.head)
print(df.describe())
print(df.Clarity)
print(df.Colour)
print(df["Cut"])
print("\n\n---------------------------\n\n")

reviews = pd.read_csv('winemag-data-130k-v2.csv')
print(reviews.country)
print(reviews['country'][0])
print(reviews.iloc[0])

# Conditional selection
print(reviews.country == 'Italy')
print(reviews.loc[(reviews.country == 'Italy') & (reviews.points >= 90)])

'''
Pandas comes with a few built-in conditional selectors, two of which we will highlight here.
The first is isin. isin is lets you select data whose value "is in" a list of values. For example, 
here's how we can use it to select wines only from Italy or France:

The second is isnull (and its companion notnull). These methods let you highlight values which are (or are not) empty (NaN). 
For example, to filter out wines lacking a price tag in the dataset, here's what we would do:
'''
reviews.loc[reviews.country.isin(['Italy', 'France'])]
reviews.loc[reviews.price.notnull()]





