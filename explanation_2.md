### Reasoning
I used a list to store the found file paths, since at the outset, we do not know the number of file paths to be found.  Recursion was used to step down into each directory to continue the search.

### Efficiency
#### Time: O(n)
Appending paths onto a list object has Big-O complexity of O(1), while the process of iterating over the files / directories has a complexity of O(n), making the final complexity O(n).

#### Space: O(n)
Space complexity is O(n), where `n` is the number of file paths found -- while we use some additional variables for each file we are checking, this remains the same for each file, so does not add to our space required.

