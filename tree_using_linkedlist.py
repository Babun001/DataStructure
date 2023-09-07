class BSTree:
    def __init__(self, data):
        self.info=data
        self.lchild=None
        self.rchild=None
        
    def insert(self, item):
        if item==self.info:
            return
        if item < self.info:
            if self.lchild is None:
                self.lchild=BSTree(item)
            else:
                self.lchild.insert(item)
        else:
            if self.rchild is None:
                self.rchild=BSTree(item)
            else:
                self.rchild.insert(item)

    def preorder(self, root):
        if(root!=None):
            print(root.info,end=" ")
            self.preorder(root.lchild)
            self.preorder(root.rchild)

    def inorder(self, root):
        ls=[]
        if root:
            ls=self.inorder(root.lchild)
            ls.append(root.info)
            ls=ls+self.inorder(root.rchild)
        return ls

    def postorder(self, root):
        if(root!=None):
            self.postorder(root.lchild)
            self.postorder(root.rchild)
            print(root.info,end=" ")


    def count_node(self, root):
        if root==None:
            return 0
        else:
            return (self.count_node(root.lchild)+ self.count_node(root.rchild)+1)

    def count_leafnode(self, root):
        if root == None:
            return 0
        elif (root.lchild==None and root.rchild==None):
            return 1
        else:
            return (self.count_leafnode(root.lchild)+self.count_leafnode(root.rchild))
        
    def count_nonleafnode(self, root):
        if root == None:
            return 0
        elif (root.lchild==None and root.rchild==None):
            return 0
        else:
            return (self.count_nonleafnode(root.lchild)+self.count_nonleafnode(root.rchild)+1)
        

    def largest_node(self, root):
        if root == None or root.rchild==None:
            return root.info
        else:
            return self.largest_node(root.rchild)
    
    def smallest_node(self, root):
        if root == None or root.lchild==None:
            return root.info
        else:
            return self.smallest_node(root.lchild)

    def del_bst(self, root, item):
        if root==None:
            print("\nNothing to Delete!")
            return
        elif (item < root.info):
            root.lchild=self.del_bst(root.lchild, item)
        elif (item > root.info):
            root.rchild=self.del_bst(root.rchild, item)
        else:
            tmp=root
            if root.lchild==None:
                tmp=root.rchild
                root=None
                return tmp
            elif (root.rchild==None):
                tmp=root.lchild
                root=None
                return tmp
            x=self.smallest_node(root.rchild)
            root.info=x
            root.rchild=self.del_bst(root.lchild, x)
        return root
        
if __name__=="__main__":
    x=int(input("\nEnter the value of the root node:"))
    tree=BSTree(x)
    tree.insert(75)
    tree.insert(52)
    tree.insert(22)
    tree.insert(11)
    tree.insert(80)
    tree.insert(30)
    tree.insert(92)
    tree.insert(15)
    ls=[]
    print("\nElements of the tree in Pre-Order are:")
    tree.preorder(tree)
    ls=tree.inorder(tree)
    print("\nElements of the tree in In-Order are:",ls)
    print("Elements of the tree in Post-Order are:")
    tree.postorder(tree)
    r1=tree.count_node(tree)
    print("\nTotal number of nodes in Binary Search Tree:",r1)
    r2=tree.count_leafnode(tree)
    print("\nTotal number of leaf nodes in Binary Search Tree:",r2)
    r3=tree.count_nonleafnode(tree)
    print("\nTotal number of non leaf nodes in Binary Search Tree:",r3)
    r4=tree.largest_node(tree)
    print("\nLargest Node in the Binary Search Tree:",r4)
    r5=tree.smallest_node(tree)
    print("\nSmallest Node in the Binary Search Tree:",r5)
    y=int(input("\nEnter the node to be deleted:"))
    tree=tree.del_bst(tree, y)
    ls=tree.inorder(tree)
    print("\nElements of the tree in In-Order are:",ls)
          
