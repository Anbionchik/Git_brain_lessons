# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9. Примечание: 8 разных ответов.

res_dict = {x : 0 for x in range(2, 10)}

for i in range(2, 100):
    for dev, summ in res_dict.items():
        if not i % dev:
            res_dict[dev] += 1
print(res_dict)

