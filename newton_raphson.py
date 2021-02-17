# -- coding: UTF-8 --

"""
Implement the Newton-Raphson method for finding the real roots of an nth
degree polynomial with real valued coefficients. If the polynomial has no real
roots your function should throw an error indicating the same. Your function
should also take in a debug boolean flag variable, which when set to true
prints the following
○ The iteration number
○ The function value
○ The gradient of the function
○ The residual error
"""
import logging
import argparse

from horner_method import horner

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

FORMATTER = logging.Formatter("%(asctime)s: %(name)s %(message)s")

FILE_HANDLER = logging.FileHandler('nr.log')
FILE_HANDLER.setLevel(logging.ERROR)
FILE_HANDLER.setFormatter(FORMATTER)

STREAM_HANDLER = logging.StreamHandler()
STREAM_HANDLER.setFormatter(FORMATTER)

LOGGER.addHandler(FILE_HANDLER)
LOGGER.addHandler(STREAM_HANDLER)


def deriv(lst, x):
    """
    Function Description: To find the derivative of the polynomial at value x

    :param lst: Polynomial Coefficient
    :type lst: list

    :param x: Number for which the derivative of the polynomial to be found
    :type x: float

    :return: Derivative value
    :rtype: Float
    """
    total = 0
    for i in range(len(lst)-1):
        total = total + lst[i]*(len(lst)-i-1)*x**(len(lst)-i-2)

    return total


def find_root(lst, x, flag):
    """
    Function Description: To find the root using Newton Raphson method

    :param lst: Polynomial Coefficients
    :type lst: list

    :param x: Initial value to evaluate the func() and deriv()
    :type x: float

    :param flag: Whether or not to display the other parameters
    :type flag: bool

    :return: The root of the polynomial
    :rtype: Float
    """
    count = 0
    flag_root = True
    h = 10e-15
    try:
        h = horner(lst, x) / deriv(lst, x)
    except ZeroDivisionError:
        LOGGER.error("Tried to divide by zero")

    while abs(h) >= 0.00001:                     # make it user defined(optional)
        h = horner(lst, x) / deriv(lst, x)

        # x(i+1) = x(i) - f(x) / f'(x)
        x = x - h
        count = count + 1
        if count > 100:                      # make it user defined
            flag_root = False
            break
    if flag and flag_root and h != 10e-15:

        LOGGER.info(f"No Of Iterations:{count}")
        LOGGER.info(f"Value of the function:{horner(lst,x)}")
        LOGGER.info(f"Value of the derivative:{deriv(lst,x)}")
        LOGGER.info(f"Residual error:{h}")
    return x, flag_root


def arg_parse():
    """
    Function Description: To parse command line arguments

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs="+", type=float)
    parser.add_argument('-x', help="Initial value of x", type=float)
    parser.add_argument("-v", "--verbose", help="print extra values", default=0,
                        action="store_true")
    return parser.parse_args()


def main():
    args = arg_parse()

    polynomial = args.p
    x = args.x
    flag = args.verbose
    root, flag_root = find_root(polynomial, x, flag)            # Get it from user
    if flag_root:
        LOGGER.info(f"The value of the root is : {root}")
    else:
        LOGGER.info("The equation does not have a solution")


if __name__ == '__main__':
    main()
