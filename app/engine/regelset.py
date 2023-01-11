from enum import Enum

from app.engine.resource import get_abs_path


class RegelSet(str, Enum):
    DSA5_GRUND = get_abs_path('regelwerk/dsa5/grundregeln.lp')
    DSA5_OPTIONAL = get_abs_path('regelwerk/dsa5/optionale_regeln.lp')
