import unittest
import time

import gazerbeam


def factorial(n):
    DELAY = 0.3
    print("factorial(n=%d)" % n)
    time.sleep(DELAY)

    if n <= 1:
        result = 1
    else:
        result = n * factorial(n-1)

    time.sleep(DELAY)
    print("factorial(n=%d) ==> %d" % (n, result))
    return result


@gazerbeam.tracer(factorial)
def factorial_start(n):
    return factorial(n)


class TestGazerbeam(unittest.TestCase):
    def test_factorial(self):
        factorial_start(5)
