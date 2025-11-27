class Solution {
public:
    unordered_map<Node*, Node*> visited;

    Node* cloneGraph(Node* node) {
        if (!node) return nullptr;                               // base case

        if (visited.count(node))                                 // already cloned?
            return visited[node];

        Node* clone = new Node(node->val);                       // clone node
        visited[node] = clone;                                   // mark as visited
        
        for (Node* nei : node->neighbors)                        // clone neighbors
            clone->neighbors.push_back(cloneGraph(nei));

        return clone;                                            // return clone root
    }
};
