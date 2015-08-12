# -*- coding: utf-8 -*-
import unittest
import wx

# NoseTest OK/Fail
### Absolute import Y/N                  N               Y
# -------------------------------------------------------------
import ci_setup_check.core as core     # OK              OK
#from .. import core as core            # OK              OK
#from . import core as core             # fail            fail
#from ci_setup_check import core        # OK              OK
#import core                            # fail           fail



class Examples(unittest.TestCase):
    def test_things(self):
        result = core.func(2, 3)
        self.assertEqual(result, 5)

    def test_wx_version(self):
        self.assertEqual(wx.ID_ABORT, 5115)


if __name__ == "__main__":
#    test_stuff()
    unittest.main()
