# %%
from itcs254 import Relations


# %%


A = set(range(0, 5))
B = set(range(0, 4))


def F(x, y):
    return x + y == 4


R = ((x, y) for x in A for y in B if F(x, y) or F(y, x))


print(Relations(R, A.union(B)).relations())


# %%

N = 1
X = 40

U = set(range(N, X + 1))


def F(x, y):
    return 4*(x**2)-1 <=y


R = ((x, y) for x in U for y in U if F(x, y) or F(y, x))


print(Relations(R, U).relations())


# %%
N = -5
X = 5

U = set(range(N, X + 1))


def F(a, b):
    return a * b > 0


R = ((x, y) for x in U for y in U if F(x, y) or F(y, x))


print(Relations(R, U).relations())


# %%

U = {1, 2, 3}
R = [(1, 1), (1, 2)]


print(Relations(R, U).relations())
