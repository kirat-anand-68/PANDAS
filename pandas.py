data=[
    {'name':'kirat','Age':20,'City':'Jagadhri'},
    {'name':'Jasmeet','Age':14,'City':'Jagadhri'},
    {'name':'Harsh','Age':17,'City':'Jagadhri'},
    {'name':'Ekas','Age':10,'City':'Jagadhri'}
]
df=pd.DataFrame(data)
print(df)

df['Salary']=[50000,60000,70000,80000]
df
df.drop('Salary',axis=1,inplace=True)
df
df['Age']=df['Age']+1
df
data=np.array([1,2,3,4,5])
mean=np.mean(arr)
sd=np.std(arr)
Normalized_function=(data-mean)/sd
print("Normalized_function: ",Normalized_function)
print(np.var(arr))
print(np.median(arr))
print(np.mean(arr))
print(np.std(arr))
