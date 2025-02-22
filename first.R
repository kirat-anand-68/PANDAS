v1<-c(1,2,3,4,5)
v2<-c(4,5,6,7,8)
v1+v2
v1-v2
v1*v2
mean(v1)
mean(v2)
sd(v1)
sd(v2)
median(v1)
median(v2)
#Vectors Recycling->
weight<-c(71,67,83,67)
height<-c(1.75,1.81,1.78,1.82,1.97,2.12,1.75)
bmi<-c(weight/height^2)
bmi

age<-c(21,23,24,26)
names(age)<-c("Kirat","Bhoru","Rahul","Gandhi")
age
names(age)<-NULL
age

#SLICING AD INDEXING->
v1<-c(1,2,3,4)
v1[2]
v1[-3]
#all except value at the 3
v1[4]
v2<-c(2,5,7,3,6)
v2["7"]
v2[2]
v3<-c("RAHUL","GAndhi","Kurukshetra")
hello(v3)<-v2
v3
#SELECT THE SEVERAL VALUES VALUES AT THE ONCE
v2[1:4]
v3["Kurukshetra"]
#Changing the dimension of R
a<-seq(10,100, by=10)
a
dim(a)<-c(2,5)
a
#Elemenst remains the same but the structure describe may be the different