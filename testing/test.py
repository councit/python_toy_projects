import unittest
from main import do_stuff


class TestMain(unittest.TestCase):
    def test_do_stuff(self):
        test_param = 10
        result = do_stuff(test_param)
        self.assertEqual(result, 15)


unittest.main()
