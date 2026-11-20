class Node:
    def __init__(self,key,val,left = None, right = None):
        self.key = key
        self.val = val
        self.left= left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None

    def insert(self, key: int, val: int) -> None:
        
        if not self.root:
            self.root = Node(key,val)
            return

        parent = None
        node   = self.root

        while node:
            parent = node
            if key < node.key:
                node = node.left
            elif key > node.key:
                node = node.right
            
            # Node already exists
            else:
                node.val = val
                return
        
        # New node
        new_node = Node(key,val)
        if key < parent.key:
            parent.left = new_node
        
        else:
            parent.right = new_node

    def get(self, key: int) -> int:        
        
        node = self.root
        while node:
            if node.key == key:
                return node.val
            if key < node.key:
                node = node.left
            else:
                node = node.right 
        
        return -1


    def getMin(self) -> int:

        if not self.root:
            return -1

        node = self.root

        while node.left:
            node = node.left
        
        return node.val


    def getMax(self) -> int:
        if not self.root:
            return -1

        node = self.root

        while node.right:
            node = node.right
        
        return node.val


    def remove(self, key: int) -> None:

        def delete(root, key):
            if not root:
                return None
            
            if key < root.key:
                root.left =  delete(root.left,key)
            
            elif key > root.key:
                root.right =  delete(root.right, key)
            
            # case1,2 : only one child
            else:
                if not root.right:
                    return root.left
                
                if not root.left:
                    return root.right
                
                # case 3

                # 1. find the right most left subtree or left most from right subtree
                successor = root.right

                while successor.left:
                    successor = successor.left
                
                # 2. copy the successor value to root and delete the successor
                root.key, root.val = successor.key, successor.val

                # 3. now adjust the right tree
                root.right = delete(root.right, successor.key)

            return root
        
        self.root = delete(self.root,key)


    def getInorderKeys(self) -> List[int]:

        res = []

        def dfs(root):

            if not root:
                return 
            
            dfs(root.left)
            res.append(root.key)
            dfs(root.right)

        dfs(self.root)

        return res
        

