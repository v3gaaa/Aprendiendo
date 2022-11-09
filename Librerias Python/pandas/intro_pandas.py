import pandas as pd

#Simple list
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

#Custom indexs
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

#To call the value at certain index
print(myvar[0])

#Create simple series from a dictionary
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

#Use specific values from a dictionary
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

#Create dataframe
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

#refer to the row index (This returns a pandas series)
print(df.loc[0])

#use a list of indexes (In pandas [] always returns a DataFrame)
print(df.loc[[0, 1]])

#Use custom indexes in a DataFrame
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df) 

#refer to the custom index
print(df.loc["day2"])

#the correct syntax to return the entire DataFrame.
df.to_string()

#load a CSV file into a DataFrame
df = pd.read_csv('data.csv')
print(df.to_string()) 

#If you dont use .to_string pandas will only return the first and the laat 5 rows
df = pd.read_csv('data.csv')
print(df)

#Check te maximum number of rows your system can show (without to_string)
print(pd.options.display.max_rows)

#Increase maximum number of rows
pd.options.display.max_rows = 9999

#Read json file. (JSON  have the same format as python dictionaryies)
df = pd.read_json('data.json')
print(df.to_string())

