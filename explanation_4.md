### Reasoning
The structure given in the Group class is a tree, where each node may have leaves that are users, or child trees that are groups.  I used a Breadth First Search (BFS) because in this case the user may be at any level, and if they happen to be at a higher level, we will find them faster compared to a Depth First Search (DFS).

### Efficiency
#### Time: O(n)
The complexity in the worst case is O(n), because we will need to parse the entire tree of groups.

#### Space: O(n)
The space consumed at worst will be O(n), since we have to maintain a queue structure for our search which may contain up to n-1 groups.

