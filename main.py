import unittest


class PythonSomeTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_assert_true_is_true(self):
        self.assertTrue(True, True)

    def test_assert_upper(self):
<<<<<<< HEAD
        self.assertEqual("TEST123", "TEST")
=======
        self.assertEqual("TEST", "TEST")
>>>>>>> 8daf9de73fa4a72ad673f5b52997f124a5a797c8

    def test_assert_greater(self):
        self.assertGreater(10, 20)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main()
