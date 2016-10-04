import pandas


def read_file_1(filename):
    """ Reads in a file
    >>> read_file_1('testfiles/testfile1.txt')
    'hello'
    """
    with open(filename) as F:
        return F.read().strip()

from argparse import ArgumentParser

def prepare_parser():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', type=str,
                        required=True, help='input file')
    return parser

if __name__ == "__main__":
    options = prepare_parser().parse_args()

    print read_file_1(options.input)
