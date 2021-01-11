from django.test import TestCase

class FirstSomeTest(TestCase):

    def test_some_first_functionality(self):
        self.assertEqual(1, 1)
    
    def test_some_second_functionality(self):
        self.assertTrue(True)
    
    def test_some_third_functionality(self):
        self.assertNotEqual(1, 2)
