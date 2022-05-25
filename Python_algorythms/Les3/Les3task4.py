# 4. Определить, какое число в массиве встречается чаще всего.

sample_list = [random.randint(0, 15) for _ in range(20)]

res_dict = {}
max_elem, max_count = None, 0

for i in sample_list:
    if i not in res_dict:
        res_dict[i] = 1
    else:
        res_dict[i] += 1
    if res_dict[i] > max_count:
        max_count, max_elem = res_dict[i], i

print(sample_list)
print(res_dict)
print(f'Число {max_elem} встречается {max_count} раза.')