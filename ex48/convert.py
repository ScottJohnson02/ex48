# Exercise 48: convert.py
# NOTE: This should be added to the main package inside a newly created project


def convert_number(s):
    """Convert a string to an integer, '123' to 123, or return None."""
    try:
        return int(s)
    except ValueError:
        return s
