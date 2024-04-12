def main():
    fileName = input("What is the name of the file: ").lower().strip()
    result = check(fileName)
    print(result)

def check(f):
    if f.endswith("gif"):
        return("image/gif")
    elif f.endswith("jpeg") or f.endswith("jpg"):
        return("image/jpeg")
    elif f.endswith("png"):
        return("image/png")
    elif f.endswith("pdf"):
        return("application/pdf")
    elif f.endswith("txt"):
        return("text/plain")
    elif f.endswith("zip"):
        return("application/zip")
    else:
        return("application/octet-stream")

main()
