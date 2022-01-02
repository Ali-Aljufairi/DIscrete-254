# %% Counter Example for p and q

def p(x: int, y: int) -> bool: return y**3 + y * x ** 2 <= x**3 + x * y**2
def q(x: int, y: int) -> bool: return y <= x


for x in range(100):
    for y in range(100):
        if p(x, y) and q(x, y):
            print('Counter Example: ', x, y)


# %% Counter Example for p and q

def p(x: int, y: int) -> bool: return (y + 3) % (x + 3) == 0
def q(x: int, y: int) -> bool: return y % x == 0


for x in range(1, 100):
    for y in range(1, 100):
        if p(x, y) and not q(x, y):
            print('Counter Example: ', x, y)


# %% Counter Example for p and q

def p(x: int, y: int, z: int) -> bool: return z % (x + y)
def q(x: int, y: int, z: int) -> bool: return z % x
def r(x: int, y: int, z: int) -> bool: return z % y


for x in range(1, 100):
    for y in range(1, 100):
        for z in range(1, 100):
            if   p(x, y, z) and not (q(x, y, z) and r(x, y, z)):
                print('Counter Example: ', x, y, z)