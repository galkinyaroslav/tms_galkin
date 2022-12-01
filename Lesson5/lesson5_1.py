dict_1={
    'key1': 1,
    'key2': 2,
    'key3': 3,
    'key4': 4,
    'key5': 5,
}
dict_2={val:key for key,val in dict_1.items()}
print(dict_2)