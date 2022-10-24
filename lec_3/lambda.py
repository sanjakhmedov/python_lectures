# def summ(x, y):
#     return x + y





def mult(x, y):
    return x * y


m = mult


def calc(op, a, b):
    print(op(a, b))


calc(lambda x, y: x + y, 42, 78)
