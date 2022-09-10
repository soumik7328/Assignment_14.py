#Assignment - 14 Full Stack Web Development using Python MySirG More on List
#1. Write a Python script to create a list of first N natural numbers.
a=int(input("Enter a number"))
b=[]
for e in range(1,a+1):
        b.append(e)
print(b) 
#2. Write a Python script to create a list of first N odd natural numbers.
a=int(input("Enter a number"))
b=[]
for e in range(1,a*2,2):
        b.append(e)
print("First",a," odd Natural number is-")        
print(b) 
#3. Write a Python script to create a list of first N even natural numbers.
a=int(input("Enter a number"))
b=[]
for e in range(2,(a+1)*2,2):
        b.append(e)
print("First",a," Even Natural number is-")        
print(b)
#4. Write a Python script to find the greatest number in a given list of numbers.
lst1=(input("Enter some number in list. with coma shepareted:- "))
lst2=lst1.split(',')
print("greatest number in a given list of numbers=",max(lst2))
#5. Write a Python script to find the smallest number in a given list of numbers.
lst1=(input("Enter some number in list. with coma shepareted:- "))
lst2=lst1.split(',')
print("Smallest number in a given list of numbers=",min(lst2))
#6. Write a Python script to calculate the sum of elements in a given list of numbers.
lst1=(input("Enter some number in list. with coma shepareted:- "))
lst2=lst1.split(',')
for i in range(len(lst2)):
    lst2[i]=int(lst2[i])
print("sum of elements in a given list of numbers=",sum(lst2))
#7. Write a Python script to remove all non int values from a list.
lst=[1,8,'soumik',25.8,3j+8,4]
lst2=[]
for e in lst:
    if type(e)==int:
        lst2.append(e)
print(lst2)        
#8. Write a Python script to print distinct elements along with their frequencies of occurrence in the list.
lst=(input("Enter some element useing coma separate:-"))
lst1=lst.split(',')
count={}
for e in lst1:
        if e in count:
            count[e]+=1
        else:
            count[e]=1           
for key,value in count.items():
        print(key,"  =  ",value)
#9. Write a Python script to print indices of all occurrences of a given element in a given list.
lst=(input("Enter some element useing coma separate:-"))
lst1=lst.split(',')
v=(input("Enter the element whoes index you want to know="))
for e in range(len(lst1)):
    if lst1[e]==v:
        print("index of ",v,"is",e)     
#10. Write a python script to sort a list.
bike=['Ktm350','BMWs1000rr','R15','Hayabusa']
bike.sort(reverse=True)
print(bike)