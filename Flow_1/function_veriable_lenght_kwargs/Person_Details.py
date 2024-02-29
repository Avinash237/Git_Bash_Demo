
# Print values of function Person along with its associated keywords
def Person(**kwargs):
    for key, value in kwargs.items():
        print("{} -> {}".format(key, value))    # OR print(f'{key} -> {value}')

Person(Name = 'Sean', Sex = 'Male', Age = 38, City = 'London', Mobile = 9375821987)