### chap16/dyntype.py

choice = input('Pick an object type: ')
my_variable = 'A'             # default to str
if choice == 'int':
    my_variable = 65          # change to int
elif choice == 'list':
    my_variable = ['A', 65]   # change to list
print(my_variable, 'is of type', type(my_variable))
