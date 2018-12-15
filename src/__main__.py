# this is the starting point for the program
import sys

from src import utils, queue_processor, logger


def get_input(input_args):
    if len(input_args) != 3:
        return None
    else:
        return {'filename': input_args[1], 'start_time': utils.standardize_date(input_args[2])}


if __name__ == '__main__':
    input_dict = get_input(sys.argv)
    if input_dict is None:
        logger.log('Provide 2 input arguments in this format: <input-file-name> <start-time>')
    else:
        queue_processor.process(input_dict)
