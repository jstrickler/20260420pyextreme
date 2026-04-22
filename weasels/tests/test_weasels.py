import pytest

from weasels import sample_function
def test_weasels_has_sample_function():
    assert sample_function() is None  # no return value
