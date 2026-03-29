class TreeNode:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left = left
        self.right = right
    def find_index(self,lst,value):
        pass
def tree_from_traversals(preorder, inorder):
    if len(preorder) != len(inorder):
        raise ValueError("traversals must have the same length")
    
    if set(preorder) != set(inorder):
        raise ValueError("traversals must have the same elements")
    
    if len(preorder) != len(set(preorder)):
        raise ValueError("traversals must contain unique items")
    if not preorder:
        return {}
    root_value = preorder[0]
    root_index = inorder.index(root_value)
    left_inorder = inorder[:root_index]
    right_inorder = inorder[root_index+1:]
    left_preorder = preorder[1:1+len(left_inorder)]
    right_preorder = preorder[len(left_inorder)+1:]
    left_child = tree_from_traversals(left_preorder,left_inorder)
    right_child = tree_from_traversals(right_preorder,right_inorder)
    return {
        'v':root_value,
        'l':left_child,
        'r':right_child
        
    }
    
