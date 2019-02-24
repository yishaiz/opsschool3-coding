import json

from file_reader import read_file
from file_writer import write_result_to_file


def get_file_name_from_user():
    print("please write file name")
    file_name = input()
    return file_name


def get_buckets(data_json):
    return data_json['buckets']


def get_ordered_buckets(data_json):
    buckets = get_buckets(data_json)
    buckets.sort()
    return buckets


def get_bucket_limits(buckets):
    bucket_limits = []

    previous = 0

    for item in buckets:
        bucket_limits.append({'min': previous, 'max': item, 'names': []})
        previous = item

    bucket_limits.append({'min': previous, 'max': None, 'names': []})

    return bucket_limits


def group_json_to_buckets(data_json, buckets):
    bucket_limits = get_bucket_limits(buckets)

    for name, age in data_json.items():
        for limit in bucket_limits:
            if age >= limit['min'] and (limit['max'] is None or age < limit['max']):
                limit['names'].append(name)

    return bucket_limits


def get_result_file_name(file_name):
    arr = file_name.split('.')
    arr[-1] = 'yaml'
    new_file_name = '.'.join(arr)
    return new_file_name


def get_result_in_yaml_format(groups):
    result = '--- \n'

    for group in groups:
        if group['min'] == 0 or group['max'] is None:
            continue

        result += '{}-{}:\n'.format(group['min'], group['max'])

        for item in group['names']:
            result += '-  :s{}\n'.format(item)

    result += 'other : # (<min or > max):\n'

    for item in groups[0]['names']:
        result += '-  :s{}\n'.format(item)

    for item in groups[-1]['names']:
        result += '-  :s{}\n'.format(item)

    result += '\n\n'

    return result


def write_groups_to_file(file_name, groups):
    result_file_name = get_result_file_name(file_name)
    yaml_format = get_result_in_yaml_format(groups)
    write_result_to_file(result_file_name, yaml_format)


def group_names_by_age():
    file_name = get_file_name_from_user()

    file_content = read_file(file_name)
    data_json = json.loads(file_content)

    buckets = get_ordered_buckets(data_json)

    groups = group_json_to_buckets(data_json['ppl_ages'], buckets)

    write_groups_to_file(file_name, groups)


def main():
    try:
        group_names_by_age()

        print('done.')

    except Exception as ex:
        print("There is an error. {0}".format(ex))


if __name__ == '__main__':
    main()
