
def simple_hash(sbtr):
    letter = 26
    index = 0
    size = 10000

    for i, char in enumerate(sbtr):
        index += (ord(char) - ord('a') + 1) * letter ** i

    return index % size


def get_substr(string):
    len_str = len(string)
    assert len_str > 1, "В строке должно быть более 1 символа."
    res_dict = {}

    for i in range(1, len_str):
        for j in range(len_str - i + 1):
            sbtr = string[j:j + i]
            sbtr_hash = simple_hash(sbtr)
            if sbtr_hash not in res_dict:
                res_dict[sbtr_hash] = sbtr
    return list(res_dict.values())


string = input("Введите строку: ")
print(f"В строке {string} имеются следующие подстроки: {get_substr(string)}")