# -- coding: UTF-8 --

"""
Compute the autocorrelation of a signal for a given lag. Lag can go from 1 to
N-2 where N is the length of the signal
"""
import logging
import argparse

from functools import reduce

__author__ = 'saranya@gyandata.com'

logging.basicConfig(filename='A1_2.log', level=logging.INFO)


def mean(x):
    """
    Function Description: To find mean of values from a list

    :param x: Signal Values
    :type x: list
    :return: Mean value of x
    :rtype: Float
    """

    return sum(x)/len(x)


def variance(x, m):
    """
    Function Description: To find the variance of values from a list

    :param x: Signal Values
    :type: list

    :param m: Mean obtained from mean()
    :type m: float

    :return: Variance of x
    :rtype: float
    """
    return reduce(lambda a, b: a+(b-m)*(b-m), [(x[:1][0]-m)**2]+x[1:])


def autocorrelation(x, k):
    """
    Function Description: To find the autocorrelation using signal values and lag value

    :param x: Signal input
    :type x: list

    :param k: Value of lag
    :type k: int

    :return: none
    """
    if k > len(x) - 2:
        logging.error('The value of lags exceed its limit')
    else:
        m = mean(x)
        vr = variance(x, m)
        n = 0
        for i in range(1, len(x)):
            n = n + (x[i] - m) * (x[i - k] - m)
        numerator = n/vr
        logging.info(f"The value of autocorrelation for lag={k} is:{numerator}")


def arg_parse():
    """
    Function Description: To parse command line arguments
    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', nargs="+", type=float)
    parser.add_argument("-k", help="x value", type=int)
    return parser.parse_args()


def main():
    args = arg_parse()

    signal_inp = args.s   # [float(i) for i in input("Enter the signal values(as list):").split(" ")]
    lag_inp = args.k   # int(input("Enter the value of lag:"))

    autocorrelation(signal_inp, lag_inp)


if __name__ == '__main__':
    main()
