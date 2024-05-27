# Intuition
The problem requires finding the shortest path that visits every node in the graph. Since the graph is undirected and connected, we can explore all possible paths using a breadth-first search (BFS) approach.

# Approach
1. Start BFS from each node in the graph simultaneously.
2. Use memoization to avoid revisiting the same state (node, visited_nodes).
3. Maintain a bitmask to track visited nodes. The target state is when all nodes are visited.
4. Explore neighbors of each node in the graph and enqueue them in the BFS queue with updated states.
5. Repeat BFS until the target state is reached, then return the number of steps taken.

# Complexity
- Time complexity: O(n * 2^n), where n is the number of nodes in the graph. In the worst case, each state (node, visited_nodes) can be visited multiple times, and there are 2^n possible combinations of visited nodes.
- Space complexity: O(2^n) for the memoization set and the BFS queue, where n is the number of nodes in the graph.
