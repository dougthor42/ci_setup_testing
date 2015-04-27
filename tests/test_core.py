from __future__ import print_function, division
from __future__ import absolute_import
import unittest


#def test_stuff():
#    assert 0 == 0
#    assert 1 == 1


class Examples(unittest.TestCase):
    def test_things(self):
        self.assertEqual(5, 5)


if __name__ == "__main__":
#    test_stuff()
    unittest.main()
