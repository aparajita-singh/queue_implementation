import pytest

import src.queue_processor as queue_processor
from collections import OrderedDict


def test_convert_csv_row_to_dict():
    sample_data = {
        ' time_to_expire ': '"2017/02/10 5:00"',
        ' priority': 1,
        'event_name': 'x'
    }
    sample_dict = {
        '2017/02/10 05:00': ['x']
    }
    sample_row = OrderedDict(sample_data)
    assert sample_dict == queue_processor.convert_csv_row_to_dict(sample_row, {})


def test_negative_convert_csv_to_dict():
    error_data = {
        'x': 'y'
    }
    error_dict = {
        'x': 'y'
    }
    with pytest.raises(KeyError) as ke:
        assert error_dict == queue_processor.convert_csv_row_to_dict(OrderedDict(error_data), {})


def test_do_task(capsys):
    queue_processor.do_task('sample', 'task')
    captured = capsys.readouterr()
    assert captured.out == 'Current time [ sample ] , Event "task" Processed\n'


def test_process_one_task_group(capsys):
    sample_tasks = {
        'start_time': 'time',
        'input_data': {
            'time': ['x', 'y']
        }
    }
    queue_processor.process_one_task_group(sample_tasks)
    captured = capsys.readouterr()
    assert captured.out == 'Current time [ time ] , Event "x" Processed\nCurrent time [ time ] , Event "y" Processed\n'
