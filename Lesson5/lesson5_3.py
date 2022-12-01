dic1={}
list1=[1,2,3,4,5,6,7,1,2,3,4,3,2,1,2,3,4,3,2,1,2,3,4,45,5,4,3,3]
for val in list1:
    if val in dic1.keys():
        dic1[val]+=1
    else:
        dic1[val]=1
for item in dic1.items():
    print(item)