# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        def process(self, lst):
            n = []
            cond = True
            currentNode = lst
            
            while cond:
                n.insert(0, str(currentNode.val))
                if currentNode.next == None:
                    cond = False
                else:
                    currentNode = currentNode.next
            return n

        number1 = int(''.join(process(self, l1)))
        number2 = int(''.join(process(self, l2)))

        answer = number1 + number2
        answer_list = [int(i) for i in str(answer)]
        answer_list.reverse()

        head = None
        tail = None
        for i in answer_list:
            new_node = ListNode(i)
            
            if head == None: 
                head = new_node
            
            if tail != None:
                tail.next = new_node
            
            tail = new_node
        
        return head
