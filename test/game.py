import unittest


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('capgemini'.upper(), 'CAPGEMINI')