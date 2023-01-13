from enum import Enum


class RegelSet(str, Enum):
    DSA5_GRUND = 'DSA5_Grund'
    """
    Beinhaltet Grundlegende Prüfungen wie die Existenz der angegebenen Merkmale oder ob die Merkmals-Kombinationen erlaubt sind.
    """

    DSA5_OPTIONAL = 'DSA5_Optional'
    """
    TBA
    """
