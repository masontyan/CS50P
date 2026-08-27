expression = input("Expression: ").strip(' ')

a, y, c = expression.split(' ')

x = float(int(a))
z = float(int(c))

if (y) == ('+'):
    print((x + z))
elif (y) == ('-'):
    print((x - z))
elif (y) == ('*'):
    print((x * z))
else:
    print((x / z))

# cleanest answer v

#expression = input("Expression: ").strip()

#x, y, z = expression.split(" ")

#x = int(x)
#z = int(z)

#if y == "+":
#    answer = x + z
#elif y == "-":
#    answer = x - z
#elif y == "*":
#    answer = x * z
#else:
#    answer = x / z

#print(f"{answer:.1f}")





