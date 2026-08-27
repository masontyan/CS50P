answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")

# cleanest answer v (i did not learn about in yet)

# answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

#if answer in {"42", "forty-two", "forty two"}:
#    print("Yes")
#else:
#    print("No")