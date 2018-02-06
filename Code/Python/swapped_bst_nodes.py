# bst class/functionality

class node(object):
    def __init__(self, val):
        self.val=val
        self.l=0
        self.r=0
        
def put_in_bst(val,cur_node):
    if val >= cur_node.val:
        if not cur_node.r:
            cur_node.r = node(val)
        else:
            put_in_bst(val,cur_node.r)
    if val < cur_node.val:
        if not cur_node.l:
            cur_node.l = node(val)
        else:
            put_in_bst(val,cur_node.l)

root = node(5)
put_in_bst(3, root)
put_in_bst(2, root)
put_in_bst(4, root)
put_in_bst(7, root)

def dfs_print(cur_node):
    if cur_node.l:
        dfs_print(cur_node.l)
    print(cur_node.val, end=" ")
    if cur_node.r:
        dfs_print(cur_node.r)

print("bst functionality:")        
dfs_print(root)
print("")

# examples
# first is fine
# next three have two nodes swapped
'''
    5
  3     7    
2   4

    5
  3   2 
7   4

    5
  4   7
2   3

     4
  3     7 
2   5
'''

def LCR(cur_node):
    if cur_node.l and cur_node.r:
        return LCR(cur_node.l) + [cur_node] + LCR(cur_node.r)
    if cur_node.l:
        return LCR(cur_node.l) + [cur_node]
    if cur_node.r:
        return cur_node  + LCR(cur_node.r)
    if not (cur_node.l or cur_node.r):
        return [cur_node]

def fix(root):
    lst = LCR(root)
    for i,n1 in enumerate(lst[:-1]):
        if n1.val > lst[i+1].val:
            break
    lst.reverse()
    for i,n2 in enumerate(lst[:-1]):
        if n2.val < lst[i+1].val:
            break    
    n1.val, n2.val = n2.val, n1.val
    return root

print("\ncase: fine tree")
root = node(5)
put_in_bst(3, root)
put_in_bst(2, root)
put_in_bst(4, root)
put_in_bst(7, root)
dfs_print(root)
print("")
root = fix(root)
dfs_print(root)
print("")

print("\ncase: shared ancestor")
root.l.l.val = 7
root.r.val = 2
dfs_print(root)
print("")
root = fix(root)
dfs_print(root)
print("")

print("\ncase: flipped parent")
root.l.val = 4
root.l.r.val = 3
dfs_print(root)
print("")
root = fix(root)
dfs_print(root)
print("")

print("\ncase: flipped root")
root.val = 4
root.l.r.val = 5
dfs_print(root)
print("")
root = fix(root)
dfs_print(root)
print("")




if __name__ == "__main__":
    a=int(input("Add an integer valued node to tree, or enter -1 to stop: "))
    root = node(a)
    while a != -1:
        a=int(input("Add an integer valued node to tree, or enter -1 to stop: "))
        if a != -1:
            put_in_bst(a, root)
 
    print("DFS on tree:")
    dfs_print(root)
    print("")

    a=int(input("Choose 1st distinct number to swap (must be present in tree): "))
    b=int(input("Choose 2nd distinct number to swap (must be present in tree): "))

    def get_node(cur_node, a):
        if cur_node.val == a:
            return cur_node
        if a < cur_node.val:
            return get_node(cur_node.l, a)
        else:
            return get_node(cur_node.r, a)

    a=get_node(root, a)
    b=get_node(root, b)
    a.val, b.val = b.val, a.val

    print("DFS on swapped (broken) tree:")
    dfs_print(root)
    print("\n")
    root = fix(root)
    print("\nDFS on reswapped (fixed) tree:")
    dfs_print(root)
