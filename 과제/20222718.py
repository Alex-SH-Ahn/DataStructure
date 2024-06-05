class LinkedList:
    def __init__(self):
        self.head = None

    def isEmpty(self): return self.head == None
    def clear(self): self.head = None
    def size(self):
        n = self.head
        count = 0
        while n != None:
            count += 1
            n = n.link
        return count

    def display(self, msg):
        print(msg, end='')
        n = self.head
        while n != None:
            print(n.data, end=' ')
            n = n.link
        print()
    
    def getNode(self, pos):
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node
    
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None: return None
        else: return node.data
    
    def insert(self, pos, elem):
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem, self.head)
        else:
            before.link = Node(elem, before.link)
    
    def delete(self, pos):
        before = self.getNode(pos-1)
        if before == None:
            if self.head == None: return None
            self.head = self.head.link
        else:
            if before.link == None: return None
            before.link = before.link.link
    
    def deleteFirst(self):
        if self.head == None: return None
        else:
            self.head = self.head.link
    
    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = Node(data)