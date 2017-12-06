# -*- coding: utf-8 -*-
"""This script counts frequency of words from English utf-8 format text file.
Valid english word is extract based on regex '\W+'.
---------------------------------------------------------------------------------------------------------
This script will be run only command-line.
To run module: /exercise/word_frequency_counter
    1. $python word_frequency_counter.py file.txt (default format)
    2. $python word_frequency_counter.py file.txt json (json format)
To save in  file
    3. $python word_frequency_counter.py file.txt --save
    4. $python word_frequency_counter.py file.txt json --save

To run package: /exercise
    1. $python -m word_frequency_counter file.txt (default format)
    2. $python -m word_frequency_counter file.txt json (json format)
To save in  file
    3. $python -m word_frequency_counter file.txt --save
    4. $python -m word_frequency_counter file.txt json --save

To run test package: /exercise
    5. $python -m word_frequency_counter test

To run test module: /exercise/word_frequency_counter
    6. $python words_count_test.py
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
import re
import sys
from itertools import groupby
from operator import itemgetter
from inspect import currentframe, getframeinfo
from io import open
import json


def main():
    if re.match(".*\.txt", sys.argv[1]) and len(sys.argv) <= 4:
        wc = WordCount(sys.argv[1])
        if len(sys.argv) is 2:
            wc.count_words_in_ascending()
        elif len(sys.argv) is 3 and str.lower(sys.argv[2]) == "json":
            wc.count_words_in_json()
        elif len(sys.argv) is 3 and str.lower(sys.argv[2]) == "--save":
            wc.save_count_words_in_ascending()
        elif len(sys.argv) is 4 and str.lower(sys.argv[2]) == "json" and str.lower(sys.argv[3]) == "--save":
            wc.save_count_words_in_json()
        else:
            help(WordCount().__module__)
            sys.exit()
    else:
        help(WordCount().__module__)
        sys.exit()


class WordCount(object):
    def __init__(self, *file_name):
        if file_name != ():
            self.file_name = file_name[0]

    @staticmethod
    def map_words(input_file):
        """ Split each line into words, yield each word and count 1 as the key-value pair."""
        for line in input_file:
            for word in re.split('\W+|_', line):
                if word != '':
                    try:
                        yield word.lower().strip(), 1
                    except StopIteration as stop_iteration_exception:
                        print("Error: ", stop_iteration_exception)

    @staticmethod
    def reduce_word_counts(input_file):
        """ Reduce key-value pairs and count frequency """
        for key, group in groupby(input_file, key=itemgetter(0)):
            try:
                yield key, sum([count for word, count in group])
            except StopIteration as stop_iteration_exception:
                print("Error: ", stop_iteration_exception)

    @staticmethod
    def sort_reduce_word_counts(t):
        """ Sort by frequency of word and yield result."""
        for key, value in sorted(t, key=itemgetter(1), reverse=True):
            try:
                yield key, value
            except StopIteration as stop_iteration_exception:
                print("Error: ", stop_iteration_exception)

    def count_words_in_ascending(self):
        """Display words frequency in ascending order"""
        with open(self.file_name, 'r', encoding='utf-8') as input_file:
            generated_words = self.sort_reduce_word_counts(self.reduce_word_counts(sorted(self.map_words(input_file))))
            while True:
                try:
                    check_empty_generator = 0
                    for key, value in list(next(generated_words) for _ in range(int(input("Num of words want to view:")))):
                        print("{} - {}".format(key, value))
                        check_empty_generator += 1
                    if check_empty_generator is 0:
                        print("No more words to be displayed.")
                        sys.exit()
                except StopIteration as e:
                    print("Stop Iteration exception occurred in", __name__, "line -", getframeinfo(currentframe()).lineno,
                          "try again with less value.")
                    sys.exit()

    def count_words_in_json(self):
        """Display words frequency in dictionary or json format"""
        with open(self.file_name, 'r', encoding='utf-8') as input_file:
            print(dict(self.reduce_word_counts(sorted(self.map_words(input_file)))))

    def save_count_words_in_ascending(self):
        """Save words frequency in ascending order."""
        generated_words = None
        with open(self.file_name, 'r', encoding='utf-8') as input_file:
            generated_words = self.sort_reduce_word_counts(self.reduce_word_counts(sorted(self.map_words(input_file))))

        with open("frequency_of_words.txt", 'a', encoding='utf-8') as out_file:
            for key, value in generated_words:
                out_file.write(str(key) + str(' - ') + str(value)+'\n')
        print("Successfully saved!")

    def save_count_words_in_json(self):
        """Save words frequency in json format."""
        generated_words = None
        with open(self.file_name, 'r', encoding='utf-8') as input_file:
            generated_words = self.reduce_word_counts(sorted(self.map_words(input_file)))

        with open("frequency_of_words_dic.txt", 'a', encoding='utf-8') as out_file:
            out_file.write(str(dict(generated_words)))
            print("Successfully saved!")

if __name__ == "__main__":
    main()
