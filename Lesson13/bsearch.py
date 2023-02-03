import math
list1=[1,2,3,4,5,7,23,43,46,89,100,120,345,456,]
def bsearch( searched_list, searching_value):

    mid= math.floor(len(searched_list)/2)
    # print(len(searched_list)/2)
    # print(mid)
    # print(searched_list)
    if searching_value==searched_list[mid]:
        # return f'serched_value == {searched_list[mid]}'
        return True

    elif searching_value < searched_list[mid] and len(searched_list)>1:
        return bsearch(searched_list[0:mid],searching_value)
    elif searching_value > searched_list[mid] and len(searched_list)>1:
        return bsearch(searched_list[mid:],searching_value)
    else:
        return False
print(bsearch(list1,500))