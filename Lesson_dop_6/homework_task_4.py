"""
Изменить реализацию функции рекурсивного поиска элемента в словаре (из предыдущего задания)
следующим образом:
- функция должна находить ПЕРВОЕ соответствие имени и возвращать результат в виде словаря:

    {'val': found_value, 'parent': found_value_parent, 'deep': found_value_deep}

"""


def recursive_search(src, value, deep=-1, parent=None):
    if isinstance(src, str):
        if src == value:
            print(f"{value} is found! Deep={deep}, Parent={parent}")
            dict1 = {'val': value, 'parent': parent, 'deep': deep}
            return dict1

    elif isinstance(src, dict):
        for k, v in src.items():
            # print(src)
            res = recursive_search(v, value, deep=deep + 1, parent=k)
            if res is not None:  # Нужно пояснение
                return res
    elif isinstance(src, list):
        for l in src:
            # print(src)
            res = recursive_search(l, value, deep=deep, parent=parent)
            if res is not None:
                return res


""" Source dict """


def get_source_dict():
    return {
        "key1": "John",  # deep 0
        'key2': {
            'key3': 'Alex',  # deep 1
            'key4': {
                'key5': ['Kate', 'Mary', 'Mark'],  # deep 2
                'key6': {
                    'key7': [
                        'Bob',  # deep 3
                        'Duke',
                        {
                            'key8': {  # deep 4
                                'key9': [  # deep 5
                                    'Lisa',
                                    {
                                        'key10': ['Mark', 'Alex']  # deep 6
                                    }
                                ]
                            }
                        }
                    ]
                },
            },
            'key8': 'Robert'  # deep 1
        }
    }


""" Test """
source_dict = get_source_dict()
values = [
    ("Alex", {'val': 'Alex', 'parent': 'key3', 'deep': 1}),
    ("Mary", {'val': 'Mary', 'parent': 'key5', 'deep': 2}),
    ('Duke', {'val': 'Duke', 'parent': 'key7', 'deep': 3}),
    ('Mark', {'val': 'Mark', 'parent': 'key10', 'deep': 6})
]

for lookup_value, expected_result in values:
    result = recursive_search(source_dict, lookup_value)
    assert result == expected_result, f"{result} != {expected_result}"
