import pandas as pd

df = pd.DataFrame([
    ['1', 'Fares', 32, True],
    ['2', 'Elena', 23, False],
    ['3', 'Steven', 40, True]
])

df.columns = ['id', 'name', 'age', 'decision']

# print(df)
# print(df[['name','age']])
# print(df.iloc[:,3])
# print(df.iloc[1:3,:])
# print(df[df.age>30])
print(df[(df.age<35)&(df.decision==True)])
