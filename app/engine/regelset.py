from pathlib import Path

from app.resource import get_path
from app.service import RegelSet

clingo_logik: dict[RegelSet, Path] = {
    RegelSet.DSA5_GRUND: get_path('regelwerk/dsa5/grundregeln.lp'),
    RegelSet.DSA5_OPTIONAL: get_path('regelwerk/dsa5/optionale_regeln.lp'),
}
