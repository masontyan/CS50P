def main():
    normal = input("Input: ")
    print("Output: ", end="")
    twitter(normal)
    print()


def twitter(normal):
    for letter in normal:
        if (
            letter == "a"
            or letter == "e"
            or letter == "i"
            or letter == "o"
            or letter == "u"
            or letter == "A"
            or letter == "E"
            or letter == "I"
            or letter == "O"
            or letter == "U"
        ):
            print("", end="")
        else:
            print(f"{letter}", end="")

main()

#best answer:
# def main():
#     text = input("Input: ")
#     output = ""

#     for letter in text:
#         if letter.lower() not in "aeiou":
#             output += letter

#     print("Output:", output)

# main()
