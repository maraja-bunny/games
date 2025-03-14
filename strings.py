
print('beryl')
print(8+2)
print('beryl\'s "phone"')
print(10*'beryl')
print('c:beryl\docs\2023')
x=2
y=6
print(x+y)
name= 'lennox'
print(name)
print(name+'kahati')
print(name[0])
print(name[4])
print(name[-1])
print(name[0:3])
myname= "bery asunga"
print(len(myname))
nums=[1,4,7,9]
nums.remove(4)
print(nums)
nums.insert(1,5)
print(nums)
print(min(nums))
print(sum(nums))
tup=(1,3,2,5,6,7)
print(tup)
data={1:'asunga',2:'martha',4:'beryl'}
print(data)
print(data[4])
keys=['asunga','maraja','beryl']
values=['java','python','js']
data=dict(zip(keys,values))
print(data)
print(data['asunga'])
data['martha']='sco'
print(list(range(10)))
print(list(range(2,10,2)))
a=2
b=4
print(a<b)
a=5
b=10
print(a&b)
print(a|b)
print(a^b)
print(a>>2)
print(bin(-12))
print(a<<2)
print(25&13)
import math
x=math.sqrt(25)
print(x)
temp=a
a=b
b=temp
#x=int(input('enter first number '))
#y=int(input('enter second number '))
#z=x+y
#print(z)
#char=input('enter char')[0]
#print(char)
#x=25.5
#r=x%2
#if r==0:
    #print("Even")
#elif r==1:
    #print('odd')

#i=1
#while i<=5:
    #print('beryl',end='')
    #j=1
    #while j<=4:
        #print('rocks',end='')
        #j=j+1 
x="asunga" 
for i in x:
    print(i)
nums=[10,15,26,27] 
for num in nums:
    if num % 5==0:
       print(num)
       break
else:
    print('not found')
x=10
for i in range(2,x):
    if x%i==0:
        print('not prime')
        break
#from array import*
#arr=array("i",[])
#n=int(input("enter the length of the array")) 
#for i in range(n):
    #X=int(input("enter next value")) 
    #arr.append(X)
#print(arr)
##k=0
#for e in arr:
    if e==val:
       print(k)
       break
#k=k+1

def fact(n):
    f=1
    for i in range (1,n+1):
        f=f*i
    return f
x=4
result = fact(x)
print(result)
def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
result=fact(5)
print(result) 
f=lambda a,b :a+b 
result=f(5,6) 
print(result)
def is_even(n):
    return n%2==0
nums=[3,4,5,6,7,10]
evens=list(filter(is_even,nums))         
print(evens)
x=[3,2,6,7,10]
supp=list(filter(lambda n:n%2==0,x))
print(supp)
double=list(map(lambda n:n*2,x))
print(double)
from functools import reduce
sum=reduce(lambda a,b:a*b, x)
print(sum)
a=3
b=5
print(a+b)
print(a-b)
print(a*b)
def leap (year):
    if(year/4==0):
        if(year/100==0):
            if(year/400==0):
                return True
            else:
                return False
    if True:
        return leap
    else:
        return NONE
        
year=1990
print(leap(year))
   

            
            

   








      


