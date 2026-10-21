class Node:
    def __init__(self, keyword, description):
        self.keyword = keyword
        self.description = description
        self.left = None
        self.right = None
        self.height = 1