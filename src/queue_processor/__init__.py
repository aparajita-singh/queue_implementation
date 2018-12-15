from src import utils, file_dao, logger
import time


def convert_csv_row_to_dict(row, all_tasks, start_time):
    current_time = utils.standardize_date(utils.dequotify(row[' time_to_expire ']))
    current_time = current_time if utils.get_date(current_time) >= utils.get_date(start_time) else start_time
    if current_time in all_tasks.keys():
        priority = int(row[' priority'].strip()) if row[' priority'] is not None else len(all_tasks[current_time])
        all_tasks[current_time].insert(priority - 1, row['event_name'])
    else:
        all_tasks[current_time] = list([row['event_name']])
    return all_tasks


def do_task(start_time, task):
    logger.log('Current time [ {0} ] , Event "{1}" Processed'
          .format(start_time, task))


def process_one_task_group(input_tasks):
    [do_task(input_tasks['start_time'], one_task) for one_task in input_tasks['input_data'][input_tasks['start_time']]]


def process(input_args):
    logger.log('received {} input arguments: {}'.format(len(input_args), input_args))
    input_args['input_data'] = file_dao.read_csv_file_as_custom_dict(input_args['filename'], convert_csv_row_to_dict,
                                                                     input_args['start_time'])
    logger.log(input_args['input_data'])

    while True:
        process_one_task_group(input_args) if input_args['start_time'] in input_args['input_data'] else None
        input_args['input_data'].pop(input_args['start_time'], None)
        input_args['start_time'] = str(utils.increment_time_by_minutes(input_args['start_time'], 1))
        if len(input_args['input_data']) <= 0:
            break
        logger.log('sleeping 1 minute')
        time.sleep(60)
