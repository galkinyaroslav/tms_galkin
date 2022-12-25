import json
import csv

with open('less6_3.json','r') as file:
    data=json.load(file)
    print(data)
    with open('less6_4.csv','w')as csvfile:
        writer_obj = csv.writer(csvfile, delimiter=',')
        writer_obj.writerow(['id','name','age', 'phone'])
        for key, val in data.items():
            str_to_write=key,val[0],val[1],f'+375290{key}'
            writer_obj.writerow(str_to_write)