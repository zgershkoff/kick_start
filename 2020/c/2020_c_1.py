def solver(nums_list, k):
    countdowns = 0
    counting = 1
    prev = next(nums_list)
    for n in nums_list:
        if n == prev - 1:
            counting += 1
            if counting >= k and n == 1:
                countdowns += 1
        else:
            counting = 1
        prev = n
    return countdowns

num_cases = int(input())

for case in range(num_cases):
    n, k = map(int, input().split(' '))
    l = map(int, input().split(' '))
    # print(f"Case #{case+1}: {solver(l, k)}")
    # This works on my machine, but Google's intepreter
    # doesn't like f strings. Must be Python3.5
    print("Case #{}: {}".format(case+1, solver(l, k)))
