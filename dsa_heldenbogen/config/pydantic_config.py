# u.s. Code is angelehnt an die Lösung von Erlend vollset (https://github.com/erlendvollset)
# Quelle: https://github.com/pydantic/pydantic/issues/1098#issuecomment-1009762620
# aufgerufen am 06.01.2023

from typing import Any

import pydantic.errors
import pydantic.types
import pydantic.validators


def _strict_bool_validator(v: Any) -> bool:
    if v is True or v is False:
        return v
    raise pydantic.errors.BoolError()


def _get_validators__():
    yield pydantic.validators.strict_int_validator
    yield pydantic.validators.number_size_validator
    yield pydantic.validators.number_multiple_validator


def activate_strict_mode() -> None:
    """
    Replace default non-strict pydantic validator with strict one.
    Also does bad 'monky patching' with convenient constraint types.
    """
    for i, (type_, _) in enumerate(pydantic.validators._VALIDATORS):
        if type_ == str:
            pydantic.validators._VALIDATORS[i][1][0] = pydantic.validators.strict_str_validator
        if type_ == bytes:
            pydantic.validators._VALIDATORS[i][1][0] = pydantic.validators.strict_bytes_validator
        if type_ == bool:
            pydantic.validators._VALIDATORS[i][1][0] = _strict_bool_validator
        if type_ == int:
            pydantic.validators._VALIDATORS[i][1][0] = pydantic.validators.strict_int_validator
        if type_ == float:
            pydantic.validators._VALIDATORS[i][1][0] = pydantic.validators.strict_float_validator

    # ConstrainedBytes
    # ConstrainedDate
    # ConstrainedDecimal
    # ConstrainedFloat
    # ConstrainedFrozenSet
    pydantic.types.ConstrainedInt.__get_validators__ = _get_validators__
    # ConstrainedList
    # ConstrainedNumberMeta
    # ConstrainedSet
    # ConstrainedStr
