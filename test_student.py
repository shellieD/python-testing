import unittest
from student import Student
from datetime import timedelta


class TestStudent(unittest.TestCase):

    # To set up a class once at the beginning of the test
    # and destroy it at the end of the tests use the class methods
    # setUpClass and tearDownClassb as shown below.

    # @classmethod
    # def setUpClass(cls):
    #     print('setUpClass')

    # @classmethod
    # def tearDownClass(cls):
    #     print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    def test_full_name(self):
        self.assertEqual(self.student.full_name, 'John Doe')

    def test_alert_santa(self):
        self.student.alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_email(self):
        self.assertEqual(self.student.email_address, 'john.doe@email.com')

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))


if __name__ == '__main__':
    unittest.main()
