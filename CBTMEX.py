from collections import deque

class Node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
        
class Binary:
    def __init__(self,root):
        self.root=root
        
    def inorder(self,start,show):
        if start:
            show=self.inorder(start.left, show)
            show.append(start.value)
            show=self.inorder(start.right, show)
        return show
    
def Tree(lis,root,i,n):
        if i<n:
            temp=Node(lis[i])
            root=temp
            root.left=Tree(lis,root.left,2*i+1,n)
            root.right=Tree(lis,root.right,2*i+2,n)
        return root
    
def main(z):
    root = None
    root = Tree(z,root,0,len(z))
    bi=Binary(root)
    print(bi.inorder(root, []))
    #print(route(root))
    printRootToLeafPath(root)
    
# def route(root):
#         path=[]
        
#         printRoute(root,path,0)
        
# def printRoute(root,path,length):
#     if root == None:
#         return 
#     if len(path)>length:
#         path[length]=root.value
#     else:
#         path.append(root.value)
        
#         length=length+1
        
#     if root.left is None and root.right is None:
#         arr(path,length)
        
#     else:
#         printRoute(root.left,path,length)
#         printRoute(root.right,path,length)
        
# def arr(ints, len):
# 	for i in ints[0 : len]:
# 		print(i," ",end="")
# 	print()      

# def MEX(qw):
#     count=0
#     #qw.sort()
#     #print('qw',qw)
#     for i in range(0,len(qw)):
#         if qw[i]==None:
#             qw.pop(i)
#     print('new qw',qw)
    
#     qw.sort()
#     for i in range(1,len(qw)):
#         if qw[i]!=i:
#             last.append(qw[i])
#             count=1
#     if count==0:
#             qw.append(i+1)
    # for i in range(0,len(qw)):
    #     if qw[i]!=i+1:
    #         print(i)

def isLeaf(node):
    return node.left is None and node.right is None
 
 
# Recursive function to find paths from the root node to every leaf node
def printRootToLeafPaths(node, path):
 
    # base case
    if node is None:
        return
 
    # include the current node to the path
    path.append(node.value)
 
    # if a leaf node is found, print the path
    if isLeaf(node):
        sw=[]
        print(list(path))
        #print(sw)
        
        #MEX(sw)
 
    # recur for the left and right subtree
    printRootToLeafPaths(node.left, path)
    printRootToLeafPaths(node.right, path)
 
    # backtrack: remove the current node after the left, and right subtree are done
    path.pop()
 
 
# The main function to print paths from the root node to every leaf node
def printRootToLeafPath(node):
 
    # list to store root-to-leaf path
    path = deque()
    printRootToLeafPaths(node, path)   
    
if __name__ == '__main__':
    
    
 last=[]
 #v=[1,3,2,2,4,2]
 #p=[1,1,2,2,5]
 T=int(input())
 for i in range(0,T):
  N=int(input())
  v=list(map(int,input().split())) 
  p=list(map(int,input().split()))
  a=[]
  for i in range(0,len(p)):
    s=p[i]
    ss=v[s-1]
    a.append(ss)
  #print(a)

  z=[1]
  i=0
  j=i
  for i in range(0,len(v)):
    if a.count(v[i])==2:
        
        z.append(v[j+1])
        z.append(v[j+2])
        j=j+2
    if a.count(v[i])==1:
        z.append(v[j+1])
        z.append(None)
        j=j+1
    if v[i] not in a:
        z.append(None)
        z.append(None)

  z.reverse()
  s=0
  while s==0:
     if z[s]==None:
        #print(z[s])
        z.pop(s)
        
     if z[s]!=None:
        s=1
        break
  z.reverse() 
  main(z)
