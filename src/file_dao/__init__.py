import csv


def read_csv_file_as_custom_dict(filename, conversion_function, params):
    with open(filename, 'rt') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect='excel')
        converted_data = {}
        for row in csv_reader:
            temp = conversion_function(row, converted_data, params)
            converted_data = {**converted_data, **temp}
        return converted_data
