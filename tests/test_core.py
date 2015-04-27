from __future__ import print_function, division
from __future__ import absolute_import
import unittest


class Tests(unittest.TestCase):
    """ Example Tests """

    def test_stuff(self):
        self.assertEqual(0, 0)
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main(verbosity=1)
