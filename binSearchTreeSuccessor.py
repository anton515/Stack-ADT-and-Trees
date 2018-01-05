

import check

class Node:
    '''
    Node
    '''
    # initialization of the bst node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    ## equality for testing purposes
    #def __eq__(self,other):
        #return self.key == other.key

## get_successor(bstnode) finds the successor of a given node in a binary search
## tree. Where the successor of a given node is defined as the node with the 
## smallest key greater than the key of the given node.
## get_successor: Node -> (anyof Node None)
## Requires: Input to be the node (bstnode) in which we are finding the 
## the successor to.

        
def get_successor(bstnode):
    #case with no tree/ no node
    if bstnode == None:
        return None
    #case where it's a leaf node
    elif bstnode.parent != None and bstnode.left == None and bstnode.right == None:
        if bstnode.parent.key > bstnode.key:
            return bstnode.parent
        else:
            return None
    elif bstnode.left == None and bstnode.right == None:
        return None
    #case where it is interior node, with left subtree (no right subtree)
    elif bstnode.parent != None and bstnode.right == None:
        if bstnode.parent.key > bstnode.key:
            return bstnode.parent
        else:
            return None
    elif bstnode.right == None:
        return None
    #case where it is interior node, with right subtree
    elif bstnode.left == None:
        node = bstnode.right
        if node.left == None:
            return node
        else:
            end = False
            while end == False:
                if node.left != None:
                    node = node.left
                else: end = True
        return node
    else: #other case
        node = bstnode.right
        if node.left == None:
            return node
        else:
            #go left all the way
            end = False
            while end == False:
                if node.left != None:
                    node = node.left
                else:
                    end = True
            return node  


    

## Test bst

k = Node(23)
l = Node(37)
i = Node(29)
h = Node(1)
j = Node(84)
d = Node (4)
e = Node (41)
f = Node(71)
g = Node(100)
b = Node(12)
c = Node(90)
a = Node(60)

k.left = None
k.right = None
k.parent = i

l.left = None
l.right = None
l.parent = i

i.left = k
i.right = l
i.parent = e

h.left = None
h.right = None
h.parent = d

j.left = None
j.right = None
j.parent = f

d.left = h
d.right = None
d.parent = b

e.left = i
e.right = None
e.parent = b

f.left = None
f.right = j
f.parent = c

g.left = None
g.right = None
g.parent = c

b.left = d
b.right = e
b.parent = a

c.left = f
c.right = g
c.parent = a

a.left = b
a.right = c
a.parent = None

check.expect("Q1T0",get_successor(None),None)
t1 = Node(71)
check.expect("Q1T1",get_successor(a).key,t1.key)
t2 = Node(23)
check.expect("Q1T2",get_successor(b).key,t2.key)
t3 = Node(100)
check.expect("Q1T3",get_successor(c).key,t3.key)
check.expect("Q1T4",get_successor(d),None)
check.expect("Q1T5",get_successor(e),None)
t4 = Node(84)
check.expect("Q1T6",get_successor(f).key,t4.key)
check.expect("Q1T7",get_successor(g),None)
check.expect("Q1T8",get_successor(h),None)
t5 = Node(37)
check.expect("Q1T9",get_successor(i).key,t5.key)
check.expect("Q1T10",get_successor(j),None)
check.expect("Q1T11",get_successor(k),None)
check.expect("Q1T12",get_successor(l),None)