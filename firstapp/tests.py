"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from django.test.utils import override_settings

import temp_django.settings


#@override_settings(REALM='xbox')
class SimpleTest(TestCase):


    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.

        """
        with self.settings(NAME='Tim'):
            from temp_django.settings import NAME
            print(NAME)
            self.assertEqual(1 + 1, 2)
