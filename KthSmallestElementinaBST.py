class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #BST - Inorder Traversal   >> sorted resultl
        #Left >> Root >> Right
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)   
        inorder(root)
        return res[k-1]
