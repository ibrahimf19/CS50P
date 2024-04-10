def convertSmile(prompt):
    return prompt.replace(":)","🙂",)

def convertFrown(prompt):
    return prompt.replace(":(","🙁",)

def main():
    prompt = input()
    prompt = convertSmile(prompt)
    prompt = convertFrown(prompt)
    print(prompt)
main()

