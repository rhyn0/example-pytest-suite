from collections.abc import Iterable
from textwrap import dedent


def format_iterable[T](value: Iterable[T]) -> str:
    """Format a sequence of values into our preferred format.

    Generic:
        T - contents of the input Iterable

    Args:
        value (Iterable[T]): Container of values to format into string

    Returns:
        str: Opionated format string
    """
    contents = ",\n".join(str(x) for x in value)
    return dedent(f"""
        [
            {contents}
        ]
    """)
