version: 0.0.1

Help on module __main__:

NAME
    __main__

DESCRIPTION
    This script counts frequency of words from English utf-8 format text file.
    Valid english word is extract based on regex '\W+'.
    ---------------------------------------------------------------------------------------------------------
    This script will be run only command-line.

    To run package: /exercise
        1. $python -m word_count file.txt (default format)
        2. $python -m word_count file.txt json (json format)
    To save in  file
        3. $python -m word_count file.txt --save
        4. $python -m word_count file.txt json --save

    To run module: /exercise/word_count
        1. $python word_count.py file.txt (default format)
        2. $python word_count.py file.txt json (json format)
    To save in  file
        3. $python word_count.py file.txt --save
        4. $python word_count.py file.txt json --save


    To run test package: /exercise
        5. $python -m word_count test

    To run test module: /exercise/word_count
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
            Add setup.py if mock is not installed or for any dependency. Running fine with my installed library.
            Document can be make more concise.

DATA
    __annotations__ = {}
    e = IndexError('list index out of range',)

Module
    from word_count import words_count
    from word_count import words_count_test
    import sys
    import re

FILE
    c:\users\patir\documents\github\newdangular\djangular\word_count\__main__.py






Help on module words_count.py:

NAME
    __main__ - Tested with Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32

DESCRIPTION
    Enhancement:
            Performance can be enhanced more using chuck for multiprocessing or pool.
            Handle encoding utf-8 for python < 27 and json.loads and json.dumps will be good for more generic
            Need to few more test cases.

CLASSES
    builtins.object
        WordCount

    class WordCount(builtins.object)
     |  Methods defined here:
     |
     |  __init__(self, *file_name)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |
     |  count_words_in_ascending(self)
     |      Display words frequency in ascending order
     |
     |  count_words_in_json(self)
     |      Display words frequency in dictionary or json format
     |
     |  save_count_words_in_ascending(self)
     |      Save words frequency in ascending order.
     |
     |  save_count_words_in_json(self)
     |      Save words frequency in json format.
     |
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |
     |  map_words(input_file)
     |      Split each line into words, yield each word and count 1 as the key-value pair.
     |
     |  reduce_word_counts(input_file)
     |      Reduce key-value pairs and count frequency
     |
     |  sort_reduce_word_counts(t)
     |      Sort by frequency of word and yield result.
     |
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |
     |  __dict__
     |      dictionary for instance variables (if defined)
     |
     |  __weakref__
     |      list of weak references to the object (if defined)

