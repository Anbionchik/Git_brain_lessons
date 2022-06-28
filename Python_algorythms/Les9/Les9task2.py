from collections import OrderedDict

class CustomNode():
    def __init__(self, right_branch=None, left_brunch=None, value=1):
        self.right_branch = right_branch
        self.left_branch = left_branch
        self.value = value
    def set_value(self, value):
        self.value = value
    def set_right_branch(self, right_branch):
        self.right_branch = right_branch
    def set_left_branch(self, left_branch):
        self.left_branch = left_branch


def huffman(string):
    char_count_dict = {}
    chars = set(string)

    for char in chars:
        char_count_dict[char] = string.count(char)
    char_count_dict = OrderedDict(sorted(char_count_dict.items(), key=lambda x: x[1]))
    print(char_count_dict.items())

    return char_count_dict