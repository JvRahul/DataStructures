#python :average length of words.

l = 'Geeks', 'for', '', 'Rahul'
v = l.split(',')
def avg(L):
  if L == "":
	  return None
  c= 0
  for i in L:
    i = i.strip()
    print(i)
    c = c + len(i)
  
  print(c)
  n = len(L)
  print(n)
  avg = c/n

  return avg

  def AverageLenWords(sentence):
  words = sentence.split()
  l = 0
  for word in words:
  l += len(word)
  return round((l / len(words)), 3) if len(words) > 0 else 0
  
  print(AverageLenWords("a b cddefgh"))


#Given k numbers which are less than n, return the set of prime numbers among them

L = [0,1,2,3,2,3,31,5,34,12,43,13,23,2, -10]
#res = [1,2,3,31,5,43,13,23]
n = 50

res = []

def checkPrime(m):
  c = 0
  if m <= 0:
    return False
  if (m == 2) or (m ==3):
    return True
  for i in range(1,m//2):
    if m % i == 0:
      c += 1
      # print(i, c)
  if c == 1:
    return True
  else:
    return False

def primeNum(L):
  for i in set(L):
    if checkPrime(i):
      res.append(i)
      # print(res)
  return res

print(primeNum(L))
# print(checkPrime(3))
# print(3//2)




#Count distinct words in a sentence
dict = {}
def uniqWord(word):
  if word in dict:
	dict[word] += 1
  else:
	dict[word] = 1
def countUniqWrdSent(str):
  listOfWords = str.split(" ")
  for wrd in listOfWords:
	uniqWord(wrd)
  c = 0  
  for ele in dict:
	
	if dict[ele] == 1:
	  c += 1
  return c



#count the number of times a word appear in a sentence using a Hash Map
def uniqWord(word):
  if word in dict:
	dict[word] += 1
  else:
	dict[word] = 1

#Return tuples of a list, matching each item to another item


#Count the number of times a substring appear in a string
	test_str = "GeeksforGeeks is for Geeks"
	  
	# initializing substring 
	test_sub = "Geeks" 
	  
	# printing original string  
	print("The original string is : " + test_str) 
	  
	# printing substring 
	print("The original substring : " + test_sub) 

	print(test_str.split(test_sub))  

	# using split() + len() 
	# Frequency of substring in string 
	res = len(test_str.split(test_sub))-1
	  
	# printing result  
	print("The frequency of substring in string is " + str(res)) 

# flatten a given list that contain members that are numbers or nested lists.
# find avg word len, 
# input is a string, identify if a string is a valid IP
# Check if given array is Monotonic
Calculate the average word length.
Python:-
[1,None,1,2,None] --> [1,1,1,2,2]
if L[0] == None:
  L[0] = 0 or L[-1]
for i in range(len(L)):

  if L[i] == None:
	L[i] = L[i-1]

return L




# Ensure you take care of case input[None] which means None object.

# 1. Is the question to replace None with preceding value?
# 2. Is the second question to find the number of occurrences or the position of s in the given word
# Find common words in 2 sentences

# Question 1:
# Complete a function that returns the number of times a given character occurs in the given string

# Enter a string and a character sample(mississippi,s): missiSSippi,S
def findCharNum(s,c):
/*
* returns the number of times a given character occurs in the given string
*
* param :
* s: string to search the given character in
* c: the searching character in the given string
*/

test_str = "GeeksforGeeks"

# using naive method to get count  
# of each element in string  
all_freq = {} 

for i in test_str: 
  if i in all_freq: 
	  all_freq[i] += 1
  else: 
	  all_freq[i] = 1

# printing result  
print ("Count of all characters in GeeksforGeeks is :\n "
									  +  str(all_freq)) 

OR

test_str = "GeeksforGeeks"
  
# using set() + count() to get count  
# of each element in string  
res = {i : test_str.count(i) for i in set(test_str)} 
  
# printing result  
print ("The count of all characters in GeeksforGeeks is :\n "
											   +  str(res)) 
											   

Question 2:
# Fill in the blanks
#
# Given an array containing None values fill in the None values
# with most recent non None value in the array

#
# For example:
# - input array: [1,None,2,3,None,None,5,None]
a = [None,None,1,2,3,None,None,3,2,5,None,4,None,9,None,None,None]

#for i in range(len(a)):
  #if a[0] == None:
   # if a[i] is not None:
    #  a[0]=a[i]

def repNone(a):
  for i in range(len(a)):
    if a[i] == None:
      a[i] = a[i-1]


repNone(a)
a[0] = a[-1]
repNone(a)
print(a)

[OR_OR_OR_OR_OR]

a = [None,2,4,None]
b = [None,None,1,2,3,None,None,3,2,5,None,4,None,9,None,None,None]

def nonRplc(a):
  if a == None or len(a) < 1:
    return 0
  
  for i in range(len(a)):
    if a[0] == None:
      if a[i] is not None:
        a[0]=a[i]
  
  if a[0] == None:
    a[0] = 0

  for i in range(len(a)):
    if a[i] == None:
      a[i] = a[i-1]
  
  return a
    

#repNone(a)
#a[0] = a[-1]
#repNone(a)
print(nonRplc(a))
print(nonRplc(b))

# - output array: [1,1,2,3,3,3,5,5]

for 


# Question 3:
# Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings
# 3. [[A],[A,B],[A,C],[B,D],[C,A]] -- Find the alphabet with highest neighbors? -- (Wasnt able to solve because of time limit but the interviewer was like I get what…
# Python Questions:
# Avg length of words, some of the edge cases are having spaces in the beginning and end of the words, returning a float instead of int, returning None for blank input.
# Valid ip address, edge case to remember is if there are alphanumeric characters.

# •	Python Valid IP address   2 Answers
# •	Python graph node count   3 Answers
# •	Python average word length   2 Answers
# Python
# 1. Count the number of unique words in a sequence?
# 2. Print the part of the array of numbers
# 3. Check the substring in the string
# 4. Question on exceptions

# Python Questions -
# 1) Print Max element of a given list
# 2) Print median of a given list
# 3) Print the first nonrecurring element in a list

L = ['a','b','a']

def frst_recur(L):
  if L == None or len(L) <1:
    return 0
  dct = {}
  for i in L:
    if i in dct:
      dct[i]+=1
    else:
      dct[i] =1

  for ele in dct:
    if dct[ele] ==1:
      return ele


print(frst_recur(L))

# 4) Print the most recurring element in a list

# L = [2, 1, 2, 2, 1, 3] 
L = ['Dog', 'cat', 'dog', 'dog', 'Dog']

def mostRecur(L):
  #c = 0
  dct = {}

  for i in L:
    if i in dct:
      dct[i] += 1
    else:
      dct[i] = 1

  max_value = max(dct.values())  # maximum value
  max_keys = [k for k, v in dct.items() if v == max_value] # getting all keys containing the `maximum`

  # for k, v in dct.items():
  #   if v ==  max_value:
  #     return k

  return max_keys


print(mostRecur(L))

# 5) Greatest common Factor


def computeGCD(x, y): 
  
    if x > y: 
        small = y 
    else: 
        small = x 
    for i in range(1, small+1): 
        if((x % i == 0) and (y % i == 0)): 
            gcd = i 
              
    return gcd 

#Reverse Digits
def reverse(x: int) -> int:
  result, x_remaining = 0, abs(x)
  while x_remaining:
	result = result * 10 + x_remaining % 10
	x_remaining //= 10
  return -result if x < 0 else result

print(abs(-123))



# Find common words in 2 sentences  
# sent_1 = 'A blue whale is whale which is blue'
# sent_2 = 'The blue ocean has whales which are blue'

# whether [] is monotonic:
def m_increasing(A):
  if len(A) == 0:
	return 0
  else:
	for i in range(len(A)-1):
	  if A[i] > A[i+1]:
		return False
	  
	   
	return True


def m_decreasing(A):
  if len(A) == 0:
	return 0
  else:
	for i in range(len(A)-1):
	  if A[i] < A[i+1]:
		return False
	  
	   
	return True


def monotonic(A):
  if m_increasing(A) or m_decreasing(A):
	return True
  else:
	return False

A = [1,2,2,3,4,5,6,2,3,4]
#print(monotonic(A))

#common_words
def common_words(ip1, ip2):
  L1 = ip1.split(' ')
  L2 = ip2.split(' ')

  L3 = []
  for i in set(L1):
	if i in set(L2):
	  L3.append(i)
  
  return L3


print(common_words('A blue whale is whale which is blue', 'The blue ocean has whales which are blue'))




#Complete a function that returns a list containing all the mismatched words (case sensitive) between two given input strings
# For example:
str1 = "Firstly this is the first string"
str2 = "Next is the second string"
#

def uncom(str1, str2):
  L1 = str1.split(' ')
  L2 = str2.split(' ')
  res = ''
  #l = []
  for i in set(L1):
    if i not in set(L2):
      #l.append(i)
      res += ' ' + i
    
  for j in set(L2):
    if j not in set(L1):
      #l.append(i)
      res += ' ' + j
  
  #ls = str(l).strip('[]')
  #return ','.join(l)
  return res

print(uncom(str1, str2))


# ipv4 and ipv6 validation check:

def ipv4(s):
	try: return str(int(s)) == s and 0 < = int(s) <= 255
	except: return False
	
	
def ipv6(s):
	try: return len(s) <= 4 and int(s, 16) >= 0 and s[0] != '-'
	except: return False
	
if IP.count('.') == 3 and all(ipv4(i) for i in IP.split('.')):
	return 'Ipv4'
	
if IP.count(':') == 7 and all(ipv6(i) for i in IP.split(':')):
	return 'Ipv6'
return 'Neither'




def ipv4(s):
	try: return str(int(s)) == s and 0 <= int(s) <= 255
	except: return False
	
def ipv6(s):
	try return len(s) <= 4 and int(s, 16) >= 0 and s[0] != '-'
	except: return False
	
if Ip.count('.') == 4 and all(ipv4(i) for i in IP.split('.')):
	return 'ipv4'

if IP.count(':') == 7 and all(ipv6(i) for i in IP.split(':'):
	return "Ipv6"

return Neither
