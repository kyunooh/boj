all_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}

cmd = "arst"
def function_to_test(n):
    for i in range(n):
        s.add(1)

import timeit
start = timeit.default_timer()

# 여기에 측정할 코드를 넣으세요
function_to_test(30000000)




stop = timeit.default_timer()
print(stop - start)




import timeit
start = timeit.default_timer()


def function_to_test(n):
    for i in range(n):
        if not 1 in s:
            s.add(1)


# 여기에 측정할 코드를 넣으세요
function_to_test(30000000)




stop = timeit.default_timer()
print(stop - start)
