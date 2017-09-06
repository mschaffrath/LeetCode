# 2. Add Two Numbers

# Description:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Solution 
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(0)
        l3 = head
        carry = 0
        while(l1 != None or l2!= None):
            l3.next = ListNode(0)
            l1value = 0
            l2value = 0
            
            if(l1 != None):
                l1value = l1.val
            if(l2 != None):
                l2value = l2.val
            
            l3.next.val = (l1value + l2value + carry)
            if(l3.next.val > 9):
                carry = 1
                l3.next.val = l3.next.val % 10
            else:
                carry = 0
            
            if(l1 != None):
                l1 = l1.next
            if(l2 != None):
                l2 = l2.next
            
            l3 = l3.next

        if(carry == 1):
            l3.next = ListNode(1)
            
        return head.next

# Build Linked-List from List
def LLBuilder(list):
    newList = ListNode(0)
    listHead = newList
    for i in range(0, len(list)):
        newList.next = ListNode(list[i])
        newList = newList.next
    return listHead.next

# Print Linked-List
def PrintLL(LL):
    while(LL != None):
        print(LL.val, end='  ')
        LL = LL.next
    print("")


# Main
l1 = LLBuilder([1, 5, 3])
l2 = LLBuilder([3, 6, 1])
l3 = LLBuilder([])
l4 = LLBuilder([5])
Sol = Solution()

Ans = Sol.addTwoNumbers(l1, l2)
print("Input 1: ", end='')
PrintLL(l1)
print("Input 2: ", end='')
PrintLL(l2)
print("Solution: ", end='')
PrintLL(Ans)
print("")

Ans = Sol.addTwoNumbers(l1, l3)
print("Input 1: ", end='')
PrintLL(l1)
print("Input 2: ", end='')
PrintLL(l3)
print("Solution: ", end='')
PrintLL(Ans)
print("")

Ans = Sol.addTwoNumbers(l3, l3)
print("Input 1: ", end='')
PrintLL(l3)
print("Input 2: ", end='')
PrintLL(l3)
print("Solution: ", end='')
PrintLL(Ans)
print("")

Ans = Sol.addTwoNumbers(l4, l4)
print("Input 1: ", end='')
PrintLL(l4)
print("Input 2: ", end='')
PrintLL(l4)
print("Solution: ", end='')
PrintLL(Ans)
print("")