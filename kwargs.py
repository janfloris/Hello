def example_function(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Using double asterisks to unpack a dictionary
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
example_function(**my_dict)
