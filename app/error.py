class UnexpectedResultError(Exception):
    """A result was not expected, since there was no other error the reason seems yet to be unknown/handled"""


class UnusableRulebookError(Exception):
    """Set of rulebooks contains at least one unusable."""
