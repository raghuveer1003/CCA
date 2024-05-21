#!/usr/bin/env python
# coding: utf-8

# In[1]:


import difflib
str1= "Hello World"
str2= "Hello World"
matcher= difflib.SequenceMatcher(None, str1, str2)
print("Similarity ratio is; ", matcher.ratio())


# In[2]:


def find_remove_dups(list):
    counts ={}
    duplicates=[]
    for c in list:
        if c in counts:
            counts[c] +=1
        else:
             counts[c] =1
    for c, count in counts.items():
        if count>1:
            duplicates.append(c)
    print("Duplicates: ",duplicates)
    
    list[:] = [c for c in list if counts[c] ==1]
list = ['a','b','c','d','a','e','b']
find_remove_dups(list)
print("List after removing duplicates: ",list)


# In[8]:


list =[]
list.insert(0, 'red')
list.insert(1, 'yellow')
list.insert(1, 'blue')
print("list after insert: ", list)
list.remove('yellow')
print("list after removing:", list)

list.append('black')
print('list after appending: ',list)


leng=len(list)
print("length of the list: ",leng)

popped_item = list.pop()
popped_item1 = list.pop(0)
print("last item popped: ",popped_item)
print("Specific item popped: ",popped_item1)



list.clear()
print("list cleared: ",list)


# In[1]:


tup1 = ('apple', 'banana', 'grapes')

new_tup = ("cherry", "dates")
tup1 = tup1 + new_tup
print("tuple after adding item: ",tup1)

tup_len = len(tup1)
print("length of tuple: ",tup_len)

item= 'grapes'
item_present = item in tup1
print(f"Does '{item}' exists in the tuple?: ",item_present) 
first_itm = tup1[0]
print("the first element in the tuple:",first_itm)
first_itm2 = tup1[2]
print("the second element in the tuple:",first_itm2)
range_of_items = tup1[1:4]
print("items from index 1 to 3: ",range_of_items) 


# In[ ]:




