class NodeSinglyLinkedList:
    """
    Singly linked list node
    """
    def __init__(self,key=0):
        self.key = key
        self.next = None
        
    def get_key(self):
        return self.key
    
    def set_key(self,key):
        self.key = key

    def get_nxt(self):
        return self.next
    
    def set_nxt(self,next):
        self.next = next

#%% SinglyLinkedList class
class SinglyLinkedList:
    """
    Singly linked list, with head pointer only
    Insertion at the head
    """
    def __init__(self):
        self.head = None
        
    def empty(self):
        if self.head == None:
            return True
        else:
            return False

    def insert_head(self, key):
        #create a new node and set key
        node = NodeSinglyLinkedList(key)

        #node inserted at head, so its next should point to where the list head was pointing
        node.nxt = self.head

        #the list's head should now be updatd to point at this new node
        self.head = node

    def search_key(self,key):
        node = self.head
        while node != None and node.key != key:
            node = node.nxt
        return node    

    def size(self):
        count = 0
        node = self.head
        while node != None:
            count+=1
            node = node.nxt
        return count


        
    def print_all_keys(self):
        node = self.head
        while node != None:
            print(node.key)
            node = node.nxt


#%% Test SinglyLinkedList
# =============================================================================
ll = SinglyLinkedList()
ll.empty()
ll.insert_head(1)
ll.insert_head(2)
ll.insert_head(3)
ll.insert_head(4)
ll.empty()
ll.print_all_keys()
ll.size()
if ll.search_key(3): print ("Found key")
if ll.search_key(13): print("Found key")
# =============================================================================        
# %%