
# Program for printing all the strings passed to the function
def func(a,*args):
    print("Value of a is:", a)
    for i in args:
        print(f' args are -> {i} ')

func('Hey', 'How', 'are', 'you?')