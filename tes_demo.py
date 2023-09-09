import unittest
import demo

class TestDemo(unittest.TestCase):
    def test_add(self):
        self.assertEqual(demo.add(2, 3),5)


