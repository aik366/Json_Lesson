import json
import pprint


def read_json(filename):
    with open(filename, encoding='utf-8') as file:
        return json.load(file)


def write_json(filename, an_object):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(an_object, file, ensure_ascii=False, indent=2)


# print(read_json_file('data/user.json'))
my_dict = {"a": 1, "b": 2, "c": 3}
write_json('data/test.json', read_json('data/user.json'))

# for key, vol in read_json('data/test.json').items():
#     print(f"{key}: скидка = {vol['discount']}, телефон = {vol['phone']}")

for key, vol in read_json('data/test.json').items():
    if vol['discount'] > 0:
        print(f"{key}: скидка = {vol['discount']}, телефон = {vol['phone']}")
