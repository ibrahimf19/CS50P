def main():
    greeting = input("Greet me ").lower().strip()
    result = check(greeting)
    print(result)

def check(greeting):
    if greeting.startswith("hello"):
        return("$0")
    elif greeting.startswith("h"):
        return("$20")
    else:
        return("$100")

main()
