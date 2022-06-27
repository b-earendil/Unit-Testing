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
        test_str = "test_init: ctor 'text' attribute does not match input"
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "Failed : " + test_str)

    # Add Your Test Cases Here...

    # Write a test to verify the constructor raises an error if passed
    # something other than a string
    def test_ctor(self):
        not_a_string = 124
        with self.assertRaises(Exception):
            p = textproc.Processor(not_a_string)

    # Write one or more unit tests to test the count() method
    def test_count(self):
        test_str = "test_count: empty string"
        text = ""
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 0, "Failed: " + test_str)

        test_str = "test_count: single digit"
        text = "6"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 1, "Failed " + test_str)

        test_str = "test_count: multiple digits"
        text = "123"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 3, "Failed " + test_str)

        test_str = "test_count: single lower-case alpha"
        text = "a"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 1, "Failed " + test_str)

        test_str = "test_count: multiple lower-case"
        text = "hey"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 3, "Failed " + test_str)

        test_str = "test_count: single upper-case alpha"
        text = "Z"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 1, "Failed " + test_str)

        test_str = "test_count: multiple upper-case"
        text = "HELLO"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 5, "Failed " + test_str)

        test_str = "test_count: begin single digit, end multiple lower-case"
        text = "6hello"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin multiple lower-case, end single digit"
        text = "hello5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin single digit, multiple lower-case, end single digit"
        text = "6hello5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 7, "Failed " + test_str)

        test_str = "test_count: begin single digit, end multiple upper-case"
        text = "6HELLO"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin multiple upper-case, end single digit"
        text = "HELLO5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin single digit, multiple upper-case, end single digit"
        text = "6HELLO5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 7, "Failed " + test_str)

        test_str = "test_count: begin single digit, end mixed upper and lower-case"
        text = "6HeLlO"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin mixed upper and lower-case, end single digit"
        text = "HeLL05"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 6, "Failed " + test_str)

        test_str = "test_count: begin single digit, mixed upper and lower-case, end single digit"
        text = "6hElLo5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 7, "Failed " + test_str)

        test_str = "test_count: begin single digit, end single punctuation"
        text = "9!"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 2, "Failed " + test_str)

        test_str = "test_count: begin single punctuation, end single digit"
        text = "!9"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 2, "Failed " + test_str)

        test_str = "test_count: begin multiple digits, end single punctuation"
        text = "123456789$"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 10, "Failed " + test_str)

        test_str = "test_count: begin single punctuation, end multiple digits"
        text = "@123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 10, "Failed " + test_str)

        test_str = "test_count: begin single punctuation, multiple digits, end single punctuation"
        text = "@123456789^"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 11, "Failed " + test_str)

        test_str = "test_count: begin multiple punctuation, end single digit"
        text = "!@#$%^&*(){}[]:;\"',./?0'"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 24, "Failed " + test_str)

        test_str = "test_count: begin single digit, end multiple punctuation"
        text = "0!@#$%^&*(){}[]:;\"',./?"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 23, "Failed " + test_str)

        test_str = "test_count: begin single digit, multiple punctuation, end single digit"
        text = "0!@#$%^&*(){}[]:;\"',./?5"
        p = textproc.Processor(text)
        self.assertEqual(p.count(), 24, "Failed " + test_str)

    # Write one or more unit tests to test the count_alpha() method
    def test_count_alpha(self):
        test_str = "test_count_alpha: empty string"
        text = ""
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 0, "Failed: " + test_str)

        test_str = "test_count_alpha: single lower-case"
        text = "a"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 1, "Failed: " + test_str)

        test_str = "test_count_alpha: multiple lower-case"
        text = "abc"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 3, "Failed: " + test_str)

        test_str = "test_count_alpha: single upper-case"
        text = "M"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 1, "Failed: " + test_str)

        test_str = "test_count_alpha: multiple upper-case"
        text = "TOM"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 3, "Failed: " + test_str)

        test_str = "test_count_alpha: begin lower-case, end upper-case"
        text = "hI"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 2, "Failed: " + test_str)

        test_str = "test_count_alpha: begin upper-case, end lower-case"
        text = "Im"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 2, "Failed: " + test_str)

        test_str = "test_count_alpha: begin upper-case, mixed lower and upper-case, end lower-case"
        text = "LmNop"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 5, "Failed: " + test_str)

        test_str = "test_count_alpha: begin lower-case, mixed lower and upper-case, end upper-case"
        text = "lmNoP"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 5, "Failed: " + test_str)

        test_str = "test_count_alpha: single digit"
        text = "5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 0, "Failed: " + test_str)

        test_str = "test_count_alpha: multiple digits"
        text = "325"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 0, "Failed: " + test_str)

        test_str = "test_count_alpha: begin multiple lower-case, end digit"
        text = "nope5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin digit, end multiple lower-case"
        text = "4nope"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin multiple upper-case, end digit"
        text = "NOPE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin digit, end multiple upper-case"
        text = "3NOPE"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin digit, mixed upper and lower-case, end digit"
        text = "5nOpE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin multiple punctuation, end mixed upper and lower-case and digits"
        text = "!@#$%^&*(){}[]:;\"',./?5nOpE5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

        test_str = "test_count_alpha: begin multiple punctuation, end mixed upper and lower-case and digits"
        text = "5nOpE5!@#$%^&*(){}[]:;\"',./?"
        p = textproc.Processor(text)
        self.assertEqual(p.count_alpha(), 4, "Failed: " + test_str)

    # Write one or more unit tests to test the count_numeric() method
    def test_count_numeric(self):
        test_str = "test_count_numeric: empty string"
        text = ""
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: single lower-case"
        text = "a"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: multiple lower-case"
        text = "abc"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: single upper-case"
        text = "S"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: multiple upper-case"
        text = "XYZ"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: begin lower-case, end upper-case"
        text = "sM"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: begin upper-case, end lower-case"
        text = "Ms"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: begin digit, end lower-case"
        text = "5g"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 1, "Failed: " + test_str)

        test_str = "test_count_numeric: begin lower-case, end digit"
        text = "g9"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 1, "Failed: " + test_str)

        test_str = "test_count_numeric: begin digit, end upper-case"
        text = "5G"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 1, "Failed: " + test_str)

        test_str = "test_count_numeric: begin upper-case, end digit"
        text = "G9"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 1, "Failed: " + test_str)

        test_str = "test_count_numeric: begin upper-case, mixed digits and alpha, end upper-case"
        text = "G55i9yY"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: begin upper-case, mixed digits and alpha, end lower-case"
        text = "G55i9Yy"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: begin upper-case, mixed digits and alpha, end digit"
        text = "G55i9Y8"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 4, "Failed: " + test_str)

        test_str = "test_count_numeric: begin lower-case, mixed digits and alpha, end lower-case"
        text = "a55i9Yy"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: begin lower-case, mixed digits and alpha, end upper-case"
        text = "a55i9yY"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: begin lower-case, mixed digits and alpha, end digit"
        text = "a55i9yY5"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 4, "Failed: " + test_str)

        test_str = "test_count_numeric: begin punctuation, end digits"
        text = "-500"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: begin digits, end punctuation"
        text = "0123456789!"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 10, "Failed: " + test_str)

        test_str = "test_count_numeric: single digit"
        text = "1"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 1, "Failed: " + test_str)

        test_str = "test_count_numeric: multiple digits"
        text = "198"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 3, "Failed: " + test_str)

        test_str = "test_count_numeric: single punctuation"
        text = "!"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

        test_str = "test_count_numeric: multiple punctuation"
        text = "!@#$%^&*(){}[]:;\"',./?"
        p = textproc.Processor(text)
        self.assertEqual(p.count_numeric(), 0, "Failed: " + test_str)

    # Write one or more unit tests to test the count_vowels() method
    def test_count_vowels(self):
        test_str = "test_count_vowels: empty string"
        text = ""
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: single digit"
        text = "1"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: multiple digits"
        text = "0123456789"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: single punctuation"
        text = "!"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: single punctuation"
        text = "!"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: multiple punctuation"
        text = "!@#$%^&*(){}[]:;\"',./?"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 0, "Failed: " + test_str)

        test_str = "test_count_vowels: multiple vowels"
        text = "hello"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "Failed: " + test_str)

        test_str = "test_count_vowels: multiple lower-case vowels"
        text = "hello"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "Failed: " + test_str)

        test_str = "test_count_vowels: all lower-case vowels"
        text = "aeiou"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5, "Failed: " + test_str)

        test_str = "test_count_vowels: single upper-case vowels"
        text = "Apple"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "Failed: " + test_str)

        test_str = "test_count_vowels: multiple upper-case vowels"
        text = "AE"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 2, "Failed: " + test_str)

        test_str = "test_count_vowels: all upper-case vowels"
        text = "AEIOU"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5, "Failed: " + test_str)

        test_str = "test_count_vowels: mixed upper and lower-case vowels"
        text = "aEiOu"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 5, "Failed: " + test_str)

        test_str = "test_count_vowels: all vowels upper and lower-case"
        text = "aeiouAEIOU"
        p = textproc.Processor(text)
        self.assertEqual(p.count_vowels(), 10, "Failed: " + test_str)


