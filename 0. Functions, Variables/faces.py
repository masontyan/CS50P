def main():
    camera = input("you're on camera! ")
    print(convert(camera))

def convert(text):
    return(text).replace(':)', '🙂').replace(':(', '🙁')

main()

# cleanest answer v
# def main():
#     text = input()
#     print(convert(text))

# def convert(text):
#     return text.replace(":)", "🙂").replace(":(", "🙁")

# main()