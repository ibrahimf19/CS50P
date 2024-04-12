def main():
    expression = input("Expression: ")
    x, y, z = expression.split(" ")
    result = checkOperator(x,y,z)
    print(result)

def checkOperator(x,y,z):
    if y == "+":
        result = float(x)+float(z)
        return result
    if y == "*":
        result = float(x)*float(z)
        return result
    if y == "/":
        result = float(x)/float(z)
        return result
    if y == "-":
        result = float(x)-float(z)
        return result

main()
