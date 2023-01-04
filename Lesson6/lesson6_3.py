import json
dict1={
    111111: ('masha', 11),
    222222: ('tanya', 22),
    333333: ('olga', 33),
    444444: ('natasha', 44),
    555555: ('xenia', 55),
    666666: ('marina', 66),
}
with open('less6_3.json','w') as file:
    json.dump(dict1,file)