
def func(a, b, *args, option = False, **kwargs):
    print(a, b)
    print(args)
    print(option)
    print(kwargs)

func(1, 3, 10, 20, Name = 'Tom', Salary = 60000)