import json
from typing import Any
from typing import Optional
from typing import Type

from sqlalchemy import Dialect
from sqlalchemy import Text
from sqlalchemy import TypeDecorator
from sqlalchemy.sql.type_api import _T

SIZE = 256


class JsonType(TypeDecorator):

    @property
    def python_type(self) -> Type[Any]:
        pass

    impl = Text(SIZE)

    def process_literal_param(self, value: Optional[_T], dialect: Dialect) -> str:
        pass

    def process_bind_param(self, value, dialect):
        if value is not None:
            value = json.dumps(value)

        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value = json.loads(value)
        return value
