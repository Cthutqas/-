def print_params(a=1, b='Сергей', c=True):
    print(a, b, c)

print_params()
print_params(c = [1,2,3])
print_params(b = 25)

values_list = [1, 'Сергей', (1, 2, 3)]
print_params(*values_list)

values_dict = {'a': 1, 'b': 'Сергей', 'c': True}
print_params(**values_dict)

values_list_2 = [123, 'Сергей']
print_params(*values_list_2, 42)



