# Exer-03-Testing-for-Exceptional-Conditions-in-Unit-Tests

import unittest

# A simple function to illustrate
def parse_int(s):
    return int(s)


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaises(ValueError, parse_int, "N/A")


###

import errno


class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open("/file/not/found")
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail("IOError not raised")


###


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int("N/A")
        except ValueError as e:
            self.assertEqual(type(e), ValueError)


###


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int("N/A")
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
        else:
            self.fail("ValueError not raised")


###


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, "invalid literal .*", parse_int, "N/A")


###


class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        with self.assertRaisesRegex(ValueError, "invalid literal .*"):
            r = parse_int("N/A")
