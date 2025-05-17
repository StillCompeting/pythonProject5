import unittest
from io import StringIO
import sys

from main import print_hi


class TestPrintHi(unittest.TestCase):
    def test_returns_message(self):
        captured = StringIO()
        original = sys.stdout
        try:
            sys.stdout = captured
            message = print_hi("Tester")
        finally:
            sys.stdout = original
        self.assertEqual(message, "Hi, Tester")
        self.assertEqual(captured.getvalue().strip(), "Hi, Tester")

    def test_type_error(self):
        with self.assertRaises(TypeError):
            print_hi(123)


if __name__ == "__main__":
    unittest.main()
