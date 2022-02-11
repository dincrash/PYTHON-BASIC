import argparse
import sys


def main(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('-a')
    process(**vars(parser.parse_args(args)))
    return 0


def process(a=None):
    pass

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))