class CustomNode():
    def __init__(self, left_branch=None, right_branch=None, value=1, obj=None):
        self.right_branch = right_branch
        self.left_branch = left_branch
        self.value = value
        self.obj = obj

    def set_obj(self, value):
        self.obj = obj

    def set_value(self, value):
        self.value = value

    def set_right_branch(self, right_branch):
        self.right_branch = right_branch

    def set_left_branch(self, left_branch):
        self.left_branch = left_branch


def huffman(string):
    result_dict = {}

    def get_codes(node, code=''):
        moved_left = False
        if node.obj:
            result_dict[node.obj] = code
            return
        if node.left_branch:
            code += '0'
            moved_left = True
            get_codes(node.left_branch, code)
        if node.right_branch:
            if moved_left:
                code = code[:-1] + '1'
            else:
                code += '1'
            get_codes(node.right_branch, code)

    nodes_list = []
    chars = set(string)

    for char in chars:
        nodes_list.append(CustomNode(value=string.count(char), obj=char))

    nodes_list = sorted(nodes_list, key=lambda x: x.value)

    while len(nodes_list) > 1:
        fst, scnd = nodes_list.pop(0), nodes_list.pop(0)
        nodes_list.append(CustomNode(left_branch=fst, right_branch=scnd, value=fst.value + scnd.value))
        nodes_list = sorted(nodes_list, key=lambda x: x.value)

    get_codes(nodes_list[0])

    new_string = ''
    for i in string:
        new_string += result_dict[i] + ' '

    return result_dict, new_string


result_dict, new_string = huffman("asjdgksjdvoi ahesdifugnh ekarfbiacw bfasgk agfuaw ckmnbgf ouashfdklajshgik sdbvkash nfhbsjkafgsa vbjashbdf asd")

for obj, code in result_dict.items():
    print(f'Символ "{obj}", код {code}')
print(new_string)