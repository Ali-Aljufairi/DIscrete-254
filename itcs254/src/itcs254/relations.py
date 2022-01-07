class Relations:

    def __init__(self, universal: set[int] = set(), pairs: set[tuple[int, int]] = set()) -> None:
        self.pairs, self.universal = set(pairs), set(universal)

    def __str__(self) -> str:
        return '[' + ', '.join(f"({pair[0]}, {pair[1]})" for pair in self.pairs) + ']'

    def relations(self) -> str:

        reflective = self.is_reflective()
        symmetric = self.is_symmetric()
        antisymmetric = self.is_antisymmetric()
        transitive = self.is_transitive()

        all = reflective and symmetric and antisymmetric and transitive
        equivalent = reflective and symmetric and transitive
        partial = reflective and antisymmetric and transitive

        return f"\n{self.universal}\n{self}\n" + \
            '\n'.join(
                f"{s:^13}: {'✔' if t else '❌'}" for s, t in (
                    ('-'*20, all),
                    ('Reflective', reflective),
                    ('Symmetric', symmetric),
                    ('Antisymmetric', antisymmetric),
                    ('Transitive', transitive),
                    ('-'*20, equivalent and partial),
                    ('Equivalent', equivalent),
                    ('Partial', partial),
                )
            )

    def is_reflective(self) -> bool:
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

        return all((R[::-1] in self.pairs) for R in self.pairs)

    def is_antisymmetric(self) -> bool:
        if len(self.pairs) <= 1:
            return True

        x = filter(lambda pair: pair[0] == pair[1], self.pairs)

        return any(x) or all((R[::-1] not in self.pairs) for R in x)

        # s = set()

        # for x, y in self.pairs:
        #     if (y, x) in s:
        #         return x == y
        #     s.add((x, y))

        # return True

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

    def is_equivalent(self) -> bool:
        return self.is_reflective() and self.is_symmetric() and self.is_transitive()

    def is_partial(self) -> bool:
        return self.is_reflective() and self.is_antisymmetric() and self.is_transitive()


def transitive(R, A):
    """Returns True if a relation R on set A is transitive, False otherwise."""
    for a in A:
        for b in A:
            if (a, b) in R:
                for c in A:
                    if (b, c) in R and (a, c) not in R:
                        return False
    return True
