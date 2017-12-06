# -*- coding: utf-8 -*-
"""Version: 0.0.1
This script counts frequency of words from English utf-8 format text file.
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
from word_frequency_counter import words_count
from word_frequency_counter import words_count_test
import sys
import re
try:
    if sys.argv[1] == 'test':
        words_count_test.main()
    else:
        if re.match(".*\.txt", sys.argv[1]) and len(sys.argv) <= 4:
            # help(main)
            wc = words_count.WordCount(sys.argv[1])
            # words_count.main(sys.argv[1])
            if len(sys.argv) is 2:
                wc.count_words_in_ascending()
            elif len(sys.argv) is 3 and str.lower(sys.argv[2]) == "json":
                wc.count_words_in_json()
            elif len(sys.argv) is 3 and str.lower(sys.argv[2]) == "--save":
                wc.save_count_words_in_ascending()
            elif len(sys.argv) is 4 and str.lower(sys.argv[2]) == "json" and str.lower(sys.argv[3]) == "--save":
                wc.save_count_words_in_json()
            else:
                help(words_count.WordCount.__module__)
                sys.exit()
        else:
            help(__name__)
            sys.exit()
except IndexError as e:
    print("Hmmmm! Something is wrong. Please read instructions.", e)
    help(__name__)