FUNCTIONS
    main()
        Commands:
            1. $python word_count.py file.txt (default format)
            2. $python word_count.py file.txt json (json format)
        To save in file
            3. $python word_count.py file.txt --save
            4. $python word_count.py file.txt json --save
        Num of words want to view: 10
        Num of words want to view: 15
        ...

    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
        Open file and return a stream.  Raise IOError upon failure.

        file is either a text or byte string giving the name (and the path
        if the file isn't in the current working directory) of the file to
        be opened or an integer file descriptor of the file to be
        wrapped. (If a file descriptor is given, it is closed when the
        returned I/O object is closed, unless closefd is set to False.)

        mode is an optional string that specifies the mode in which the file
        is opened. It defaults to 'r' which means open for reading in text
        mode.  Other common values are 'w' for writing (truncating the file if
        it already exists), 'x' for creating and writing to a new file, and
        'a' for appending (which on some Unix systems, means that all writes
        append to the end of the file regardless of the current seek position).
        In text mode, if encoding is not specified the encoding used is platform
        dependent: locale.getpreferredencoding(False) is called to get the
        current locale encoding. (For reading and writing raw bytes use binary
        mode and leave encoding unspecified.) The available modes are:

        ========= ===============================================================
        Character Meaning
        --------- ---------------------------------------------------------------
        'r'       open for reading (default)
        'w'       open for writing, truncating the file first
        'x'       create a new file and open it for writing
        'a'       open for writing, appending to the end of the file if it exists
        'b'       binary mode
        't'       text mode (default)
        '+'       open a disk file for updating (reading and writing)
        'U'       universal newline mode (deprecated)
        ========= ===============================================================

        The default mode is 'rt' (open for reading text). For binary random
        access, the mode 'w+b' opens and truncates the file to 0 bytes, while
        'r+b' opens the file without truncation. The 'x' mode implies 'w' and
        raises an `FileExistsError` if the file already exists.

        Python distinguishes between files opened in binary and text modes,
        even when the underlying operating system doesn't. Files opened in
        binary mode (appending 'b' to the mode argument) return contents as
        bytes objects without any decoding. In text mode (the default, or when
        't' is appended to the mode argument), the contents of the file are
        returned as strings, the bytes having been first decoded using a
        platform-dependent encoding or using the specified encoding if given.

        'U' mode is deprecated and will raise an exception in future versions
        of Python.  It has no effect in Python 3.  Use newline to control
        universal newlines mode.

        buffering is an optional integer used to set the buffering policy.
        Pass 0 to switch buffering off (only allowed in binary mode), 1 to select
        line buffering (only usable in text mode), and an integer > 1 to indicate
        the size of a fixed-size chunk buffer.  When no buffering argument is
        given, the default buffering policy works as follows:

        * Binary files are buffered in fixed-size chunks; the size of the buffer
          is chosen using a heuristic trying to determine the underlying device's
          "block size" and falling back on `io.DEFAULT_BUFFER_SIZE`.
          On many systems, the buffer will typically be 4096 or 8192 bytes long.

        * "Interactive" text files (files for which isatty() returns True)
          use line buffering.  Other text files use the policy described above
          for binary files.

        encoding is the name of the encoding used to decode or encode the
        file. This should only be used in text mode. The default encoding is
        platform dependent, but any encoding supported by Python can be
        passed.  See the codecs module for the list of supported encodings.

        errors is an optional string that specifies how encoding errors are to
        be handled---this argument should not be used in binary mode. Pass
        'strict' to raise a ValueError exception if there is an encoding error
        (the default of None has the same effect), or pass 'ignore' to ignore
        errors. (Note that ignoring encoding errors can lead to data loss.)
        See the documentation for codecs.register or run 'help(codecs.Codec)'
        for a list of the permitted encoding error strings.

        newline controls how universal newlines works (it only applies to text
        mode). It can be None, '', '\n', '\r', and '\r\n'.  It works as
        follows:

        * On input, if newline is None, universal newlines mode is
          enabled. Lines in the input can end in '\n', '\r', or '\r\n', and
          these are translated into '\n' before being returned to the
          caller. If it is '', universal newline mode is enabled, but line
          endings are returned to the caller untranslated. If it has any of
          the other legal values, input lines are only terminated by the given
          string, and the line ending is returned to the caller untranslated.

        * On output, if newline is None, any '\n' characters written are
          translated to the system default line separator, os.linesep. If
          newline is '' or '\n', no translation takes place. If newline is any
          of the other legal values, any '\n' characters written are translated
          to the given string.

        If closefd is False, the underlying file descriptor will be kept open
        when the file is closed. This does not work when a file name is given
        and must be True in that case.

        A custom opener can be used by passing a callable as *opener*. The
        underlying file descriptor for the file object is then obtained by
        calling *opener* with (*file*, *flags*). *opener* must return an open
        file descriptor (passing os.open as *opener* results in functionality
        similar to passing None).

        open() returns a file object whose type depends on the mode, and
        through which the standard file operations such as reading and writing
        are performed. When open() is used to open a file in a text mode ('w',
        'r', 'wt', 'rt', etc.), it returns a TextIOWrapper. When used to open
        a file in a binary mode, the returned class varies: in read binary
        mode, it returns a BufferedReader; in write binary and append binary
        modes, it returns a BufferedWriter, and in read/write mode, it returns
        a BufferedRandom.

        It is also possible to use a string or bytearray as a file for both
        reading and writing. For strings StringIO can be used like a file
        opened in a text mode, and for bytes a BytesIO can be used like a file
        opened in a binary mode.

DATA
    __annotations__ = {}

FILE
    c:\users\patir\documents\github\newdangular\djangular\word_count\words_count.py


Help on module words_count_test.py:

NAME
    __main__

DESCRIPTION
    This script run test for words_count.py.
    ---------------------------------------------------------------------------------------------------------
    To run test as package:
        1. $python -m word_count test
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

CLASSES
    unittest.case.TestCase(builtins.object)
        ReduceWordCountTestSetup
            ReduceWordCountTestFail
            ReduceWordCountTestPass
        WordCountTestSetup
            SplitLineIntoWordsTestFail
            SplitLineIntoWordsTestPass

    class ReduceWordCountTestFail(ReduceWordCountTestSetup)
     |  Positive case: Sorting and reducing the duplicating.
     |
     |  Method resolution order:
     |      ReduceWordCountTestFail
     |      ReduceWordCountTestSetup
     |      unittest.case.TestCase
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  runTest(self)
     |
     |  ----------------------------------------------------------------------
     |  Methods inherited from ReduceWordCountTestSetup:
     |
     |  setUp(self)
     |      Hook method for setting up the test fixture before exercising it.
     |
     |  tearDown(self)
     |      Hook method for deconstructing the test fixture after testing it.
     |
     |  ----------------------------------------------------------------------

