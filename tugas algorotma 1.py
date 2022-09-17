def bank():
    Greetings = input("Greetings = ").strip().lower()
    if Greetings.startswith("hello") or Greetings == ("hello, newman"):
        return 0
    elif Greetings.startswith("h"):
        return 20
    else:
        return 100

for i in range(5):
    print("$",bank())