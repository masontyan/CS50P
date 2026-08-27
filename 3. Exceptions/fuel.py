while True:
    try:

        fraction = (input("Fraction: "))

        numerator, denominator = fraction.split("/")

        x = int(numerator)
        y = int(denominator)

        if x > y:
            continue
        elif x < 0 or y < 0:
            continue

        answer = (x / y)*100

        if answer <= 1:
            print("E")
        elif answer >= 99:
            print("F")
        else:
            print(f"{answer:.0f}%")

    except ValueError:
            continue
    except ZeroDivisionError:
        continue
    break

# def main():
#     while True:
#         try:
#             fraction = input("Fraction: ")
#             x, y = fraction.split("/")

#             x = int(x)
#             y = int(y)

#             if x < 0 or y <= 0 or x > y:
#                 continue

#             percentage = (x / y) * 100
#             break

#         except ValueError:
#             continue
#         except ZeroDivisionError:
#             continue

#     if percentage <= 1:
#         print("E")
#     elif percentage >= 99:
#         print("F")
#     else:
#         print(f"{percentage:.0f}%")


# main()
