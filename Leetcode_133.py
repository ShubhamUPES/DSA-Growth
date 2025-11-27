class Solution:
    def __init__(self):
        self.visited = {}                     # original -> clone mapping

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None                       # base case

        if node in self.visited:
            return self.visited[node]         # already cloned

        clone = Node(node.val, [])            # create clone
        self.visited[node] = clone            # mark visited

        for nei in node.neighbors:            # clone neighbors
            clone.neighbors.append(self.cloneGraph(nei))

        return clone                          # return cloned root
