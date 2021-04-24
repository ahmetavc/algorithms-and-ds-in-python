class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def appendToTail(self, data):
        self.length += 1

        if not self.head:
            self.head = Node(data)
            return
        
        cur = self.head

        while cur.next:
            cur = cur.next

        cur.next = Node(data)

    def appendToHead(self, data):
        self.length += 1
        self.head = Node(data, self.head)

    def deleteFromTail(self):
        if self.length == 0:
            return

        if self.length == 1:
            self.length -=1 
            self.head = None
            return
        
        self.length -= 1
        cur = self.head

        while cur.next.next:
            cur = cur.next

        cur.next = None
    
    def deleteFromHead(self):
        if self.length == 0:
            return
        
        self.length -=1
        self.head = self.head.next

    def search(self, data):
        cur = self.head

        while cur and cur.data != data:
            cur = cur.next

        return cur

    def delete(self, data):
        if self.head and self.head.data == data:
            self.head = self.head.next
            self.length -= 1
            return

        cur = self.head
        
        while cur and cur.next:
            if cur.next.data == data:
                self.length -= 1
                cur.next = cur.next.next
                return
            cur = cur.next

    
    def printItself(self):
        cur = self.head
        print("length: ", self.length)

        while cur:
            print(cur.data)
            cur = cur.next
