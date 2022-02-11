
from telnetlib import STATUS


class nodes:
    def __init__(self, val=0) -> None:
        self.val = val
        self.next = None


class Linkedlist:
    def __init__(self) -> None:
        self.head = None

    def push(self, val):
        newnode = nodes(val)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        
        temp = self.head
        while temp:
            
            print(temp.val)
            temp = temp.next

    def twosum(self, l1, l2):
        carry = 0
        output = nodes()
        tail = output
        k=l1
        
        
        while l1 or l2 or carry:
            

            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            agg = val1+val2+carry
            val3 = agg % 10
            carry = val3/10

            tail.next = nodes(val3)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            return output.next
