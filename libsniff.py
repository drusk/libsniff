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

import os


class AbstractLibSniffer(object):
    def sniff(self, filename):
        libs = []

        with open(filename, "rb") as filehandle:
            for line in filehandle:
                lib = self.sniff_line(line)

                if lib is not None:
                    libs.append(lib)

        return libs

    def sniff_line(self, line):
        raise NotImplementedError()


class PythonLibSniffer(AbstractLibSniffer):
    def sniff_line(self, line):
        if "import" not in line:
            return None

        # TODO: regex?
        return line.split(" ")[1]


_sniffers = {".py": PythonLibSniffer()}


def get_sniffer(file_extension):
    """
    Determines an appropriate sniffer for a file given its extension.
    """
    return _sniffers[file_extension]


def findlibs(path):
    """
    Finds libraries used in the project at the specified path.

    Args:
      path: str
        The path to the project whose content will be searched for libraries.

    Returns:
      libs: list(str)
        A list of the library names.
    """
    all_libs = []

    for filename in os.listdir(path):
        extension = os.path.splitext(filename)[1]

        libs = get_sniffer(extension).sniff(os.path.join(path, filename))
        all_libs.extend(libs)

    return all_libs
