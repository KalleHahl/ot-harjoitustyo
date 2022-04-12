import unittest
from ui.register import Register


class TestRekisteroidy(unittest.TestCase):


    def setUp(self):
        self.register = Register()

    def test_constructor_working(self):
        self.assertEqual(self.register._frame, None)


