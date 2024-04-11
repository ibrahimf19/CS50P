def main():
    answer = input("What is the answer to The Great Question of Life?").lower().strip()
    check(answer)
    print(check(answer))

def check(n):
    if(n=="forty-two" or n=="forty two" or n=="42"):
        return("Yes")
    else:
        return("No")

main()
