from decimal import Decimal

from hypothesis import given
from hypothesis import strategies as st
import pytest

from example_pytest_suite.sorts import merge_sort


class TestSimple:
    def test_merge_empty(self):
        assert merge_sort([]) == []

    def test_merge_one_element(self):
        assert merge_sort([1]) == [1]

    def test_sorts(self):
        original = [4, 3, 2, 1]
        expected = [1, 2, 3, 4]
        assert merge_sort(original) == expected

    def test_new_object(self):
        original = [2, 1]
        # assert that object is different after sorting
        assert merge_sort(original) is not original

    def test_same_object_no_sort(self):
        original = [1]
        # nothing to sort (len == 1), so same object returned
        assert merge_sort(original) is original


class TestHypothesis:
    @pytest.mark.parametrize(
        "strategy",
        [
            st.integers(),
            st.floats(allow_nan=False),
            st.decimals(allow_nan=False),
            st.binary(),
            st.booleans(),
            st.characters(),
        ],
        ids=str,
    )
    @given(data=st.data())
    def test_sort_given_dynamic(self, data: st.DataObject, strategy: st.SearchStrategy):
        drawn: list = data.draw(st.lists(strategy))
        expected = sorted(drawn)
        assert merge_sort(drawn) == expected
