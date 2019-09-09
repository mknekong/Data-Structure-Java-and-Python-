# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 19:26:02 2019

@author: mankup
"""

class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class link_list:
    def __init__(self):
        #pointer that points the first element
        self.head = node()
        
    #insertion
    def append(self,data):
        new_node = node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        
    #traversal (find the length)
    def length(self):
        curr = self.head
        total = 0
        while curr.next!=None:
            total +=1
            curr = curr.next
        print( total)
    
    #Display the current content of linked list
    def Display(self):
        element = []
        curr_node = self.head
        while curr_node.next!=None:
            curr_node = curr_node.next
            element.append(curr_node.data)
        print(element)
        
    def Delete(self,index):
        if index>= self.length():
            print("Error")
            return
        curr_index = 0
        curr_node = self.head
        while True:
            last_node = curr_node
            curr_node = curr_node.next
            if curr_index == index:
                last_node.next = curr_node.next
                return
            curr_index +=1
            
       
    #getting the index of the list
    def get(self,index):
        if index >= self.length():
            print("ERROR: Index out of range")
            return None
        curr_index = 0
        curr_node = self.head
        while True:
            curr_node = curr_node.next
            if curr_index == index:
                return curr_node.data
            curr_index+=1
 
           
        
my_list = link_list()
my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append(5)
my_list.Display()
my_list.length() 
print("Element at second index: %d",my_list.Delete(2))     