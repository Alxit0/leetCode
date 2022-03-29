from typing import Optional, List
from Structs.Binary_Tree import TreeNode, create_tree, print_tree


def inorderTraversal(root: Optional[TreeNode]) -> List[int]:
    # if root is None:
    #     return []
    #
    # resp = []
    # resp += inorderTraversal(root.left) + [root.val] + inorderTraversal(root.right)
    # return resp
    resp = []
    stack = []
    cur = root
    while stack or cur:
        while cur:
            stack.append(cur)
            cur = cur.left
        node = stack.pop()
        resp.append(node.val)
        cur = node.right
    return resp



def main():
    a = [1, 2, None, 4, 5, 6, 7, 8]
    h = create_tree(a)
    print_tree(h)
    print(inorderTraversal(h))



if __name__ == '__main__':
    main()
