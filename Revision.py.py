
# coding: utf-8

# In[62]:


#number

a=5
print(a**5)

#int * float = float

my_income = 100
tax_rate = 0.1
my_taxes= my_income * tax_rate
print(my_taxes)


# In[63]:


# string splitting

my_string='Hello world'
x = my_string.split()
print(x)

# without space

my_string = 'Hello World'
x= my_string.split('e')
print(x)

# Capitalize

my_string ='abcdefgh'
x = my_string.capitalize()
print(x)

# Upper

my_string ='abcdefgh'
x = my_string.upper()
print(x)


# In[25]:


#print formatting (to inserst one string into anothor string)

x= 'this is a string: {}' .format('Insert me')
print(x)

#mutiple

x= 'Item one: {}, Item two: {}, Item three: {}' .format('dog', 'cat', 'rabbit')
print(x)

#multiple and organized to reduce complexity

x= 'Item one: {c}, Item two: {b}, Item three: {a}' .format(a='dog', b='cat', c='rabbit')
print(x)



# In[66]:


#lists

x=[1,2,3,4]
print(x)

#length of the list

print(len(x))

#type

print(type(x))

#indexing

print(x[0])

print(x[1:])

print(x[:4])

print(x[2:4])

#lists are mutable

x[0]='new item'
print(x)

# append for add new items at the end

x.append('last item')
print(x)

#extend to add one list into one list 

first_list= [1,2,3,4]
second_list = ['a','b','c']
first_list.extend(second_list)
print(first_list)

#pop the last item

x.pop(0)
print(x)

x.reverse()
print(x)

#sort

a=[34,67,4,3,8,2]
a.sort()
print(a)

#index the nested list

nested_list=[1,2,3,4,['a','b','c','d']]
print(nested_list[4][1])

# list comprehension

matrix=[[1,2,3],[4,5,6],[7,8,9]]
col=[row[0] for row in matrix]
print(col)


# In[79]:


#dictionaries

a = {'key1':123,'key2':'abcd', 'key3':{'breakfast':['eggs','bread','butter']} }
print(a['key3']['breakfast'][2].upper())
     


# In[129]:


#tuples are immutable

a =('sri',1,2,3,True)
print(a)

#tuple unpacking

list=[(1,2), (3,4), (5,6)]
for (tup1, tup2) in list:
    print(tup1)
    print(tup2)
    


# In[84]:


#set = sets are unorganizd list of elements

x=set()
x.add(1)
x.add(2)
x.add(0.4)
x.add(5)
print(x)


#sets takes in only unique elements
x=set()
x.add(1)
x.add(2)
x.add(2)
x.add(2)
x.add(2)
x.add(0.4)
x.add(5)
print(x)

y=set([1,2,2,2,2,3,4,4,4,5,])
print(y)




# In[85]:


#Exercise

#problem:1
#given the string 
s='django'

#'d'

#'o'

#'djan'

#'jan'

#'go'

#reverse the string



# In[86]:


#problem:2
#given the nested list
l=[3,7,[1,4,'hello']]
#reassign 'hello' to be 'goodbye'



# In[88]:


#problem:3
#grab hello from the dictionaries:

#d1={'simple_key':'hello'}
#d2={'k1':{'k2':'hello'}}
#d3={'k1':[{'nested_key':{'this is deep',['hello']]}]}          
          


# In[90]:


#problem:4
#find the unique values
#mylist =[1,1,1,1,1,3,3,3,,6,6,6,6,7,,8]


# In[93]:


#problem:5
#given two var
#age=4
#name=sam

#print following string
#"Hello my dog's name is sam and he is 4 years old"


# In[100]:


# Control Flow

'black'=='white'


# In[101]:


1>2


# In[102]:


2<8


# In[103]:


(2==2) or (2>1)


# In[105]:


(2==2) and (2<1)


# In[108]:


1!=1


# In[107]:


1!='1'


# In[120]:


#indentation

if 1==1:
    print('first block')
    if 2>4:

        print('second block')
        
if 1!=1:
    print('hello')
elif 3>6:
    print('run')
else:
    print('bye')
        


# In[144]:


#loop

#for loop

seq=[1,2,3,4,5,6]
for hello in seq:
    print('hello')
    
#in dictionary

d={'sam':1, 'dan':2, 'van':3}
for k in d:
    print(d[k])
    
#while loop

i = 1

while i<10:
        print("i is: {}" .format(i))
        i=i +5
    
    
    

