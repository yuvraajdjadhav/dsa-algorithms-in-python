class Node:
    def __init__(self,val):
        self.data = val
        self.next = None


class LinkList:
    def __init__(self):
        # Initialize the linked list with head as None and number of nodes as 0
        self.head = None
        self.n = 0
    
    def __len__(self):
        # Return the number of nodes in the linked list
        return self.n
    
    def insert_head(self, value):
        # Insert a new node at the head of the linked list
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def __str__(self):
        # Return a string representation of the linked list
        result = ''
        curr = self.head
        while curr != None:
            result += str(curr.data) + " ==>"
            curr = curr.next
        return result[:-3]
    
    def append(self, value):
        # Append a new node at the end of the linked list
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        # You are at the end of the list
        curr.next = new_node
        self.n += 1
    
    def insert_after(self, after, value):
        # Insert a new node after a given node in the linked list
        new_node = Node(value)
        curr = self.head
        while curr is not None:
            if curr.data == after:
                break
            curr = curr.next
        if curr is not None:
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return "Item not found"
    
    def clear(self):
        # Clear the linked list
        self.head = None
        self.n = 0

    def delete_head(self):
        if self.head is None:
            return "Empty LL"
        
        self.head = self.head.next

    def pop(self):
        print(self.head)


# Note: The Node class is assumed to be defined elsewhere


L = LinkList()

L.append(15)
L.append(12)
L.append(32)
L.append(55)

print(L)

L.insert_after(12, 100)
print(L)
L.delete_head()
print(L)

L.pop()
