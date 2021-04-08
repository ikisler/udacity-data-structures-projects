import sys, heapq

class Node:
    def __init__(self):
        self.char = ""
        self.count = 0
        self.left = None
        self.right = None
        self.visited = False

    def __lt__(self, otherNode):
        return self.count < otherNode.count

def huffman_encoding(data):
    # Edge case!  When the string is empty, then just return "" and None
    if data == "":
        return "", None

    chars_to_count = {}
    nodes = []
    for char in data:
        if chars_to_count.get(char) is None:
            chars_to_count[char] = 1
        else:
            chars_to_count[char] = chars_to_count[char] + 1

    for char, count in chars_to_count.items():
        node = Node()
        node.char = char
        node.count = count
        heapq.heappush(nodes, node)

    # Edge case!  If the whole string is just one character, manually create a parent for it and return
    if len(nodes) == 1:
        parent = Node()
        parent.left = nodes[0]
        return "0" * node.count, parent

    while len(nodes) > 1:
        node1 = heapq.heappop(nodes)
        node2 = heapq.heappop(nodes)

        parent = Node()
        parent.count = node1.count + node2.count
        parent.left = node1
        parent.right = node2

        heapq.heappush(nodes, parent)

    root = heapq.heappop(nodes)
    char_to_encoding = {}
    encoded_string = ""

    get_encodings(root, char_to_encoding)

    for char in data:
        encoded_string += char_to_encoding[char]

    return (encoded_string, root)

def get_encodings(node, encodings_map, current_encoding = ""):
    if node.left is not None:
        get_encodings(node.left, encodings_map, current_encoding + "0")

    if node.right is not None:
        get_encodings(node.right, encodings_map, current_encoding + "1")

    if node.right is None and node.left is None:
        encodings_map[node.char] = current_encoding

def huffman_decoding(data, root):
    decoded_string = ""
    current_node = root

    for char in data:
        if char == "0":
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.left is None and current_node.right is None:
            # Found our character, so go back to the root
            decoded_string += current_node.char
            current_node = root

    return decoded_string

if __name__ == "__main__":
    # Basic functionality, provided tests:
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the decoded data is: {}\n".format(decoded_data))

    # Empty string
    encoded_data, tree = huffman_encoding("")
    print (encoded_data)
    # Returns "" (empty string)
    decoded_data = huffman_decoding(encoded_data, tree)
    print (decoded_data)
    # Returns "" (empty string)

    # String contains only one character (repeating or not, doesn't matter)
    encoded_data, tree = huffman_encoding("aaaa")
    print (encoded_data)
    # Returns "0"
    decoded_data = huffman_decoding(encoded_data, tree)
    print (decoded_data)
    # Returns "aaaa" 

