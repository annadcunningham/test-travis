import pandas

def read_file_1(filename):
    """ Reads in a file
    >>> read_file_1('../testfiles/testfile1.txt')
    'hello'
    """
    with open(filename) as F:
        return F.read().strip()
