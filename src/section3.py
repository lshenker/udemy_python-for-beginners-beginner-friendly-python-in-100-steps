
# function names in python must start with [ a-z | A-Z | _ ] and cannot be keywords
# the return keyword returns values in functions

# print with seperator
print('a', 'b', 'c', sep='-')

# print without newline
print('.', end='') 

def print_squares_of_numbers(n):
    for i in range(1, n):
        print(f"{i} squared is {pow(i,2)}")
print_squares_of_numbers(20)

def print_multiplication_table(table, start=1, end=10):
    for i in range(start, end+1):
        print(f"{table} * {i} = {table * i}")
print_multiplication_table(5)

def sum_of_three_integers(n1, n2, n3):
    return n1+n2+n3
print(sum_of_three_integers(2, 3, 5))

def get_third_angle_of_triangle(a1, a2):
    return 180-a1-a2
print(get_third_angle_of_triangle(67, 31))
