import os
import re
import datetime


def get_date_from_filename(filename):
    # return date from filename, if nothing found return ''
    date_regexp_1 = re.compile(r'(201\d-\d{2})-\d{2}')
    date_regexp_2 = re.compile(r'(201\d{3})\d{2}')
    res = re.search(date_regexp_1, filename)
    if res is None:
        res = re.search(date_regexp_2, filename)
    if res is None:
        return ''
    return res.group(0)


def get_year_from_date(date):
    # return year. Here year is always at a begining
    return date[:4]


def get_month_from_date(date):
    # return month
    date_regexp_1 = re.compile(r'(201\d-\d{2})-\d{2}')
    if re.match(date_regexp_1, date) is None:
        return date[4:6]
    return date[5:7]


def get_created_date(path):
    # return creation date from file properties
    ts = os.path.getctime(path)
    return datetime.datetime.fromtimestamp(ts)


def create_dir_ifnoexists(path):
    # create new folder if no exists
    if not os.path.exists(path):
        os.makedirs(path)
    return 0


def get_year_and_month(path):
    # get year and month from file. First try from name, if can't get from properties
    date = get_date_from_filename(path)
    if date == '':
        date = get_created_date(path)
    year = get_year_from_date(str(date))
    month = get_month_from_date(str(date))
    return year, month


def replace_file(source_dir, destination_dir, file):
    # create directory and replace file there
    create_dir_ifnoexists(destination_dir)
    old_path = os.path.join(source_dir, file)
    new_path = os.path.join(destination_dir, file)
    os.rename(old_path, new_path)
    return 0


source_dir = 'Z:\_0_PAVEL_MATVEEVICH\Photos'
# source_dir = r'C:\temp\photos'

for file in os.listdir(source_dir):
    year, month = get_year_and_month(os.path.join(source_dir, file))
    destination_dir = os.path.join(source_dir, year, month)
    replace_file(source_dir, destination_dir, file)
    print(' '.join((file, destination_dir)))
