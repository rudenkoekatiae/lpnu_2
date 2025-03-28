class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @staticmethod
    def build_tree_from_file(filename):
        try:
            with open(filename, "r") as file:
                levels = [line.strip().replace(",", "").split() for line in file.readlines()]
            
            if not levels or all(not level for level in levels):  
                raise ValueError("Error. File is empty")

            root = BinaryTree(int(levels[0][0]))
            queue = [root]
            index = 1

            while index < len(levels):
                next_level = levels[index]
                new_nodes = []
                for parent in queue:
                    if next_level:
                        left_val = next_level.pop(0)
                        if left_val != "None":
                            parent.left = BinaryTree(int(left_val))
                            new_nodes.append(parent.left)
                    
                    if next_level:
                        right_val = next_level.pop(0)
                        if right_val != "None":
                            parent.right = BinaryTree(int(right_val))
                            new_nodes.append(parent.right)

                queue = new_nodes
                index += 1
            
            return root
        
        except FileNotFoundError:
            raise FileNotFoundError(f"Error'{filename}' not found.")
        except ValueError as e:
            raise ValueError(f"Error in the file '{filename}': {e}")

    @staticmethod
    def tree_diam(root):
        if not root:
            return 0
        
        stack = [(root, None)]
        parent_map = {}
        depths = {}
        max_diameter = 0
        
        while stack:
            node, parent = stack.pop()
            if node:
                parent_map[node] = parent
                stack.append((node.left, node))
                stack.append((node.right, node))
        
        nodes = list(parent_map.keys())[::-1]
        
        for node in nodes:
            left_depth = depths.get(node.left, 0)
            right_depth = depths.get(node.right, 0)
            depths[node] = max(left_depth, right_depth) + 1
            max_diameter = max(max_diameter, left_depth + right_depth)
        
        return max_diameter
    
if __name__ == "__main__":
    try:
        root = BinaryTree.build_tree_from_file("tree.txt")
        tree_diameter = BinaryTree.tree_diam(root)
        print(f"Max diameter of the tree equals {tree_diameter}")
    except Exception as e:
        print(e)