import os
os.system('cls')

class Node:
    def __init__(self,data) :
        self.data = data
        self.right = None
        self.left = None
def storeBSTNodes(root,nodes):
    if not root:
        return
    storeBSTNodes(root.left,nodes)
    nodes.append(root)
    storeBSTNodes(root.right,nodes)
    
def buildTreeUtil(nodes,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    node = nodes[mid]
    node.left = buildTreeUtil(nodes,start,mid-1)
    node.right = buildTreeUtil(nodes,mid+1,end)
    return node

def buildTree(root):
    nodes = []
    storeBSTNodes(root,nodes)
    n = len(nodes)
    return buildTreeUtil(nodes,0,n-1)

def preOrder(root):
    if not root:
        return
    print(root.data,end=" ")
    preOrder(root.left)   
    preOrder(root.right) 
    
if __name__ == "__main__":
    root = Node(10)
    root.left = Node (8)   
    root.left.left = Node (7)   
    root.left.left.left = Node (6)   
    root.left.left.left.left = Node (5)
    root = buildTree(root)
    preOrder(root)