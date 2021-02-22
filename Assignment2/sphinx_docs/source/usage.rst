===========================================
Welcome to Assignment 2 usage documentation
===========================================

Problem Statement
-----------------
You are working on a project where a client has given you a directory with a whole
bunch of csv/txt/pdf files. The client tells you that the csv files are the ones that
contain the data and there are multiple csv files for each date. The csv files of the
same date need to be grouped together into a single directory before further
analyses could be performed. The client also tells you that the date format for each
data-dump he/she is about to give you can change across each data-dump.
Your task now is to :

* Write a program which would perform the given task

Input to the program:
----------------------
The command line takes 1 input:

* The directory name in which the data dump is present.

It can be found by typing the following in the Terminal:


.. code-block::

    check_csv.py -h

for which we get:

.. code-block::

    usage: check_csv.py [-h] d

    positional arguments:
    d           enter the directory name


Inside the program:
-------------------
when the directory name is given, the program checks if the directory is present. Else it throws:

.. code-block::

     [ERROR] - [root] : The directory doesnt exist

The program iterates through the entire directory and when the csv files are found we get:

.. code-block::

      [INFO] - [root] : CSV files are found

While parsing through the filenames obtained the date, if there's any date that doesnt match the formats, we get:

.. code-block::

      [WARNING] - [root] : Date is not according to the format.

Directories are created using parsed dates.

.. code-block::

      [INFO] - [root] : Directories are created

And the csv files are copied to the appropriate folders

.. code-block::

      [INFO] - [root] : Files are copied

Output
-------

The csv files are segregated according to the dates in each folder. When given 'dir' command in terminal, we get all
the files and directories in the data dump. Inside the data dump folder, we have the csv files.

.. code-block::

   dir

.. code-block::

       ...
       17-02-2021  14:54                 3 17_feb_2021_3.pdf
       17-02-2021  14:54                 2 17_feb_2021_3.txt
       19-02-2021  17:05    <DIR>          2021-02-17

.. code-block::


   19-02-2021  17:05                 2 02_17_2021_1.csv
   19-02-2021  17:05                 2 02_17_2021_2.csv
   19-02-2021  17:05                 2 02_17_2021_3.csv
   19-02-2021  17:05                 2 17_feb_2021_1.csv
   19-02-2021  17:05                 2 17_feb_2021_2.csv
   19-02-2021  17:05                 2 17_feb_2021_3.csv

