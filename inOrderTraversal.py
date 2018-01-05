
from dataStructures import BinTreeNode, Stack
import check

## inorderTraversal(root) returns the inorder traversal of its nodes' values 
## using Stack. Returns a list of integers of the tree nodes' values.
## inorderTraversal: BinTreeNode -> lst of Int
## Requires: root to be a root node of BinTreeNode type
def inorderTraversal(root):
    mystack = Stack ()
    lst = []
    untouchedStack = True
    while untouchedStack == True:
        if root != None:
            mystack.push(root)
            root = root.left  
        else:
            if not mystack.isEmpty():
                root = mystack.pop()
                lst.append(root.data)
                root = root.right
            else:
                untouchedStack = False
    return lst

## Tests

# Perfect Binary Tree
d = BinTreeNode(11,None,None)
e = BinTreeNode(25,None,None)
f = BinTreeNode(29,None,None)
g = BinTreeNode(96,None,None)
c = BinTreeNode(30,f,g)
b = BinTreeNode(20,d,e)
a = BinTreeNode(10,b,c)
check.expect("Q4T1",inorderTraversal(a),[11,20,25,10,29,30,96])

# Tree one Node
one = BinTreeNode(50,None,None)
check.expect("Q4T2",inorderTraversal(one),[50])

# No Tree
check.expect("Q4T3",inorderTraversal(None),[])

# Full Binary Tree
h1 = BinTreeNode(10,None,None)
i1 = BinTreeNode(6,None,None)
j1 = BinTreeNode(77,None,None)
k1 = BinTreeNode(99,None,None)
d1 = BinTreeNode(5,None,None)
e1 = BinTreeNode(80,h1,i1)
f1 = BinTreeNode(11,None,None)
g1 = BinTreeNode(100,j1,k1)
b1 = BinTreeNode(15,d1,e1)
c1 = BinTreeNode(50,f1,g1)
a1 = BinTreeNode(21,b1,c1)
check.expect("Q4T4",inorderTraversal(a1),[5,15,10,80,6,21,11,50,77,100,99])

