input = "hello world!"

def tokenize(text):
    return [ord(char) for char in text]


print(tokenize(input))
