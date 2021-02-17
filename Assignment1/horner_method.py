# -- coding: UTF-8 --


"""
Implement horner’s method for polynomial evaluation
"""

import logging
import argparse

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

FORMATTER = logging.Formatter("%(levelname)s: %(name)s %(message)s")

FILE_HANDLER = logging.FileHandler('horner.log')
FILE_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)


def horner(poly, x):
    """
    Function Description: To find the value of the polynomial using Horner's method

    :param poly: Coefficients of the polynomial
    :type poly: list

    :param x:  x for which the value of the polynomial to be found
    :type x: float

    :return: value of the polynomial at x
    :rtype: float
    """
    n = len(poly)
    tot = 0
    for i in range(n):
        tot = tot*x + poly[i]
    return tot


def arg_parse():
    """
    Function Description: To parse command line arguments

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', nargs="+", type=float)
    parser.add_argument("-x", help="x value", type=float)
    return parser.parse_args()


def main():
    args = arg_parse()                                            # CLI: python A1_1.py -a 1 3 3 1 -x -1

    polynomial = args.a
    x = args.x
    value = horner(polynomial, x)
    LOGGER.info(f"The value of the polynomial at x={x} is {value}")


if __name__ == '__main__':
    main()
