import random

import pytest
from pytest_benchmark.fixture import BenchmarkFixture

from example_pytest_suite.sorts import merge_sort


@pytest.fixture
def shuffled_ints() -> list[int]:
    """Fixture of a randomly shuffled list of 1000 numbers."""
    original = list(range(1000))
    random.shuffle(original)
    return original


class TestBenchmark:
    def test_merge_sort(self, benchmark: BenchmarkFixture, shuffled_ints: list[int]):
        expected = sorted(shuffled_ints)
        result = benchmark(merge_sort, shuffled_ints)

        assert result == expected
