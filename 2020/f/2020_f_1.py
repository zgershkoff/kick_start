from collections import deque

def solver(limit, amounts):
    i = 1
    pairs = []
    for a in amounts:
        pairs.append((a // limit, i))
        i += 1
    pairs.sort()

    output = " ".join([str(person) for _, person in pairs])
    return output


num_cases = int(input())

for case in range(num_cases):
    people, limit = map(int, input().split(' '))
    amounts = map(int, input().split(' '))
    print("Case #" + str(case + 1) + ":", solver(limit, amounts))


# 2
# 3 3
# 2 7 4
# 5 6
# 9 10 4 7 2
