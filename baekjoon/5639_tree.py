import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def get_postorder(start, end):
    global preorder
    if start > end:
        return
        
    parent = preorder[start]
    idx = -1
    for i in range(start+1, end+1):
        if preorder[i] > parent:
            idx = i
            break
    
    if idx == -1:
        get_postorder(start+1,end)
    else:
        get_postorder(start+1,idx-1)
        get_postorder(idx,end)
    
    print(parent)

preorder = []   

while True:
    try:
        preorder.append(int(input()))
    except:
        break
get_postorder(0, len(preorder)-1)


