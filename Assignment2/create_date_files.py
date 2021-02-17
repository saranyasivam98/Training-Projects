# -- coding: UTF-8 --

"""
You are working on a project where a client has given you a directory with a whole
bunch of csv/txt/pdf files. The client tells you that the csv files are the ones that
contain the data and there are multiple csv files for each date. The csv files of the
same date need to be grouped together into a single directory before further
analyses could be performed. The client also tells you that the date format for each
data-dump he/she is about to give you can change across each data-dump.
Your task now is to :
● Write a program which would perform the given task
● Write a test program which would synthetically generate csv/txt files for you to
verify that the program that you wrote is working correctly
"""

import logging
import logging.config
import argparse
import re
import os
import random
import json
from datetime import datetime
from pathlib import Path

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'  # use os.join.path


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
        """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def arg_parse():
    """
    Function Description: To parse command line arguments
    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", help='Date', type=str)
    parser.add_argument("-f", help='format', type=str)
    parser.add_argument("-n", help='name of the folder', type=str)

    return parser.parse_args()


def proper_date(date):
    """
    Function Description: To set the separator in the dates to a constant '-'

    :param date: Input date from user
    :type date: str
    :return: date with '-' separator
    :rtype: str
    """
    return re.sub('[^a-zA-Z0-9 \n.]', '-', date)


def files_creation(date):
    """
    function Description: To create files with the input date from the user as file name
    :param date: user input date for file creation
    :type date: str
    """
    try:

        for i in range(1, 4):
            file_name = str(date) + '_' + str(i) + '.txt'
            with open(file_name, 'w') as file:
                file.write(str(random.randrange(0, 50)))

            file_name = str(date) + '_' + str(i) + '.csv'
            with open(file_name, 'w') as file:
                file.write(str(random.randrange(50, 100)))

            file_name = str(date) + '_' + str(i) + '.pdf'
            with open(file_name, 'w') as file:
                file.write(str(random.randrange(100, 150)))
        LOGGER.info("The files are created")
    except OSError:
        LOGGER.error("Invalid separator")


def check_acceptable_separator(date):
    """
    Function Description: To check for the acceptable separator in the given date
    :param date: The input date given by the user
    :type date: str
    :return: The value if there is an unacceptable separator
    :rtype: bool
    """
    value = True
    for date_part in date:
        if date_part in "\\/:*.?<>|":
            value = False
            LOGGER.error("Invalid separator")
            break
    return value


def main():
    """ The main function"""
    args = arg_parse()
    setup_logging()

    inp_date = args.d
    inp_format = args.f
    dir_name = args.n

    # p_date = proper_date(inp_date)
    try:
        t_date = datetime.strptime(inp_date, inp_format)  # pylint: disable=unused-variable
        value = check_acceptable_separator(inp_date)
        if value:
            dir_path = Path.cwd() / dir_name
            if dir_path.is_dir():
                os.chdir(dir_path)
                files_creation(inp_date)
            else:

                LOGGER.error("Invalid directory")
    except ValueError:
        LOGGER.error("Invalid format")


if __name__ == '__main__':
    main()
