# Exer-02-Patching-Objects-in-Unit-Tests

from unittest.mock import patch
import example


@patch("example.func")
def test1(x, mock_func):
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)


###

with patch("example.func") as mock_func:
    example.func(x)  # Uses patched example.func
    mock_func.assert_called_with(x)

###

p = patch("example.func")
mock_func = p.start()
example.func(x)
mock_func.assert_called_with(x)
p.stop()

###

"""
@patch('example.func1')
@patch('example.func2')
@patch('example.func3')
def test1(mock1, mock2, mock3):
    ...
"""

"""
def test2():
    with patch('example.patch1') as mock1, \
         patch('example.patch2') as mock2, \
         patch('example.patch3') as mock3:
    ...
"""

x = 42
with patch("__main__.x"):
    print(x)

###

with patch("__main__.x", "patched_value"):
    print(x)

###

from unittest.mock import MagicMock

m = MagicMock(return_value=10)
m(1, 2, debug=True)
m.assert_called_with(1, 2, debug=True)
m.assert_called_with(1, 2)  # AssertionError

m.upper.return_value = "HELLO"
m.upper("hello")
assert m.upper.called
m.split.return_value = ["hello", "world"]
m.split("hello world")
m.split.assert_called_with("hello world")

m["blah"]
m.__getitem__.called
m.__getitem__.assert_called_with("blah")

###

# example.py
from urllib.request import urlopen
import csv


def dowprices():
    u = urlopen("http://finance.yahoo.com/d/quotes.csv?s=@^DJI&f=sl1")
    lines = (line.decode("utf-8") for line in u)
    rows = (row for row in csv.reader(lines) if len(row) == 2)
    prices = {name: float(price) for name, price in rows}
    return prices


import unittest
from unittest.mock import patch
import io
import example

simple_data = io.BytesIO(
    b"""\
"IBM",91.1\r
"AA",13.25\r
"MSFT",27.72\r
\r
"""
)


class Tests(unittest.TestCase):
    @patch("example.urlopen", return_value=sample_data)
    def test_dowprices(self, mock_urlopen):
        p = example.dowprices()
        self.assertTrue(mock_urlopen.called)
        self.assertEqual(p, {"IBM": 91.1, "AA": 13.25, "MSFT": 27.72})

    if __name__ == "__main__":
        unittest.main()
