def main():

    groceries = {}

    while True:
        try:
            item = input()
        except EOFError:
            break

        if item in groceries:
            groceries[item] =+ 1
        else:
            groceries[item] = 1

    for item in groceries:
        print(groceries[item])

main()
