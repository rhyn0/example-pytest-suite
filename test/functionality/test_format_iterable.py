import pytest
from pytest_insta.fixture import SnapshotFixture

from example_pytest_suite.formats import format_iterable


class TestSimple:
    def test_int_list(self):
        original = [1]
        expected = "\n[\n    1\n]\n"
        assert format_iterable(original) == expected


class TestSnapshot:
    def test_format_float_list(self, snapshot: SnapshotFixture):
        original = [1.0, 2.0, 3.0]
        result = format_iterable(original)
        assert snapshot() == result
