from datetime import datetime

TIME_FORMAT = '%Y/%m/%d %H:%M'


def standardize_date(raw_data):
    return datetime.strftime(datetime.strptime(raw_data.strip(), TIME_FORMAT), TIME_FORMAT)


def dequotify(value):
    return ''.join(value.split('"'))


def get_date(time_string):
    return datetime.strptime(time_string, TIME_FORMAT)
