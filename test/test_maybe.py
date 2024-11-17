from src.functionalMaybe import FunctionalMaybe as Maybe

from typing import NamedTuple


PRINT = True


class Tst(NamedTuple):
    x: int
    y: str


def logger(val):
    # Just to console
    return print(val) if PRINT else None


def test():
    assert Maybe()\
            .construct(Tst, (1, "one"))\
            .run(logger) \
            .transform(lambda i, s: str(i) + s, True) \
            .run(logger) \
            .get() == "1one"


if __name__ == "__main__":
    test()