### Reasoning
I used a linked list implementation to connect each block in the chain to the next one in the list, since each block depends on the previous one for its hash.

### Efficiency
#### Time: O(1) (add and get count)
Adding a block to the chain has a worst case complexity of O(1), since the linked list implementation does not depend on having to iterate over the existing nodes, the operation time involved is the same every time.

Getting the count for the number of blocks also has a big O(1), since we are keeping track of the count when we add a block.

The __repr__ method has a complexity of O(n), since we are iterating over all our nodes to create the print out.

#### Space: O(n)
The linked list implementation consumes O(n) space, since the space consumed is directly proportional to the number of blocks in the chain.

