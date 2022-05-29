# 4. Определить, какое число в массиве встречается чаще всего.
import random
import cProfile

def most_frequent(n):

    test_list = [random.randint(-99, 99) for i in range(n)]
    N = len(test_list)
    num = test_list[0]
    max_score = 1
    for i in range(N-1):
        score = 1
        for j in range(i+1, N):
            if test_list[i] == test_list[j]:
                score += 1
        if score > max_score:
            max_score = score
            num = test_list[i]

# cProfile.run('most_frequent(1000)')