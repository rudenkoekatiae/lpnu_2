import math

class Node:
    def __init__(self, key, ip, name, distance, color='red'):
        self.key = key
        self.ip = ip
        self.name = name
        self.distance = distance
        self.color = color
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return f"{self.key} ({self.color})"

class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, None, None, None, color='black')
        self.root = self.NIL

    def insert(self, key, ip, name, distance):
        new_node = Node(key, ip, name, distance)
        new_node.left = self.NIL
        new_node.right = self.NIL
        new_node.parent = None

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.key < current.key:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self.fix_insert(new_node)

    def delete(self, ip_key):
        def transplant(u, v):
            if u.parent is None:
                self.root = v
            elif u == u.parent.left:
                u.parent.left = v
            else:
                u.parent.right = v
            v.parent = u.parent

        def minimum(node):
            while node.left != self.NIL:
                node = node.left
            return node

        z = self.search(ip_key)
        if z == self.NIL:
            return False

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            transplant(z, z.left)
        else:
            y = minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 'black':
            self.fix_delete(x)
        return True

    def fix_delete(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.left_rotate(x.parent)
                    s = x.parent.right
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.right.color == 'black':
                        s.left.color = 'black'
                        s.color = 'red'
                        self.right_rotate(s)
                        s = x.parent.right
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.right.color = 'black'
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 'red':
                    s.color = 'black'
                    x.parent.color = 'red'
                    self.right_rotate(x.parent)
                    s = x.parent.left
                if s.left.color == 'black' and s.right.color == 'black':
                    s.color = 'red'
                    x = x.parent
                else:
                    if s.left.color == 'black':
                        s.right.color = 'black'
                        s.color = 'red'
                        self.left_rotate(s)
                        s = x.parent.left
                    s.color = x.parent.color
                    x.parent.color = 'black'
                    s.left.color = 'black'
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def fix_insert(self, k):
        while k != self.root and k.parent.color == 'red':
            if k.parent == k.parent.parent.left:
                u = k.parent.parent.right
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            else:
                u = k.parent.parent.left
                if u.color == 'red':
                    k.parent.color = 'black'
                    u.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
        self.root.color = 'black'

    def search(self, key):
        return self._search_tree(self.root, key)

    def _search_tree(self, node, key):
        if node == self.NIL or key == node.key:
            return node
        if key < node.key:
            return self._search_tree(node.left, key)
        return self._search_tree(node.right, key)

    def print_tree(self, node, indent="", last=True):
        if node != self.NIL:
            print(indent, "└─ " if last else "├─ ", node, sep="")
            indent += "   " if last else "│  "
            self.print_tree(node.left, indent, False)
            self.print_tree(node.right, indent, True)

def calculate_distance(x1, y1, x2, y2):
    return round(math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)) 

def ip_to_key(ip):
    try:
        return int(ip)
    except ValueError:
        raise ValueError(f"Invalid IP format: {ip}. IP must be a numeric value.")

def main():
    tree = RedBlackTree()
    print("Enter your coordinates (x y):")
    try:
        x0, y0 = map(int, input().split())
    except ValueError:
        print("Invalid coordinates entered. Please enter two integers.")
        return

    initial_objects = [
        ("Lviv Polytechnic", "15225", 20, 638),
        ("Saint Luke Hospital", "19212", -562, 475),
        ("Stryiskyi Park", "43620", 321, 861),
        ("Ivan Franko Park", "12345", 10, 350),
        ("Market Square", "54321", 250, 700),
        ("Lviv Opera House", "67890", 500, 920),
        ("Lviv City Hall", "11223", 350, 650),
        ("Shevchenko Grove", "44556", -100, 500),
        ("Lviv Art Gallery", "77889", 180, 800),
        ("High Castle Park", "98765", 800, 1000),
        ("Lviv Train Station", "13579", 450, 550),
        ("Pidzamche", "24680", -200, 400),
        ("Museum of Folk Architecture", "54310", 100, 450),
        ("Lychakiv Cemetery", "67801", 150, 750),
        ("King Cross Leopolis", "11234", 1200, 950)
    ]

    for name, ip, x, y in initial_objects:
        try:
            dist = calculate_distance(x0, y0, x, y)
            key = ip_to_key(ip)
            tree.insert(key, ip, name, dist)
        except ValueError as e:
            print(e)

    while True:
        print("\nChoose an option:")
        print("1. Add object")
        print("2. Delete object")
        print("3. Search by IP")
        print("4. Show red-black tree")
        print("5. Exit")
        choice = input("Your choice: ")

        if choice == '1':
            print("Enter object name, IP (5 digits), and coordinates (x y):")
            try:
                parts = input().split()
                name = " ".join(parts[:-3])
                ip = parts[-3]
                x, y = map(int, parts[-2:])
                dist = calculate_distance(x0, y0, x, y)
                key = ip_to_key(ip)
                tree.insert(key, ip, name, dist)
                print("Object added.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '2':
            print("Enter IP ' of the object to delete (5 digits):")
            ip = input()
            key = ip_to_key(ip)
            if tree.delete(key):
                print("Object deleted.")
            else:
                print("Object not found.")

        elif choice == '3':
            print("Enter IP to search (5 digits):")
            ip = input()
            key = ip_to_key(ip)
            node = tree.search(key)
            if node and node != tree.NIL:
                print(f"{node.name}. Distance: {node.distance}. IP: {node.ip}")
            else:
                print("Object not found.")

        elif choice == '4':
            print("\nRed-black tree:")
            tree.print_tree(tree.root)

        elif choice == '5':
            break
        else:
            print("Invalid choice.")
  
if __name__ == "__main__":
    main()