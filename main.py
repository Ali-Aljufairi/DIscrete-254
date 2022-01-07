# %%
# !! Import
from itcs254 import Relations


# %% ----------------------------------------------------------------------------------------------------
# TODO: Solve...


U = {1, 2, 3}
R = {(1, 1), (1, 2)}

print(Relations(U, R).relations())


# %% ----------------------------------------------------------------------------------------------------
# ? Simple example


# Universal set
U = {1, 2, 3}

# Relation set
R = {(1, 1), (1, 2)}


print(Relations(U, R).relations())


# %% ----------------------------------------------------------------------------------------------------
# ? Function example

# Range
min, max = -5, 5

# Universal set
U = set(range(min, max + 1))


# Function
def F(x, y): return x + y == 4


# Relation set
R = {(x, y) for x in U for y in U if F(x, y)}


print(Relations(U, R).relations())


# %% ----------------------------------------------------------------------------------------------------
# ? Multiple Range example

# Range of A
min, max = -5, 5

A = set(range(min, max + 1))


# Range of B
min, max = -5, 5

B = set(range(min, max + 1))


# Function
def F(x, y): return x + y == 4


# Relation set
R = {(x, y) for x in A for y in B if F(x, y) or F(y, x)}


print(Relations(U, R).relations())
