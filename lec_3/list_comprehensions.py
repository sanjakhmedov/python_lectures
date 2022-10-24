# def f(x):
#     return x**3
#
#
# ls = [(i, f(i)) for i in range(1, 21) if i % 2 == 0]
#
# print(ls)


# ls = [1, 2, 3, 5, 8, 15, 23, 38]
# new_ls = [(ls[i], ls[i] ** 2) for i in range(len(ls)) if ls[i] % 2 == 0]
# print(ls)
# print(new_ls)


data = '1 2 3 5 8 15 23 38'.split()

res = map(int, data)
res = filter(lambda x: not x % 2, res)
res = list(map(lambda x: (x, x ** 2), res))
print(res)
