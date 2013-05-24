"""
blank.py

.. autosummary ::
    blankline
"""

def blankline(line1, line2):
    """
    Print "line1\n\nline2".
    >>> blankline("Hello", "World")
    Hello
    <BLANKLINE>
    World
    """
    print line1
    print ""
    print line2


