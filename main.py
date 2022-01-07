# %%
from itcs254 import Relations


# %%
from itcs254 import Relations
U = {1, 2}
R = [(1, 1), (1, 2)]


print(Relations(R, U).relations())


# %%

U = {1, 6, 3, 9}
def F(a, b): return a + b <= 10 and any((a + b) % x ** 2 == 0 for x in U)


r = Relations(((a, b) for a in U for b in U if F(a, b) or F(b, a)), U)

print(r.relations())


# %%

N = -5
X = 5

U = set(range(N, X + 1))


def F(a, b):
    return (a * b) == 0


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
