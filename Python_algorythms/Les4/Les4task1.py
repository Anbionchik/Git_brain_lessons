# 4. Определить, какое число в массиве встречается чаще всего.
# Наиболее предпочтителен Var1
# 	    Var1		                    Var2		                    Var3
# n	    timeit 	    cProfile	        timeit 	    cProfile	        timeit 	    cProfile
# 100	106 usec	532 function calls	656 usec	537 function calls	424 usec	790 function calls
# 200	213 usec	1054 function calls	2.38 msec	1065 function calls	1.51 msec	1464 function calls
# 1000	1.07 msec	5296 function calls	62.1 msec	5337 function calls	34.3 msec	7670 function calls


#Var 1

import random
import cProfile

def most_frequent(n):
    test_list = [random.randint(-99, 99) for i in range(n)]

    res_dict = {}
    max_elem, max_count = None, 0

    for i in test_list:
        if i not in res_dict:
            res_dict[i] = 1
        else:
            res_dict[i] += 1
        if res_dict[i] > max_count:
            max_count, max_elem = res_dict[i], i


#Var2
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

#Var3
import random
import cProfile

def most_frequent(n):

    test_list = [random.randint(-99, 99) for i in range(n)]
    max_num = 0

    for i in test_list:
        if test_list.count(max_num) < test_list.count(i):
            max_num = test_list.index(i)
