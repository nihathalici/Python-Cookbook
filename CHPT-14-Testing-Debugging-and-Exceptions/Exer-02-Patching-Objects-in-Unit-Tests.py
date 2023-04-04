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
