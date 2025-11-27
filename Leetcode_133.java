class Solution {
    private HashMap<Node, Node> visited = new HashMap<>();

    public Node cloneGraph(Node node) {
        if (node == null) return null;                         // base case

        if (visited.containsKey(node))                         // already cloned?
            return visited.get(node);

        Node clone = new Node(node.val, new ArrayList<>());    // clone node
        visited.put(node, clone);                              // mark as visited

        for (Node nei : node.neighbors)                        // clone neighbors
            clone.neighbors.add(cloneGraph(nei));

        return clone;                                           // return clone root
    }
}
