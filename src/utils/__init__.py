from datetime import datetime, timedelta as timedelta

TIME_FORMAT = '%Y/%m/%d %H:%M'


def standardize_date(raw_data):
    return datetime.strftime(datetime.strptime(raw_data.strip(), TIME_FORMAT), TIME_FORMAT)


def dequotify(value):
    return ''.join(value.split('"'))


def get_date(time_string):
    return datetime.strptime(time_string, TIME_FORMAT)


def increment_time_by_minutes(time, minutes):
    return datetime.strftime(
            datetime.strptime(time, '%Y/%m/%d %H:%M') + timedelta(minutes=minutes), '%Y/%m/%d %H:%M')
