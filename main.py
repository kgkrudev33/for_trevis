import unittest


class PythonSomeTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_assert_true_is_true(self):
        self.assertTrue(True, True)

    def test_assert_upper(self):
        self.assertEqual("TEST", "TEST")

    def test_assert_greater(self):
        self.assertGreater(10, 9)
      
    def test_assert_greater(self):
        self.assertGreater(15, 9)
    
    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
