# binary tree traversal
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_preorder(post_start, post_end, in_start, in_end):
    global postorder, inorder, preorder
    if in_end == in_start:
        preorder.append(inorder[in_start])
        return
    elif in_end < in_start == 0:
        return
    else:
        parent = postorder[post_end]
        preorder.append(parent)
        idx = inorder.index(parent)
        left_st = inorder[in_start:idx]
        right_st = inorder[idx+1:in_end+1]
        get_preorder(post_start, post_start + len(left_st)-1, in_start, idx-1)
        get_preorder(post_start + len(left_st), post_end-1, idx+1, in_end)
    
    
n = int(input())
inorder = list(map(int, input().split(' ')))
postorder = list(map(int, input().split(' ')))
preorder = []
get_preorder(0, n-1, 0, n-1)
print(*preorder)