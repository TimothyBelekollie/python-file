# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 11:34:27 2023

@author: Timothy Belekollie

"""

# the code immediately below is about reading opening file in python
'''
there are different mode in python file manipulation:
    read
    write
    append and just many more
'''

file = open("/Users/belek/Desktop/Data Science/File/words.txt")

# if you want read file in python
file.read()

file.close()


# the key word with helps us to alias a file as simple name to use.
with open("words.txt","r") as f:
 content=f.read()
 
 print(content)
 # writing to a file
 #newfile=open("words.txt","w")
 #appending to a file
 newfile=open("words.txt","a")
 newfile.write("I want to add something here")
 newfile.close()
 print(newfile)
 
 oldfile=open("words.txt","r");
 print(oldfile);
 
 
     
     
