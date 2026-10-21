from data_structures.b_tree_node import BTreeNode

class BTree:
    def __init__(self, t=2):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, k, node=None):
        if node is None:
            node = self.root
        
        i = 0
        while i < len(node.keys) and k > node.keys[i]['token']:
            i += 1
            
        if i < len(node.keys) and node.keys[i]['token'] == k:
            return node.keys[i]
            
        if node.leaf:
            return None
            
        return self.search(k, node.children[i])

    def insert(self, token, location):
        existing = self.search(token)
        if existing:
            if location not in existing['locations']:
                existing['locations'].append(location)
            return

        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.children.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, token, location)
        else:
            self.insert_non_full(root, token, location)

    def insert_non_full(self, node, token, location):
        i = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while i >= 0 and token < node.keys[i]['token']:
                node.keys[i + 1] = node.keys[i]
                i -= 1
            node.keys[i + 1] = {'token': token, 'locations': [location]}
        else:
            while i >= 0 and token < node.keys[i]['token']:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self.split_child(node, i)
                if token > node.keys[i]['token']:
                    i += 1
            self.insert_non_full(node.children[i], token, location)

    def split_child(self, x, i):
        t = self.t
        y = x.children[i]
        z = BTreeNode(y.leaf)
        
        x.children.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        
        z.keys = y.keys[t: (2 * t - 1)]
        y.keys = y.keys[0: t - 1]
        
        if not y.leaf:
            z.children = y.children[t: 2 * t]
            y.children = y.children[0: t - 1]