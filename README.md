# Queue Implementation
Schedules events in a queue based on start time for the event and the priority

## Code structure
The starting point of the program is __\_\_main__.py in src folder.
The main thread invokes the queue processor which reads the input file, parses the contents and executes the tasks when the current time reaches the time specified against the task in the input file. If a priority is specified for the tasks, the tasks will be executed in that order.
The __file_dao__ package is meant for performing file operations. Currently, it only has a function to read a file and return the contents as a python dictionary when the full path of the file is given as input. 
The __utils__ package is meant for performing trivial operations that do not directly involve any functional/business logic. Currently, it contains functions for doing data type manipulations, such as converting a string to date.
The __logger__ package is meant for writing logs to the desired log store. Currently, it immediately outputs logs to console output.

## Sample runs:
### 1. File containing 3 inputs. One with start time after one minute, two with same start time of which one has higher priority

input>> python3 -m src data/input.csv "2017/12/10 4:59"

output>> 
received 2 input arguments: {'filename': 'src/data/input.csv', 'start_time': '2017/02/10 04:59'}
{'2017/02/10 05:01': ['Task_#501'], '2017/02/10 05:00': ['Task_#502', 'Task_#500']}

sleeping 1 minute

Current time [ 2017/02/10 05:00 ] , Event "Task_#502" Processed

Current time [ 2017/02/10 05:00 ] , Event "Task_#500" Processed

sleeping 1 minute

Current time [ 2017/02/10 05:01 ] , Event "Task_#501" Processed

###2. Input file containing tasks with start time in the past

input>> python3 -u -m src src/data/input.csv "2017/12/10 6:00"

output>> 
received 2 input arguments: {'filename': 'src/data/input.csv', 'start_time': '2017/02/10 05:59'}

{'2017/02/10 05:59': ['Task_#502', 'Task_#500', 'Task_#501']}

Current time [ 2017/02/10 05:59 ] , Event "Task_#502" Processed

Current time [ 2017/02/10 05:59 ] , Event "Task_#500" Processed

Current time [ 2017/02/10 05:59 ] , Event "Task_#501" Processed

