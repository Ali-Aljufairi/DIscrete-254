class Relations:

    def __init__(self, pairs: list[tuple[int, int]], universal: tuple[int] = set()) -> None:
        self.pairs = tuple(pairs)
        self.universal = set(universal)

    def __str__(self) -> str:
        return '[' + ', '.join(f"({pair[0]}, {pair[1]})" for pair in self.pairs) + ']'

    def relations(self) -> str:
        return f"\n{self.universal}\n{self}\n{'-'*20}\n" \
            + '\n'.join(
                f"{s:^13}: {'✔' if t() else '❌'}\n"
                for s, t in {'Reflective': self.is_reflective, 'Symmetric': self.is_symmetric, 'Antisymmetric': self.is_antisymmetric, 'Transitive': self.is_transitive}.items()
            )

    def is_reflective(self) -> bool:
        """Return True if the relation is reflexive, False otherwise."""

        if len(self.pairs) == 0:
            return False

        for s in self.universal:
            for pair in self.pairs:
                if pair == (s, s):
                    break
            else:
                return False

        return True

    def is_symmetric(self) -> bool:
        if len(self.pairs) == 0:
            return True

        s = set()

        for x, y in self.pairs:
            if (y, x) in s:
                return True
            s.add((x, y))

        return all(x == y for x, y in self.pairs)

    def is_antisymmetric(self) -> bool:
        if len(self.pairs) <= 1:
            return True

        s = set()

        for x, y in self.pairs:
            if (y, x) in s:
                return x == y
            s.add((x, y))

        return True

    def is_transitive(self) -> bool:
        if len(self.pairs) <= 1:
            return True

        s = set()

        for x, y in self.pairs:
            s.add((x, y))

            for z in [b for a, b in s if (a == y)]:
                if (x, z) in s:
                    return True

        return False


def transitive(R, A):
    """Returns True if a relation R on set A is transitive, False otherwise."""
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True
