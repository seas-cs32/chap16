### chap16/equal.py

a_letter = 'A'
an_int = 65

# Show that their bit patterns match
a_in_bits = bin(ord(a_letter))
i_in_bits = bin(an_int)
print(a_in_bits, i_in_bits)

print(f'Does Python think these two objects are equal? {a_letter == an_int}')

print(f'{a_letter} is of type {type(a_letter)}')
print(f'{an_int} is of type {type(an_int)}')
