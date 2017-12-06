# -*- coding: utf-8 -*-
"""This script run test for words_count.py.
---------------------------------------------------------------------------------------------------------
To run test as package:
    1. $python -m word_frequency_counter test
To run test as module:
    2. $python words_count_test.py
----------------------------------------------------------------------------------------------------------
Default format output:
hello - 327
hi - 42
howdy - 17
-----------------------------------------------------------------------------------------------------------
Json format output:
{"howdy": 17, "hello": 327, "hi": 42, ...}
-----------------------------------------------------------------------------------------------------------

Tested with Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

Enhancement:
        Performance can be enhanced more using chuck for multiprocessing or pool.
        Handle encoding utf-8 for python < 27 and json.loads and json.dumps will be good for more generic
        Need to few more test cases.

"""

import unittest
from unittest import mock

try:
    from word_frequency_counter import words_count
except ModuleNotFoundError as m:
    import words_count



class WordCountTestSetup(unittest.TestCase):
    def setUp(self):
        print("Setting up the test to normalize lines into words.")

    def tearDown(self):
        print("Cleaning up the test to normalize lines into words.")


class SplitLineIntoWordsTestPass(WordCountTestSetup):
    """Positive case: normalization of lines into words correct and consistent."""

    def runTest(self):
        input_lines = "This is testing for python test.\nThis is hello."
        expected_out = [('this', 1), ('is', 1), ('testing', 1), ('for', 1), ('python', 1), ('test', 1), ('this', 1),
                        ('is', 1), ('hello', 1)]
        with mock.patch('{}.open'.format(__name__), mock.mock_open(read_data=input_lines),
                        create=True) as m:
            with open("file.txt") as input_file:
                actual_output = list(words_count.WordCount.map_words(input_file.readlines()))
                self.assertTrue(isinstance(actual_output, list), "Instance of actual output should be list.")
                self.assertEquals(len(actual_output), len(expected_out),
                                  "Length of both actual output and expected output list should be equal.")
                self.assertEquals(actual_output, expected_out,
                                  "\nFollowing lines:\n\n{}\n\nShould be converted as follows:\n\n '{}'".format(
                                      input_lines, expected_out))


class SplitLineIntoWordsTestFail(WordCountTestSetup):
    """Negative case: normalization of lines into words is wrong."""

    def runTest(self):
        input_lines = "This is testing for python test.\nThis is hello."
        expected_out = [('this', 1), ('is', 1), ('testing', 1), ('for', 1), ('python', 1), ('test', 1), ('this', 1),
                        ('is', 1)]
        with mock.patch('{}.open'.format(__name__), mock.mock_open(read_data=input_lines),
                        create=True) as m:
            with open("file.txt") as input_file:
                actual_output = list(words_count.WordCount.map_words(input_file.readlines()))
                self.assertFalse(not isinstance(actual_output, list),
                                 "Instance of actual out should be not be other than list.")
                self.failIfEqual(len(actual_output), len(expected_out),
                                 "Length of both actual and expected list should not be equal.")
                self.failIfEqual(actual_output, expected_out,
                                 "\nFollowing lines:\n\n{}\n\nWrong out:\n\n '{}'".format(
                                     input_lines, expected_out))


class ReduceWordCountTestSetup(unittest.TestCase):
    # wc = words_count.WordCount()
    def setUp(self):
        print("Setting up the test to sort and reduce the duplicate.")

    def tearDown(self):
        print("Cleaning up the test to sort and reduce the duplicate.")


class ReduceWordCountTestPass(ReduceWordCountTestSetup):
    """Positive case: Sorting and reducing the duplicating."""

    def runTest(self):
        input_lines = "This is testing for python test.\nThis is hello."
        expected_sorted_output = [('for', 1), ('hello', 1), ('is', 1), ('is', 1), ('python', 1), ('test', 1),
                                  ('testing', 1), ('this', 1), ('this', 1)]
        expected_sorted_grouped_output = [('for', 1), ('hello', 1), ('is', 2), ('python', 1), ('test', 1),
                                          ('testing', 1), ('this', 2)]
        with mock.patch('{}.open'.format(__name__), mock.mock_open(read_data=input_lines),
                        create=True) as m:
            with open("file.txt") as input_file:
                actual_sorted_output = sorted(words_count.WordCount.map_words(input_file.readlines()))
                self.assertTrue(isinstance(actual_sorted_output, list),
                                "Instance of sorted actual output should be list.")
                self.assertEquals(len(actual_sorted_output), len(expected_sorted_output),
                                  "Length of both sorted actual output and expected output list should be equal.")
                actual_sorted_grouped_output = list(words_count.WordCount.reduce_word_counts(actual_sorted_output))

                self.assertTrue(isinstance(actual_sorted_grouped_output, list),
                                "Instance of actual grouped output should be list.")
                self.assertEquals(len(actual_sorted_grouped_output), len(expected_sorted_grouped_output),
                                  "Length of both actual grouped output list and expected grouped output list should be equal.")
                self.assertEquals(actual_sorted_grouped_output, expected_sorted_grouped_output,
                                  "\nFollowing lines:\n\n{}\n\nShould be converted as follows:\n\n '{}'".format(
                                      input_lines, expected_sorted_grouped_output))


class ReduceWordCountTestFail(ReduceWordCountTestSetup):
    """Positive case: Sorting and reducing the duplicating."""

    def runTest(self):
        input_lines = "This is testing for python test.\nThis is hello."
        expected_sorted_output = [('for', 1), ('hello', 1), ('is', 1), ('is', 1), ('python', 1), ('test', 1),
                                  ('testing', 1), ('this', 1)]
        expected_sorted_grouped_output = [('for', 1), ('hello', 1), ('is', 2), ('python', 1), ('test', 1),
                                          ('testing', 1)]
        with mock.patch('{}.open'.format(__name__), mock.mock_open(read_data=input_lines),
                        create=True) as m:
            with open("file.txt") as input_file:
                actual_sorted_output = sorted(words_count.WordCount.map_words(input_file.readlines()))
                self.assertFalse(not isinstance(actual_sorted_output, list),
                                "Instance of sorted actual output should not be list.")
                self.failIfEqual(len(actual_sorted_output), len(expected_sorted_output),
                                  "Length of both sorted actual output and expected output list should be equal.")
                actual_sorted_grouped_output = list(words_count.WordCount.reduce_word_counts(actual_sorted_output))

                self.assertFalse(not isinstance(actual_sorted_grouped_output, list),
                                "Instance of actual grouped output should be list.")
                self.failIfEqual(len(actual_sorted_grouped_output), len(expected_sorted_grouped_output),
                                  "Length of both actual grouped output list and expected grouped output list should be equal.")
                self.failIfEqual(actual_sorted_grouped_output, expected_sorted_grouped_output,
                                  "\nFollowing lines:\n\n{}\n\nWrong out:\n\n '{}'".format(
                                      input_lines, expected_sorted_grouped_output))

def suite():
    suites = unittest.TestSuite()
    suites.addTest(SplitLineIntoWordsTestPass())
    suites.addTest(SplitLineIntoWordsTestFail())
    suites.addTest(ReduceWordCountTestPass())
    suites.addTest(ReduceWordCountTestFail())
    return suites


def main():
    runner = unittest.TextTestRunner()
    test_suite = suite()
    runner.run(test_suite)


if __name__ == "__main__":
    main()
    help(__name__)
