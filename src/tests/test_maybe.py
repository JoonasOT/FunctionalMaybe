import unittest
from src.FunctionalMaybe.functional_maybe import FunctionalMaybe as Maybe

# FIXME: These are dumb

PRINT = False


class Tst:
    def __init__(self, x, y, z=None, w=1):
        self.x = x
        self.y = y
        self.z = z
        self.w = w

    def __str__(self):
        return f"{self.x}, {self.y}, {self.z}, {self.w}"


def logger(val):
    # Just to console
    return print(val) if PRINT else None


TEST_PARAMS = (1, "one")


def constructTestMaybe():
    return Maybe().construct(Tst, *TEST_PARAMS, w=4)


class TestMaybe(unittest.TestCase):
    def testConstructor(self):
        got = str(constructTestMaybe().unwrap())
        expected = str(Tst(*TEST_PARAMS, w=4))
        self.assertEqual(expected, got)

    def testTransform(self):
        got = str(constructTestMaybe().transform(lambda tst: str(tst.x) + " " + tst.y).unwrap())
        expected = str((lambda i, s: str(i) + " " + s)(*TEST_PARAMS))
        self.assertEqual(expected, got)

    def testTransformers(self):
        toTup = lambda tst: (tst.x, tst.y)
        toString = lambda tup: str(tup[0]) + tup[1]
        padd = lambda s: s + " ;"

        got = str(constructTestMaybe().transformers(toTup, toString, padd).unwrap())
        expected = padd(toString(TEST_PARAMS))
        self.assertEqual(expected, got)

    def testRun(self):
        got = str(constructTestMaybe().run(lambda _: 1).unwrap())
        expected = str(constructTestMaybe().unwrap())
        self.assertEqual(expected, got)

    def testRunners(self):
        toTup = lambda tst: (tst.x, tst.y)
        toString = lambda tst: str(tst.x) + tst.y
        padd = lambda s: str(s) + " ;"

        got = str(constructTestMaybe().runners(toTup, toString, padd).unwrap())
        expected = str(constructTestMaybe().unwrap())
        self.assertEqual(expected, got)
