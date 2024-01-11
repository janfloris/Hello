def example_function(it):
    for key, value in it.items():
        print(f"{key}: {value}")

# Using double asterisks to unpack a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
example_function(my_dict)
