from setuptools import setup

setup(
    name='QueueImplementation',
    version='1',
    packages=['utils', 'queue_processor', 'file_dao', 'logger'],
    package_dir={'': 'src'},
    url='https://github.com/aparajita-singh/queue_implementation',
    license='',
    author='Aparajita Singh',
    author_email='aparajita.1194@gmail.com',
    description='Schedules events in a queue based on start time for the event and the priority'
)
