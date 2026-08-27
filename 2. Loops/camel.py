def main():
    camelCase = input("camelCase: ").strip()
    print("snake_case: ", end="")
    snake_case(camelCase)

def snake_case(camelCase):
    for letter in camelCase:
            if (letter).isupper():
                print(f"_{(letter).lower()}", end="")
            else:
                print(f"{letter}", end="")
main()

# cleanest answer v

# def main():
#     camel_case = input("camelCase: ").strip()
#     print("snake_case:", convert(camel_case))


# def convert(camel_case):
#     snake_case = ""

#     for letter in camel_case:
#         if letter.isupper():
#             snake_case += "_" + letter.lower()
#         else:
#             snake_case += letter

#     return snake_case

# main()
