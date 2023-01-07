import unittest
from typing import KeysView
from typing import Type

from pydantic import ValidationError
from pydantic.error_wrappers import get_exc_type


def assert_errors(self: unittest.TestCase,
                  error: ValidationError,
                  fields: KeysView[str],
                  cls: Type[Exception],
                  **msg_data):
    """
    Tests that contained pydantic validation errors are as expected
    :param self: test class reference
    :param error: received pydantic validation error
    :param fields: field with expected errors
    :param cls: expected error class for fields
    :param msg_data: [optional] keyword arguments to pass parameters to format message
    """
    for error in error.errors():
        self.assertIn(error['loc'][0], fields)
        self.assertEqual(error['type'], get_exc_type(cls))
        if msg_data or cls.msg_template:
            msg = cls.msg_template.format(**msg_data) if msg_data else cls.msg_template
            self.assertEqual(error['msg'], msg)
