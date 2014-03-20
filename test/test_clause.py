import sys, os
from unittest import main, TestCase

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, root)
from models.clause import Clause

class TestCauseSatisfaction(TestCase):
    def setUp(self):
        self.a = Clause([1,4,5],[1,0,1])

    def test_satisfaction_check(self):
        self.assertTrue(self.a.is_satisfied({1:True,4:False}))
        self.assertFalse(self.a.is_satisfied({1:False,4:True,5:False}))
        #a.show_vars_used()
        print self.a.as_text()

    def test_output_check(self):
        expected = "(X1 ~X4 X5)"
        actual = self.a.as_text()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    main()
