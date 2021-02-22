# -- coding: UTF-8 --

"""
Check CSV
=========
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
import argparse
import re
import shutil
from pathlib import Path
import os
from datetime import datetime
import json
import logging
import logging.config

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
    """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def unique(list1):
    """
    Function Description: To get the unique dates from a set of dates

    :param list1: Input list
    :type list1: list
    :return: unique values in the input list
    :rtype: list
    """
    list_set = set(list1)
    unique_list = (list(list_set))
    return unique_list


def get_csv_files(path_to_csv):
    """
    Function Description: To get all te csv files from a directory        # combine get_csv_files and get_file_names

    :param path_to_csv: Path where the csv files are stored
    :type path_to_csv: Path

    :return: csv_files and csv_files in string format
    :rtype: Union[pathlib.Path , str]
    """
    csv_files = path_to_csv.glob('*.csv')
    filenames = os.listdir(path_to_csv)
    csv_files_s = [filename for filename in filenames if filename.endswith('.csv')]
    if len(csv_files_s) > 0:
        LOGGER.info("CSV files are found")
    return csv_files, csv_files_s


def get_file_names(files):
    """
    Function Description:  To get the file names of the csv files

    :param files: The path of the csv files
    :type files: path
    :return: File names extracted from the path
    :rtype: list
    """
    file_names = []

    for file in files:
        file_names.append(file.name.replace('.csv', ''))
    return file_names


def is_date(file_names, fmts):
    """
    Function Description: To extract the dates from any of the formats mentioned

    :param file_names: Names of the csv files without the .csv extension
    :type file_names: list[str]
    :param fmts: All possible formats in which date can be entered
    :type fmts: tuple
    :return: Dates of the files as datetime.time object
    :type: list
    """
    file_dates = []
    parsed = []
    for file in file_names:
        c_date = ret_datetime_obj(file, fmts)
        file_dates.append(c_date)
        parsed.append((file, c_date))

    success = {t[0] for t in parsed}
    for name in file_names:
        if name not in success:
            LOGGER.warning("Date:%s is not according the format ", name)

    return file_dates


def ret_datetime_obj(date_name, fmts):  # call it inside the is_date func
    """
    Function Description: To return the datetime.date object for a date

    :param date_name: Dates
    :type date_name: str
    :param fmts: All possible formats in which date can be entered
    :type fmts: tuple
    :return: date as datetime.date object
    :rtype: datetime.date
    """
    t_date = '01-01-2001'
    for fmt in fmts:
        try:
            t_date = datetime.strptime(date_name, fmt)
            break
        except ValueError:
            pass

    return t_date.date()


def clear_repetition(file_names):
    """
    Function Description: To clear the repetition in file names

    :param file_names: All the filenames with repetition
    :type file_names: list[str]
    :return: filenames cleared with '_number'
    :rtype: list
    :raises ValueError: if file_names is empty.
    """
    final_names = []
    for name in file_names:
        final_names.append(name[:-2])
    return final_names


def create_directory(unique_dates):
    """
    Function Description: To create directories for the dates

    :param unique_dates: The unique dates obtained from all the csv files
    :type unique_dates: list[str]
    """
    for ele in unique_dates:
        new_dir = Path.cwd() / str(ele)
        new_dir.mkdir()
    LOGGER.info("The directories are created")


def copy_files(csv_files_str, fmts, unique_dates):
    """
    Function Description: To copy the files under its respective date in the directory created

    :param csv_files_str: The path of csv files stored as string
    :type csv_files_str: list[str]
    :param fmts: All possible formats in which date can be entered
    :type fmts: tuple
    :param unique_dates: The unique dates obtained from all the csv files
    :type unique_dates: list[str]
    """
    for file in csv_files_str:
        path = Path(file)
        f_name = path.name.replace('.csv', '')  # shutil.copy(f, path)
        f_name = f_name[:-2]
        p_name = check_proper_date(f_name)
        date_obj = ret_datetime_obj(p_name, fmts)
        if date_obj in unique_dates:
            file_path = Path.cwd() / str(date_obj)
            shutil.copy(file, file_path)
    LOGGER.info("The files are copied")


def check_proper_dates(dates):
    """
    Function Description: To set the separator in the dates to a constant '-'

    :param dates: Input date from user
    :type dates: list[str]
    :return: date with '-' separator
    :rtype: list
    """
    final_dates = []
    for date in dates:
        final_dates.append(check_proper_date(date))

    return final_dates


def check_proper_date(date):
    """
    Function Description: To set the separator in the dates to a constant '-'

    :param date: Input date from user
    :type date: str
    :return: date with '-' separator
    :rtype: str
    """
    return re.sub('[^a-zA-Z0-9 \n]', '-', date)


def arg_parse():
    """
    Function Description: To parse command line arguments
    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("d", help='enter the directory name', type=str)
    return parser.parse_args()


def ambiguity(dates):
    """
    Function Description: To display a warning if any ambiguity is present
    :param dates: The unique dates obtained
    :type dates: list
    """
    lists = []
    for i, _ in enumerate(dates):  # for i in range(len(dates)):
        lst = []
        d_lst = str(dates[i]).split("-")
        for ele in d_lst:
            lst.append(int(ele))
        lists.append(lst)
    for i, _ in enumerate(lists):  # for i in range(len(lists)):
        if lists[i][1] < 12 and lists[i][2] < 12:
            LOGGER.warning("There might be an ambiguity between  "
                           "month: %d and date:%d", lists[i][2], lists[i][1])


def main():
    """ Main function """
    fmts = ('%d-%m-%y', '%d-%m-%Y', '%m-%d-%Y', '%m-%d-%y', '%y-%m-%d',
            '%Y-%m-%d', '%Y-%d-%m', '%y-%d-%m', '%b-%d-%Y',
            '%b-%d-%y', '%B-%d-%Y', '%B-%d-%y', '%d-%b-%Y', '%d-%b-%y', '%d-%B-%Y', '%d-%B-%y')
    args = arg_parse()
    setup_logging()
    dir_path = Path.cwd() / args.d
    if dir_path.is_dir():
        os.chdir(dir_path)
        csv_files, csv_files_str = get_csv_files(Path.cwd())
        file_names = get_file_names(csv_files)

        cr_dates = clear_repetition(file_names)
        final_dates = check_proper_dates(cr_dates)
        file_dates = is_date(final_dates, fmts)
        unique_dates = unique(file_dates)
        create_directory(unique_dates)
        copy_files(csv_files_str, fmts, unique_dates)
        ambiguity(unique_dates)
    else:
        LOGGER.error("The directory doesnt exist")
        print(dir_path)


if __name__ == '__main__':
    main()
