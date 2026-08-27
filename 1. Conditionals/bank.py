greet = input("Greeting: ").strip()

if (greet).startswith(('Hello', 'hello')):
    print("$0")
elif (greet).startswith(('H', 'h')):
    print("$20")
else:
    print("$100")

# cleanest answer v (converted everything into lower so that if only needs to check "hello" rather than lower and uppercase capitalization)

#greet = input("Greeting: ").strip().lower()

#if greet.startswith("hello"):
#    print("$0")
#elif greet.startswith("h"):
#    print("$20")
#else:
#    print("$100")