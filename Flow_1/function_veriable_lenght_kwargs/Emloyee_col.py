def Employee(**kwargs):
    for i in kwargs:
        print(i)


Employee(emp="Jim", salary=9000, age=34)