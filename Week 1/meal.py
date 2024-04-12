def main():
    time = input("What time is it? ")
    result = convert(time)
    if result >= 7.00 and result <=8.00:
        print("breakfast time")
    elif result >= 12.00 and result <=13.00:
        print("lunch time")
    elif result >= 18.00 and result <=19.00:
        print("dinner time")


def convert(time):
    h,m = time.split(":")
    m=float(m)
    m = m/60
    time = float(h) + m
    return(time)


if __name__ == "__main__":
    main()
