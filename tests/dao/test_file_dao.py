from src.file_dao import __init__ as file_dao


def do_nothing(x=None, y=None):
    return x


def test_read_csv_file():
    sample_data = {
        'header': 'some test data',
        'something': 'more test'
    }
    assert file_dao.read_csv_file_as_custom_dict(
        '/home/broken-compass/PycharmProjects/QueueImplementation/src/data/test.csv', do_nothing) == sample_data
