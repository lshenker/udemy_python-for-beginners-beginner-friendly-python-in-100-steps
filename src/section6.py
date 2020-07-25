
# no primitive data types in Python, every variable is an object of a class

# int
print(type(5))
# float
print(type(2.5))
# str
print(type("text"))
# bool
print(type(True))

def calculate_simple_interest(principal, interest, duration):
    return principal * (1 + interest * 0.01 * duration)
print(calculate_simple_interest(10000, 2, 10))


# no i++ or ++i in python
i = 2; i += 1; print(i)

# drop decimal remainder
i //= 2; print(i)
# or use int()
print(int(3/2))

# round() to 3 decimal places
print(round(10/3, 3))

print(1 < 0)


# conditions
i = 4
if i<5:
    print(f"{i} is less than 5")
elif i > 5:
    print(f"{i} is greater than 5")
else:
    print(f"{i} is equal to 5")

# Logical operators
# and
# or
# not
# ^  exclusive or

i = 11
j = 16
if i%2==0 and j%2==0:
    print("i and j are even")

if not i==10:
    print("i is not 10")
if i != 10:
    print("i is not 10!")

# IMPORTANT: anything not 0 == True






















