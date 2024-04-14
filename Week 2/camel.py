def main():
    name = input("camelCase:").strip()
    result = convert(name)
    print(result)

def convert(name):
    for i in name:
        if i.isupper():
            lowerCase = i.lower()
            name = name.replace(i ,"_"+lowerCase)
    return name

main()
