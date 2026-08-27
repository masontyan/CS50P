def main():
    value = input("What time is it? ")
    meal = convert(value)

    if  7 <= meal <= 8:
        print("breakfast time")
    elif 12 <= meal <= 13:
        print ("lunch time")
    elif 18 <= meal <= 19:
        print ("dinner time")

def convert(number):
    number = number.strip(" ").replace(":", " ")

    if (number).endswith('a.m.'):
        x, y = (number).strip('a.m.',).strip(' ').split(' ')
        h = int(x)
        m = float(int(y) / 60)
        value = h + m
        return value
    elif (number).endswith('p.m.'):
        x, y = (number).strip('p.m.',).strip(' ').split(' ')
        h = int(x)
        m = float(int(y) / 60)
        value = h + m + 12
        return value
    elif (number):
        x, y = (number).strip(' ').split(' ')
        h = int(x)
        m = float(int(y) / 60)
        value = h + m
        return value 

if __name__ == "__main__":
    main()

# cleanest answer v

#def main():
#    meal = convert(input("What time is it? "))
#
#    if 7 <= meal <= 8:
#        print("breakfast time")
#    elif 12 <= meal <= 13:
#        print("lunch time")
#    elif 18 <= meal <= 19:
#        print("dinner time")


#def convert(time):
#    time = time.strip()

#    is_am = time.endswith("a.m.")
#    is_pm = time.endswith("p.m.")

#    if is_am:
#        time = time.removesuffix("a.m.").strip()
#    elif is_pm:
#        time = time.removesuffix("p.m.").strip()

#    hours, minutes = time.split(":")
#    hours = int(hours)
#    minutes = int(minutes)

#    if is_am and hours == 12:
#        hours = 0
#    elif is_pm and hours != 12:
#        hours += 12

#   return hours + minutes / 60


#if __name__ == "__main__":
#    main()
