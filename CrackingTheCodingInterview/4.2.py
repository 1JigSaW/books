class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def sortedArrayToBST(num):
    if not num:
        return None

    mid = len(num) // 2

    root = TreeNode(num[mid])
    root.left = sortedArrayToBST(num[:mid])
    root.right = sortedArrayToBST(num[mid+1:])

    return root

print(sortedArrayToBST([1,2,3,4,5,6]))