def main():
    while True:
        try:
            date = input("Date: ")

            months = [
                "January",
                "February",
                "March",
                "April",
                "May",
                "June",
                "July",
                "August",
                "September",
                "October",
                "November",
                "December"
                        ]

            if "/" in date:
                month, day, year = date.split("/") #but you also need to know how to get the other format of valid input...

                month = int(month)
                day = int(day)
                year = int(year)

            elif "," in date:

                month, day, year = date.split()

                month = int(months.index(month) +1)
                day = int(day.strip(","))
                year = int(year)

            elif "/" or "," not in date:
                continue

            if not 1 <= month <= 12:
                continue
            if not 1 <= day <= 31:
                continue
        except ValueError:
                continue

        if month < 10:
            month = f"0{month}"
        if day < 10:
            day = f"0{day}"
        print(f"{year}-{month}-{day}")
        break

main()


# def main():
#     months = [
#         "January",
#         "February",
#         "March",
#         "April",
#         "May",
#         "June",
#         "July",
#         "August",
#         "September",
#         "October",
#         "November",
#         "December"
#     ]

#     while True:
#         try:
#             date = input("Date: ")

#             if "/" in date:
#                 month, day, year = date.split("/")
#                 month = int(month)
#                 day = int(day)
#                 year = int(year)

#             elif "," in date:
#                 month, day, year = date.split()
#                 month = months.index(month) + 1
#                 day = int(day.strip(","))
#                 year = int(year)

#             else:
#                 continue

#             if 1 <= month <= 12 and 1 <= day <= 31:
#                 break

#         except (ValueError, IndexError):
#             continue

#     print(f"{year:04}-{month:02}-{day:02}")


# main()
