### Reasoning
For the union function, I used a set and added all the values from both lists to it since this automatically handles duplicates.

The intersection function also uses sets to take advantage of the handling of duplicates plus the convenience as well as built-in set operators.

### Efficiency
#### Time:
Union function worst case time complexity is O(n), since we iterate over the contents of each list, so O(2(n + l)), which simplifies into O(n).

Intersection function worst case time complexity is O(n), since iterating over both linked lists is O(n), and set subtraction is O(n) (weirdly, using the set intersection function provided by Python is O(n**2) in the worst case, which is why I'm not using it).

#### Space:
Union - O(n), since we save the contents of the lists first as a set, then again as the linked list to return, it's O(2(n + m)), which simplifies to O(n).

Intersection - O(n).  We save the contents of the lists first as sets, it consumes O(2(n+m)), which simplifies to O(n).

