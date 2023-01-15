print("************  PROGRAMMED BY  ************")
print("********* HYDEE LYN C. PALISOC *********\n")

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return 
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    
    def search(self, val):
        if self.data == val:
            return True
            
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
            
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
        
    def in_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def post_order_traversal(self):
        elements = []
        if self.left:
            elements += self.left.post_order_traversal()
        if self.right:
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self):
        elements = [self.data]
        if self.left:
            elements += self.left.pre_order_traversal()
        if self.right:
            elements += self.right.pre_order_traversal()

        return elements
        
    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()
        
    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()
        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root
        
if __name__ == '__main__':
    alphabet = ["H", "Y", "D", "E", "E", "L", "Y", "N", "C", "P", "A", "L", "I", "S", "O", "C"]

    
    alphabet_tree = build_tree(alphabet)
    print("\tCharacters:",alphabet)
    print("Min:",alphabet_tree.find_min())
    print("Max:",alphabet_tree.find_max())
    print("In order traversal:", alphabet_tree.in_order_traversal())
    print("Pre order traversal:", alphabet_tree.pre_order_traversal())
    print("Post order traversal:", alphabet_tree.post_order_traversal())



