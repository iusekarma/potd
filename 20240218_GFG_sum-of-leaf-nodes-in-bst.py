#User function Template for python3

##Structure of node
'''
class Node:
    def __init__(self, data=0):
        self.data=0
        self.left=None
        self.right=None
'''

class Solution:
    
    def sumOfLeafNodes(self, root):
        if root.left == None and root.right == None:
            return root.data
        else:
            s = 0
            if root.left:
                s += self.sumOfLeafNodes(root.left)
            if root.right:
                s += self.sumOfLeafNodes(root.right)
            return s
