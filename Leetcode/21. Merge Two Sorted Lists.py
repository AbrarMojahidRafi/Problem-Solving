# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = currentNode = ListNode() 
        while list1 and list2: 
            if list2.val <= list1.val: 
                currentNode.next = list2 
                currentNode = currentNode.next 
                list2 = list2.next 
            else: 
                currentNode.next = list1
                currentNode = currentNode.next
                list1 = list1.next 
         
            
        if list1: 
            currentNode.next = list1
        elif list2:
            currentNode.next = list2
        return dummy.next 
      
