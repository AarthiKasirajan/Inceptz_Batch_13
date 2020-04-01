#!/usr/bin/env python
# coding: utf-8

# In[62]:


#1. Write a Python program to find those numbers which are divisible by 7 
#and multiple of 5 between 1500 and 2700(both included)

lst=[]
for i in range(1499,2701,1):
    if (i%7==0):
        if(i%5==0):
            lst.append(i)
            
print(lst)  


# In[63]:


# 2. Write a python program to construct following pattern, using a nestes for loop.
for i in range(0,5):
    for j in range(0,i+1):
        print ("*", end = "")
    print () 
    


# In[64]:


#3. Write a python program to count number of even and odd numbers from a series of numbers.
num_list = [30,34,35,29,50,204,79]
l=len(num_list)
even = 0
odd = 0

for i in num_list:
    if (i%2==0):
        even+=1
    else:
        odd+=1
print("Count of numbers in the list are:",l)
print("The value of numbers are:", num_list)   
print("The count of even numbers in the list is: ",even)  
print("The count of odd numbers in the list is: ",odd)  


# In[65]:


#4. Write a python program to find numbers between 100 and 400(both included) 
# where each digit of a number is an even number. 
# The numbers obtained should be printed in a comma sequence.
lst=[]
for i in range(99,401):
    s = str(i)
    if (int(s[0])%2==0) and (int(s[1])%2==0) and (int(s[2])%2==0):
            lst.append(s)
            
print(",".join(lst)) 


# In[66]:


# 5. Write a python program to caculate a dog's age in dog years. 
# Note- for first two years, a dog year = 10.5 human years, after that each dog year = 4 human years.
# eg- 20 = dog's age in human years
#   93= dog's age in dog's years 
dage = int(input("Enter the age of your dog: "))
hage=0

for i in range(1,dage):
    if(i<3):
        hage+=10.5
for i in range(3,dage+1):
    hage+=4
print("The age of your dog in dog years is", hage)


# In[67]:


# 6. Write a python function to find max of three numbers

n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
    
if (n1 > n2 and n1 > n3):
    largest = n1
elif (n2 > n1 and n2 > n3):
    largest = n2
else:
    largest = n3
print("The largest of three numbers is:", largest)


# In[68]:


# 7. Write a python function that takes a number as a parameter and check the number is prime or not.
num = int(input("Enter a number to check whether prime or not: "))
if num > 1:
    for i in range(2,num):
        if (num % i)==0:
            print (num, "is not a prime number.")
            print (i, "is divisible by", num)
            break
    else:
        print (num, "is a Prime Nummber!!")
else:
     print (num, "is not a prime number.")


# In[69]:


# 8. Write a python function that accepts a string and 
# calculate the number of upper case letters and lower case letters

ex = str(input("Type a statement:"))
upper = 0
lower = 0
for i in ex:
    if (i.isupper()):
        upper+=1
    elif(i.islower()):
        lower+=1
print("The number of uppercase characters in string is: ", upper)
print("The number of lowercase characters in string is: ", lower)
        


# In[70]:


# 9. Write a python program to reverse a string 

def Reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
s= str(input("Please enter something:"))
print("The original string is:", s)
print("The reversed string is:", Reverse(s))


# In[71]:


# 10. Write a python program to find the greatest common divisor(GCD) of two integers.
n1=int(input("Enter a number: "))
n2=int(input("Enter another number: "))

if(n1 > n2):
    small = n2
else:
    small = n1
for i in range(1, small+1):
    if((n1%i==0) and n2%i==0):
        gcd=i
        
print("The GCD is :", gcd)


# In[ ]:




