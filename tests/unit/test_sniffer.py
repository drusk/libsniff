# Copyright (C) 2013 David Rusk
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

__author__ = "David Rusk <drusk@uvic.ca>"

import unittest

from hamcrest import assert_that, equal_to

import libsniff


class PythonLibSnifferTest(unittest.TestCase):
    def setUp(self):
        self.sniffer = libsniff.PythonLibSniffer()

    def assert_sniffed(self, input_line, expected_lib):
        assert_that(self.sniffer.sniff_line(input_line),
                    equal_to(expected_lib))

    def test_sniff_plain_import_line(self):
        self.assert_sniffed("import flask", "flask")

    def test_sniff_from_lib_import_line(self):
        self.assert_sniffed("from flask import Flask", "flask")

    def test_sniff_non_import_line(self):
        self.assert_sniffed("def hello():", None)


if __name__ == '__main__':
    unittest.main()
