### Reasoning

### Efficiency
#### Time: O(n)
The encoding process takes O(n log n) in the worst case, because we have to iterate over each character in the string(O(n)), and add each node to the min heap (O(log n)).

The decoding process takes O(n) time, since we only have to iterate over the characters in the encoded string.

#### Space:
The encoding process takes up O(n) space because we must store each character of the string.

Decoding consumes O(n) because we have to iterate over each character of the encoded string.

