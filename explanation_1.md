### Reasoning
I used the OrderedDict data structure because it provides the same average O(1) operation speed as a regular dictionary, and then could use the ordering features to act like a queue structure -- removing and re-adding an item whenever it is accessed keeps it at the tail of the "queue", so when we run out of cache space, we always remove the first element from the head of the "queue".

### Efficiency
#### Time: O(1)
The `get` and `set` operations have a Big-O time complexity of O(1) on average -- all of the dictionary operations (pop, get, set) of the underlying OrderedDict have the average time complexity of O(1), however these operations may take up to an amortized worst case time of O(n).

#### Space: O(n)
The underlying OrderedDict has to store `m` keys, plus `n` values, plus some overhead for the ordering `o` -- so Big-O(`m` + `n` + `o`), which boils down to O(n).

