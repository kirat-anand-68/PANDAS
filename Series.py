#A series is a data structures in pandas that holds the array of information along with the index number.
#the named index differentiates this from a simple numpy array
# it is a one dimensional ndarray with the axis label.
#Panda series add a label index in the array.
import numpy as np
import pandas as pd
# myIndex=['USA','Canada','Mexico']
# myData=[1776,1778,1878]
# mySer=pd.Series(data=myData,index=myIndex)  #Now index is labelled series index/
# print(mySer)
# print(mySer['USA'])
# print(mySer[1])
#
# Ages={'Kirat':20,'Pranjay':20,'Karan':19}
# print(pd.Series(Ages))
# #*******************************SERIES 2******************************************
q1={'USA':20,'Japan':30,'India':49,'Canada':45,'Russia':56}
q2={'USA':90,'Holululu':67,'India':53,'Canada':52,'Russia':89}
My_q1=pd.Series(q1)
My_q2=pd.Series(q2)
print(My_q2)
print(My_q1)#Panda is a Case Sensitive.
print(My_q1.keys())
print(My_q1*2)
print(My_q1+My_q2) # It will not give the total sum of the name that are not matched in it.
New_total=My_q1.add(My_q2,fill_value=0)
print(New_total)
print(New_total.dtype)
