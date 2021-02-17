# -- coding: UTF-8 --

"""
Given a positive integer N, find the closest number to N which can be written
as 2^p
"""
import logging
import logging.config
import argparse

__author__ = 'saranya@gyandata.com'

logging.config.fileConfig('config.conf', disable_existing_loggers=False)
# create logger
LOGGER = logging.getLogger('__name__')   # Change it to LOGGER


def binary(num):

    """
    Function Description: To find the binary equivalent of a given number

    :param num: The number to be converted to binary representation
    :type num: int

    :return: Binary value of num
    :rtype: str
    """

    return bin(num).replace("0b", "")


def find_nn(number):

    """
    Function Description: To find the nearest power of 2 to the number

    :param number: Input Number
    :type number: int

    :return: The power to closer to number
    :rtype: int
    """
    string = binary(number)
    n = len(string)
    if number - 2 ** (n - 1) < 2 ** n - number:
        return 2 ** (n - 1)
    else:
        return 2 ** n


def arg_parse():
    """

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('num', help="Angle of sine to be found", type=int)
    return parser.parse_args()


def main():
    args = arg_parse()

    inp_num = args.num   # int(input("Enter the number:"))
    closer_num = find_nn(inp_num)
    LOGGER.info(f'The power of 2 closer to number {inp_num} is {closer_num}')


if __name__ == '__main__':
    main()
