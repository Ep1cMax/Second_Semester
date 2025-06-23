import sys
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree():
    lines = []
    while True:
        line = sys.stdin.readline().strip()
        if line == '-':
            break
        if line:
            lines.append(line)

    if not lines:
        return None

    n = int(lines[0])
    nodes = {}

    for line in lines[1:n + 1]:
        parts = line.split()
        node_id = int(parts[0])
        value = int(parts[1])
        nodes[node_id] = TreeNode(value)

    for line in lines[1:n + 1]:
        parts = line.split()
        node_id = int(parts[0])
        left_id = int(parts[2]) if parts[2] != 'None' else None
        right_id = int(parts[3]) if parts[3] != 'None' else None

        if left_id is not None:
            nodes[node_id].left = nodes[left_id]
        if right_id is not None:
            nodes[node_id].right = nodes[right_id]

    return nodes.get(0)

def maxDepth(root):
    if not root:
        return 0

    queue = deque([(root, 1)])
    max_depth = 0

    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)

        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))

    return max_depth

root = buildTree()
print(maxDepth(root))

'''
12
0 5 1 2
1 3 3 4
2 8 5 6
3 1 None None
4 4 None None
5 6 None None
6 9 None 7
7 19 None 8
8 138 9 10
9 130 None None
10 140 11 None
11 139 None None
-
7
'''