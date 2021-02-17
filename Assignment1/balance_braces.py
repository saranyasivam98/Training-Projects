# -- coding: UTF-8 --

"""
Given a string containing opening and closing braces verify if the string is
balanced or not with regards to opening and closing braces. The braces can
be () or {} or [] and any combination of these
"""

import logging
import argparse

__author__ = 'saranya@gyandata.com'

# logging.basicConfig(filename='balance_braces.log', level=logging.INFO)
LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s: %(name)s %(message)s")

file_handler = logging.FileHandler('balance_braces.log')
file_handler.setLevel(logging.ERROR)
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)

LOGGER.addHandler(file_handler)
LOGGER.addHandler(stream_handler)


def remove_characters(string, open_b, close_b):
    """
    Function Description: To remove characters other than the braces

    :param string: Input string from the user
    :type string: str

    :param open_b: Contains all the opening braces '{' '[' '('
    :type open_b: list

    :param close_b: Contains all the closing braces '}' ']' ')'
    :type close_b: list

    :return: Removing the characters and appending the braces to a list
    :rtype: list
    """
    braces = []
    for ele in string:
        if ele in close_b or ele in open_b:
            braces.append(ele)
    if len(braces) == 0:
        LOGGER.error("Enter a string with braces")
    return braces


def check_balance(lst, open_b, close_b):
    """
    Function Description: To check the balance of the braces in a string

    :param lst: list of braces from the input string
    :type lst: list

    :param open_b: Contains all the opening braces '{' '[' '('
    :type open_b: list

    :param close_b: Contains all the closing braces '}' ']' ')'
    :type close_b: list

    :return: 1 if string is not balanced
    :rtype: int
    """
    all_braces = [['(', ')'], ['[', ']'], ['{', '}']]
    flag = 1
    while len(lst) > 0:
        last_open = 'a'
        first_close = 'b'
        index_fc = -10
        for ele in lst:
            if ele in open_b:
                last_open = ele
            if ele in close_b:
                first_close = ele
                index_fc = lst.index(ele)
                break

        if [last_open, first_close] in all_braces:
            del lst[index_fc - 1: index_fc + 1]

        else:
            flag = 0
            break
    return flag


def arg_parse():
    """
    Function Description: To parse command line arguments
    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("string", help="input string")
    return parser.parse_args()


def main():
    args = arg_parse()

    b_open = ['[', '{', '(']
    b_close = [']', '}', ')']

    # inp_string = input("Enter your string:")
    inp_string = args.string
    lst_braces = remove_characters(inp_string, b_open, b_close)
    value = check_balance(lst_braces, b_open, b_close)
    if value == 0:
        LOGGER.info("The string is not balanced")
    else:
        LOGGER.info('The string is balanced')


if __name__ == '__main__':
    main()
