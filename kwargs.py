def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

def kwarg_multiple(**kwargs):
    if 'name' in kwargs:
        print(f"Name is {kwargs['name']}")
    else:
        print("Name is not provided")

    if 'city' in kwargs:
        print(f"City is {kwargs['city']}")
    else: 
        print("City is not provided")

# Using double asterisks to unpack a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
# example_function(**my_dict)

kwarg_multiple(name='John', age=25, city='New York')
