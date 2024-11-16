from collections.abc import Sequence
from typing import Protocol
from typing import TypeVar


class Comparable(Protocol):
    """Simplest implementation necessary to do sorting with.

    If an object implements this protocol, we can use further on.
    """

    def __lt__(self, other: "Comparable") -> bool:
        """Return whether this is less than `other`."""


ComparableT = TypeVar("ComparableT", bound=Comparable)


def merge_sort(arr: Sequence[ComparableT]) -> Sequence[ComparableT]:
    """Sort the given array using merge sort algorithm.

    Args:
        arr (Sequence[ComparableT]): Array to sort

    Returns:
        Sequence[ComparableT]: sorted array
    """
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return _merge(left_half, right_half)


def _merge(
    left: Sequence[ComparableT],
    right: Sequence[ComparableT],
) -> Sequence[ComparableT]:
    result = []
    i = j = 0

    # Merge while comparing elements from both halves
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Append remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result
