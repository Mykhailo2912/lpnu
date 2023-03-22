def Print(_a, _b):
    print(_a, "+", _b)


nums = [1, 2, 3, 4, 5, 5, 6, 7]

for a in nums:
    for b in nums:
        if a + b == 10:
            print(a, b)