# Write one or more unit tests to test the is_phonenumber() method

    def test_phone(self):
        # ASSUMPTION: Phone formats may take the following forms:
        # (xxx) xxx-xxxx
        # (xxx)xxx-xxxx
        # xxx xxx-xxxx
        # xxxxxxxxxx
        # xxx-xxx-xxxx
        # xxx xxx xxxx
        # xxx.xxx.xxxx
        test_str = "test_phone: empty string"
        text = ""
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: single punctuation"
        text = ","
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: multiple punctuation"
        text = "!@#$%^&*(){}[]:;\"',./?"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: single digit"
        text = "5"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: multiple digits"
        text = "512"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: (0xx) xxx-xxxx, area code begin with zero"
        text = "(012) 543-9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: (0xx)xxx-xxxx, area code begin with zero"
        text = "(012)543-9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: 0xx xxx-xxxx, area code begin with zero"
        text = "012 543-9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: 0xxxxxxxxx, area code begin with zero"
        text = "0125439786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: 0xx-xxx-xxxx, area code begin with zero"
        text = "012-543-9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: 0xx xxx xxxx, area code begin with zero"
        text = "012 543 9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: 0xx.xxx.xxxx, area code begin with zero"
        text = "012.543.9786"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: incorrect formatting, multiple parentheses"
        text = "(512) (123) (1234)"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), False, "Failed: " + test_str)

        test_str = "test_phone: (xxx) xxx-xxxx"
        text = "(555) 555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        test_str = "test_phone: (xxx)xxx-xxxx"
        text = "(555)555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        test_str = "test_phone: xxx xxx-xxxx"
        text = "512 123-1234"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        test_str = "test_phone: xxxxxxxxxx"
        text = "5555555555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        test_str = "test_phone: xxx-xxx-xxxx"
        text = "555-555-5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        test_str = "test_phone: xxx xxx xxxx"
        text = "555 555 5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)

        text = "555.555.5555"
        p = textproc.Processor(text)
        self.assertEqual(p.is_phonenumber(), True, "Failed: " + test_str)


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
