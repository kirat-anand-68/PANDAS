#Data Frame is a Columns and Rows in the Python that we can easily restructure and filter
#It a group of Pandas Series Objects that can share the same index
import numpy as np
import pandas as pd
np.random.seed(101)
my_arr=np.random.randint(0,101,(4,3))
print(my_arr)
My_index=['CA','USA','IN','Pk']
My_columns=['jan','Feb','Mar']
df=pd.DataFrame(data=my_arr,index=My_index,columns=My_columns)
print(df)
#***********************************Reading the CSV File****************************
df=pd.read_csv('Test_new.csv')
print(df)
print(df.columns)
print(df.index)
print(df.head(2)) # it shows the first 2 dataframes
print(df.tail(2))
print(df.describe()) # it describes the min count avd std deviation etc of the data.
# df.describe().transpose() ,# print(df.info())
print(df['a']) #Single Column
my_column=['a','s']
print(df[my_column])
hello=df['a']+df['s']
print("The Combination of two columns are given below:\n",hello,)
df['Sum']=df['a']+df['s']  #Adding up a New Column
# if we create a new column to the dataframe make sure that we donot have the same column name in the dataframe as it overwrites all of it.
print(df.head())
#**********************************AFTER THE DROPPING**********************
# df=df.drop('Sum',axis=1)
# print("AFTER THE DROPPING:",df.head())
# print(df.shape)#we can also use the inplace=True for getting the permanent change.
# df=df.set_index('d')
# print(df) # now the index is d.
# df=df.reset_index(inplace=True)
# print(df)
# df=df.iloc[0]
# print(df)
# Drop the 'Sum' column
df = df.drop('Sum', axis=1)  # No inplace=True; reassign to df
print("AFTER THE DROPPING:", df.head())
print("Shape:", df.shape)  # Verify the shape

# Set index to column 'd'
df = df.set_index('d')
print("Now the index is 'd':\n", df)

# Reset index
df.reset_index(inplace=True)  # No reassignment when inplace=True
print("After resetting index:\n",df)

# Use iloc to select the first row
row = df.iloc[0]  # Do not overwrite the DataFrame
print("First row as a Series:\n", row)


#**********************************Creating the CSV File***************************
# dis={"a":[1,2,3,4,5,6],"s":[1,2,3,4,5,6],"d":[1,2,3,4,5,6]}
# d=pd.DataFrame(dis)
# print(d)
# d.to_csv("Test_new.csv")
