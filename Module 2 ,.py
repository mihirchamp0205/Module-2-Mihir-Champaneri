#1# "Write a Python program to check if a number is positive, negative or zero."

num=int(input("Enter a number:"))

if num > 0:
    print(num," Is Positive")
elif num == 0:
    print(num,"Is Zero")
else:
    print(num, " Is Negative")


#2# "Write a Python program to get the Factorial number of given Number."

i=int(input("Enter Number:"))
fac=1
while i>0:
    fac=fac*i
    i=i-1
print("Factorial=",fac)


#3# "Write a Python program to get the Fibonacci series of given range."


# for loop with fibonacci series

n=int(input("Enter Value A:"))
a=0
b=1
   
print(a)
print(b)
for i in range(2,n):
 c=a+b
 a=b
 b=c
 print(c)

# while loop with fibonacci series

n=int(input("Enter Value A:"))
a=0
b=1
print(a)
while b<n:
    print(b)
    a,b=b,a+b
print()


#4# How memory is managed in Python?
#Ans:   #Memory management in Python involves a private heap containing all Python objects and data structures.
        #The Management of this private heap is ensured internally by the python memory manager.


#5#What is the purpose continue statement in python?
#Ans:- #The continue statement in Python is used to stop an iteration that is running and continue with the next one.


#6# Write python progarm that swap two number with temp variable and without temp variable.

# Using temp variable

x=13
y=12

temp = x
print ("the value of temp variable is",temp)

x = y
print ("the value of x is", x)

y = temp
print ("the value of y is",y)


# without temp variable

x = 12
y = 13

x,y = y,x
print("the value of x is",x)
print("the value of y is",y)


#7# "Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user."

number = int(input("Enter a Number : "))

if number % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")


#8# "Write a Python program to test whether a passed letter is a vowel or not"

letter = input("Enter a Letter: ")
if letter in "aeiou":
    print("Passed letter is Vowel")
else:
    print("Passed Letter is Not a Vowel")


#9# "Write a Python program to sum of three given integers. However, if two values are equal sum will be zero"

n1=int(input("Enter Frist Value N1:"))
n2=int(input("Enter Second Value N2:"))
n3=int(input("Enter Third Value N3:"))
if n1==n2 or n2==n3 or n1==n3:
    print("Sum is:",0)
else:
    print("Sum is:",n1+n2+n3)


#10# "Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5."

n1=int(input("Enter Frist Value N1:"))
n2=int(input("Enter Second Value N2:"))
def test(n1,n2):
    if n1==n2 or (n1+n2)==5 or abs(n1-n2)==5:      # abs is convert negative to positive
        return True
    else:
        return False
print(test(n1,n2))


#11# "Write a python program to sum of the first n positive integers.

n=int(input("Enter  Input Number:"))
sum=(n*(n+1))/2
print(sum)


#12# "Write a Python program to calculate the length of a string."

s=input("Enter String:")
print(len(s))


#13# "Write a Python program to count the number of characters (character frequency) in a string..."

n=input("Enter String:").lower()        # Take a string as a input from the user.
d={}                                    # Create a empty dictionary
for i in n:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)


#14# "What are negative indexes and why are they used?"
#Ans: "Negative indexing is used to in python to begin slicling from the end of the string i.e. the last.
       #Slicing in python gets a sub-string from a string. The slicing range is set as parameters i.e. start,stop and step.


#15# "Write a Python program to count occurrences of a substring in a string.."

str=input("Enter String:")
substr=input("Enter Substring:")

count=str.count(substr)\
       
print("Substring occures %d times:"%count)


#16# "Write a Python program to count the occurrences of each word in a given sentence.."

str=input("Enter String:")
counts = dict()
txt = str.split(" ")           # is function
for word in txt:
	if word in counts:
		counts[word] += 1
	else:
		counts[word] = 1
print(counts)


#17# "Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.."

a=input("Enter String:")
b=input("Enter String:")
print("Before Swap:",a," ",b)
a1 = b[:2] + a[2:]
b1 = a[:2] + b[2:]
print("After Swap:",a1," ",b1)

#18# "Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
#     If the given string already ends with 'ing' then add 'ly' instead
#     if the string length of the given string is less than 3, leave it unchanged"


s=input("Enter String:")

length = len(s)

if length > 2:
  if s.endswith('ing'):
      s += 'ly'
  else:
      s += 'ing'
print(s)


#19# "Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string."

def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


#20# "Write a Python function that takes a list of words and returns the length of the longest one."

s=input("Enter Line of String:")
n=s.split()
longest=len(n[0])
for i in n:
    if len(i)>longest:
        longest=len(i)
print("longest string length=",longest)


#21# "Write a Python function to reverses a string if its length is a multiple of 4."

s=input("Enter a String:")

if(len(s)%4==0):
    print(s[::-1])
else:
    print("can't")


#22# "Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
#     If the string length is less than 2, return instead of the empty string."

string=input("Enter string:")
count=0

# Loop through the string
for i in string:
      count=count+1
new_str=string[0:2]+string[count-2:count]

# Printing the new String
print("string is:")
print(new_str)


#23# "Write a Python function to insert a string in the middle of a string.."

def insert_string_middle(str, word):
	return str[:2] + word + str[2:]

print(insert_string_middle('[[]]', 'Python'))
print(insert_string_middle('{{}}', 'PHP'))
print(insert_string_middle('<<>>', 'HTML'))




#21# "







       






    





















