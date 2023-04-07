# Exer-04-Logging-Test-Output-to-a-File

import unittest


class MyTest(unittest.TestCase):
    ...


if __name__ == "__main__":
    unittest.main()

###

import sys


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == "__main__":
    with open("testing.out", "w") as f:
        main(f)
