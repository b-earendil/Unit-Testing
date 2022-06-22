#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ben Adams
# Summer 2022
# CSPB 3308
# University of Colorado
# Text Processing Module
# Unit Testing

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    # Add Your Test Cases Here...

    # Write a test to verify the constructor raises an error if passed
    # something other than a string
    def test_ctor(self):
        not_a_string = 124
        with self.assertRaises(Exception):
            p = textproc.Processor(not_a_string)

    # Write one or more unit tests to test the count() method
    def test_count(self):
        text = "66hello5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), len(text), "'text' does not have same length as input")

    # Write one or more unit tests to test the count_alpha() method
    def test_count_alpha(self):
        text = "nope5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "alpha count of 'text' is not 4")
        text = "NOPE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "alpha count of 'text' is not 4")
        text = "5nOpE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "alpha count of 'text' is not 4")
        text = "!@#$%^&*()-+[]{}5nOpE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "alpha count of 'text' is not 4")
        text = "9NOPE"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "alpha count of 'text' is not 4")

    # Write one or more unit tests to test the count_numeric() method
    def test_count_numeric(self):
        text = "5g5g5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "numeric count of 'text' is not 3")
        text = "G55i9y"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "numeric count of 'text' is not 3")
        text = "155"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "numeric count of 'text' is not 3")
        text = "210"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "numeric count of 'text' is not 3")
        text = "-500"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "numeric count of 'text' is not 3")
        text = "0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 10, "numeric count of 'text' is not 3")

    # Write one or more unit tests to test the count_vowels() method
    def test_count_vowels(self):
        text = "hello"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "vowel count of 'text' is not 2")
        text = "aeiou"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5, "vowel count of 'text' is not 5")
        text = "Apple"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "vowel count of 'text' is not 2")
        text = "AEIOU"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5, "vowel count of 'text' is not 5")

    # Write one or more unit tests to test the is_phonenumber() method
    def  test_phone(self):
        text = "(555) 555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "'text' is an invalid phone number")
        text = "555-555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "'text' is an invalid phone number")
        text = "555 555 5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "'text' is an invalid phone number")
        text = "555.555.5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "'text' is an invalid phone number")
        text = "(555) 555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "'text' is an invalid phone number")



# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
