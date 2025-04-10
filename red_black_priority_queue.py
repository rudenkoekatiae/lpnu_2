from collections import deque

class Node:
    def __init__(self, value, priority, color=""):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

class BanderaPriorityTree:
    def __init__(self):
        self.nil = Node(None, None, "black")
        self.nil.left = self.nil.right = self.nil.parent = self.nil
        self.root = self.nil

    def insert(self, value, priority):
        node = Node(value, priority, "red")
        node.left = node.right = node.parent = self.nil
        self.insert_node(node)
        self.fix_after_insert(node)

    def insert_node(self, node):
        parent = self.nil
        current = self.root
        while current != self.nil:
            parent = current
            if node.priority > current.priority:
                current = current.left
            else:
                current = current.right
        node.parent = parent
        if parent == self.nil:
            self.root = node
        elif node.priority > parent.priority:
            parent.left = node
        else:
            parent.right = node

    def fix_after_insert(self, node):
        while node.parent.color == "red":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotate_left(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_right(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == "red":
                    node.parent.color = "black"
                    uncle.color = "black"
                    node.parent.parent.color = "red"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotate_right(node)
                    node.parent.color = "black"
                    node.parent.parent.color = "red"
                    self.rotate_left(node.parent.parent)
        self.root.color = "black"

    def rotate_left(self, node):
        child = node.right
        node.right = child.left
        if child.left != self.nil:
            child.left.parent = node
        child.parent = node.parent
        if node.parent == self.nil:
            self.root = child
        elif node == node.parent.left:
            node.parent.left = child
        else:
            node.parent.right = child
        child.left = node
        node.parent = child

    def rotate_right(self, node):
        child = node.left
        node.left = child.right
        if child.right != self.nil:
            child.right.parent = node
        child.parent = node.parent
        if node.parent == self.nil:
            self.root = child
        elif node == node.parent.right:
            node.parent.right = child
        else:
            node.parent.left = child
        child.right = node
        node.parent = child

    def peek(self):
        node = self.get_max(self.root)
        if node != self.nil:
            return node.value, node.priority
        return None

    def extract(self):
        node = self.get_max(self.root)
        if node == self.nil:
            return None
        value, priority = node.value, node.priority
        self.delete_node(node)
        return value, priority

    def get_max(self, node):
        while node != self.nil and node.left != self.nil:
            node = node.left
        return node

    def replace(self, old_node, new_node):
        if old_node.parent == self.nil:
            self.root = new_node
        elif old_node == old_node.parent.left:
            old_node.parent.left = new_node
        else:
            old_node.parent.right = new_node
        new_node.parent = old_node.parent

    def delete_node(self, node):
        original_color = node.color
        if node.left == self.nil:
            replacement = node.right
            self.replace(node, node.right)
        elif node.right == self.nil:
            replacement = node.left
            self.replace(node, node.left)
        else:
            successor = self.get_max(node.right)
            original_color = successor.color
            replacement = successor.right
            if replacement != self.nil:
                replacement.parent = successor
            if successor.parent != node:
                self.replace(successor, successor.right)
                successor.right = node.right
                successor.right.parent = successor
            self.replace(node, successor)
            successor.left = node.left
            successor.left.parent = successor
            successor.color = node.color
        if original_color == "black":
            self.fix_after_delete(replacement)

    def fix_after_delete(self, node):
        while node != self.root and node.color == "black":
            if node == node.parent.left:
                sibling = node.parent.right
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotate_left(node.parent)
                    sibling = node.parent.right
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.right.color == "black":
                        sibling.left.color = "black"
                        sibling.color = "red"
                        self.rotate_right(sibling)
                        sibling = node.parent.right
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.right.color = "black"
                    self.rotate_left(node.parent)
                    node = self.root
            else:
                sibling = node.parent.left
                if sibling.color == "red":
                    sibling.color = "black"
                    node.parent.color = "red"
                    self.rotate_right(node.parent)
                    sibling = node.parent.left
                if sibling.left.color == "black" and sibling.right.color == "black":
                    sibling.color = "red"
                    node = node.parent
                else:
                    if sibling.left.color == "black":
                        sibling.right.color = "black"
                        sibling.color = "red"
                        self.rotate_left(sibling)
                        sibling = node.parent.left
                    sibling.color = node.parent.color
                    node.parent.color = "black"
                    sibling.left.color = "black"
                    self.rotate_right(node.parent)
                    node = self.root
        node.color = "black"

    def print_tree(self, node=None, indent="", last=True):
        if node is None:
            node = self.root
        if node == self.nil:
            return
        print(indent, end="")
        if last:
            print("└─ ", end="")
            indent += "   "
        else:
            print("├─ ", end="")
            indent += "│  "
        color = "R" if node.color == "red" else "B"
        print(f"[{node.priority} | {node.value}] ({color})")
        self.print_tree(node.left, indent, False)
        self.print_tree(node.right, indent, True)

    def bfs(self):
        if self.root == self.nil:
            return []
        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append((node.value, node.priority, node.color))
            if node.left != self.nil:
                queue.append(node.left)
            if node.right != self.nil:
                queue.append(node.right)
        return result

def test_bandera_priority_tree():
    tree = BanderaPriorityTree()

    def insert_and_show(value, priority):
        print(f"\nInserting '{value}' with priority {priority}:")
        tree.insert(value, priority)
        tree.print_tree()

    def extract_and_show():
        item = tree.extract()
        print(f"\nExtracted: {item}")
        tree.print_tree()
        return item

    insert_and_show("task1", 5)
    insert_and_show("task2", 3)
    insert_and_show("task3", 8)
    insert_and_show("task4", 10)

    print("\nCurrent task:", tree.peek())

    extract_and_show()

    print("\task after extraction:", tree.peek())

    insert_and_show("task5", 7)

    print("\nExtracting all elements:")
    while True:
        item = extract_and_show()
        if item is None:
            break

test_bandera_priority_tree()