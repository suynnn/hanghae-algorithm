class Node:
    def __init__(self, item=0):
        self.key = item
        self.left, self.right = None, None


root = Node()


def insert(root, key):
    if (root == None):
        root = Node(key)
        return root

    if (key < root.key):
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    return root


def treeinsert(data, root):
    for key in data:
        root = insert(root, key)


def inorderRec(root, answer):
    if (root != None):
        inorderRec(root.left, answer)
        answer.append(root.key)
        inorderRec(root.right, answer)


sample = [3, 0, 1, 8, 7, 2, 5, 4, 6, 9]
answer = []

treeinsert(sample, root)
inorderRec(root, answer)
print(answer[1:])