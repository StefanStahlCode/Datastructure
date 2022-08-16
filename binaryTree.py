#Tree represents the nodes connected by edges. It is a non-linear data structure. It has the following properties −
#One node is marked as Root node.
#Every node other than the root is associated with one parent node.
#Each node can have an arbiatry number of child nodes.

#A Binary Tree can have up to 2 children
#here Binary Tree
#A Binary Search Tree (BST) inserts any element on the left or right of the node, depending if it is smaller or bigger
#the following code has a binary search tree
#includes both a search function for normal and BSt Trees



class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        self.current = self.root #Node to move around
    #simple insert method for BST
    def insert(self, value):
        #start recursion
        self.insert_help(value, self.root)
        
    def insert_help(self, value, curr):
        if curr:
            if curr.value > value:
                if curr.left is None:
                    curr.left = Node(value)
                else:
                    self.insert_help(value, curr.left)
            else:
                if curr.right is None:
                    curr.right = Node(value)
                else:
                    self.insert_help(value, curr.right)

        else:
            self.current = Node(value)
        

    #in Order traversal, start with left subtree, root, right subtree
    def printTree(self):
        self.printTree_help(self.root)

    def printTree_help(self, curr):
        if curr.left:
            self.printTree_help(curr.left)
        print(curr.value)
        if curr.right:
            self.printTree_help(curr.right)


    #pre order traversal: root visited first, then left, then right, here return as list, converted to string
    def print_pre_order(self):
        ret_str = ""
        ret_str = ret_str + self.print_pre_order_helper(self.root, ret_str)
        print(ret_str[:-1])

    def print_pre_order_helper(self, curr, ret_str):
        ret_str = ret_str + str(curr.value) + "-"
        if curr.left:
            ret_str = self.print_pre_order_helper(curr.left, ret_str)
        if curr.right:
            ret_str = self.print_pre_order_helper(curr.right, ret_str)
        return ret_str


    # function to compare preorder fucntion, which returns a string, should have named it better
    def printTree_preorder_compare(self):
        self.print_pre_order_help_compare(self.root)

    def print_pre_order_help_compare(self, curr):
        print(curr.value)
        if curr.left:
            self.print_pre_order_help_compare(curr.left)
        if curr.right:
            self.print_pre_order_help_compare(curr.right)


    #post order traversal, this time returned as list, Order: left -> right -> root
    def print_post_order(self):
        ret = []
        ret.append(self.print_post_order_helper(self.root, ret))
        print(ret[:-1])
    
    def print_post_order_helper(self, curr, ret_val):
        if curr.left:
            self.print_post_order_helper(curr.left, ret_val)
        if curr.right:
            self.print_post_order_helper(curr.right, ret_val)
        return ret_val.append(curr.value)
    

    #normal Binary Tree search function
    def search(self, search_value):
        boo = False
        boo = self.preorder_search(self.root, search_value, boo)
        return boo


    def preorder_search(self, curr, search_value, boo):
        if boo == True:
            return True
        if curr.value == search_value:
            boo = True
        if curr.left:
            boo = self.preorder_search(curr.left, search_value, boo)
        if curr.right:
            boo = self.preorder_search(curr.right, search_value, boo)
        return boo

        
    # Binary Search Tree search function
    def search_BST(self, search_value):
        boo = False
        boo = self.preorder_search(self.root, search_value, boo)
        return boo

    def search_BST_preorder(self, curr, search_value, boo):
        if boo == True:
            return True
        if curr.value == search_value:
            boo = True
        elif search_value < curr.value:
            if curr.left:
                boo = self.search_BST_preorder(curr.left, search_value, ret_list)
        else:
            if curr.right:
                boo = self.search_BST_preorder(curr.right, search_value, ret_list)
        return boo 

root = BinaryTree(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(7)
#root.printTree()
root.print_pre_order()
root.printTree_preorder_compare()
print("Normal Binary",root.search(7))
print(root.search(8))
print("BST", root.search_BST(7))
print(root.search_BST(8))
root.print_post_order()