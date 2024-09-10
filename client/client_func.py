import json


def check_client(e, en_name, cbox_name):
    with open('../data/user.json', 'r', encoding='UTF-8') as file:
        json_user = json.load(file)
    typed = en_name.get()
    if typed == '':
        data = []
    elif len(typed) == 1:
        data = []
        for item in json_user.keys():
            if typed.lower() == item.lower()[0]:
                data.append(item)
    elif len(typed) == 2:
        data = []
        for item in json_user.keys():
            if typed.lower() == item.lower()[:2]:
                data.append(item)
    else:
        data = []
        for item in json_user.keys():
            if typed.lower()[0] == item.lower()[0] and typed.lower() in item.lower():
                data.append(item)
    cbox_name.configure(values=data)
