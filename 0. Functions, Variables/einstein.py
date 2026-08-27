mass = int(input("what is mass?"))

def square(n):
    return pow(n, 2)

energy = mass * square(300000000)

print(f"{energy:,}")

# cleanest answer v

# mass = int(input("What is mass? "))

# c = 300000000
# energy = mass * c ** 2

# print(energy)


