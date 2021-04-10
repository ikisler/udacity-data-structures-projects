class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def iterate(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    # Your Solution Here
    values = set()

    for node in llist_1.iterate():
        values.add(node.value)

    for node in llist_2.iterate():
        values.add(node.value)

    new_ll = LinkedList()
    for value in values:
        new_ll.append(value)

    return new_ll

def intersection(llist_1, llist_2):
    # Your Solution Here
    set1 = set()
    set2 = set()

    for node in llist_1.iterate():
        set1.add(node.value)

    for node in llist_2.iterate():
        set2.add(node.value)

    final = set1 - (set1 - set2)

    new_ll = LinkedList()
    for value in final:
        new_ll.append(value)
    return new_ll


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
# Returns 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21 -> (ordering may vary)
print (intersection(linked_list_1,linked_list_2))
# Returns 4 -> 6 -> 21 -> (ordering may vary)

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
# Returns 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 -> (ordering may vary)
print (intersection(linked_list_3,linked_list_4))
# Returns an empty LinkedList


# Test case 3 -- None and empties tests
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

linked_list_5.append(None)
linked_list_6.append("")
linked_list_6.append(None)

print(union(linked_list_5, linked_list_6))
# Returns  -> None ->   (ordering may vary; extra "->" shows evidence of empty value)
print(intersection(linked_list_5, linked_list_6))
# Returns  None -> 

# Test case 4 -- Empty LinkedLists
print(union(LinkedList(), LinkedList()))
# Returns nothing
print(intersection(LinkedList(), LinkedList()))
# Returns nothing

