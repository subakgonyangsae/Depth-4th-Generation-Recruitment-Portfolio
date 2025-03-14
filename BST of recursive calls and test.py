class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_value(self.root, data)

    def _insert_value(self, node, data):
        if data <= node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_value(node.left, data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_value(node.right, data)

    def find(self, key):
        return self._find_value(self.root, key)

    def _find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None
        elif key < root.data:
            return self._find_value(root.left, key)
        else:
            return self._find_value(root.right, key)

    def delete(self, key):
        self.root = self._delete_value(self.root, key)

    def _delete_value(self, node, key):
        if node is None:
            return node

        if key < node.data:
            node.left = self._delete_value(node.left, key)
        elif key > node.data:
            node.right = self._delete_value(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # 삭제할 노드가 두 개의 자식을 가지고 있는 경우
            temp = self._find_min(node.right)
            node.data = temp.data
            node.right = self._delete_value(node.right, temp.data)

        return node

    def _find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.data, end=' ')
        print_inorder(node.right)

if __name__ == "__main__":
    bst = BinarySearchTree()
    data_list = [4, 5, 8, 1, 7, 6, 13]

    for data in data_list:
        bst.insert(data)

    print("이진 탐색 트리에 7 존재 여부:", bst.find(7))
    print("이진 탐색 트리에 4 존재 여부:", bst.find(4))

    print("이진 탐색 트리 삭제 전 Inorder 순회:")
    print_inorder(bst.root)
    print()

    bst.delete(4)
    print("4 삭제 후 Inorder 순회:")
    print_inorder(bst.root)
    print()

    bst.delete(13)
    print("13 삭제 후 Inorder 순회:")
    print_inorder(bst.root)