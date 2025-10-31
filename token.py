input = "hello world!"

def tokenize(text):
    return [ord(char) for char in text]

print(tokenize(input))


def tokenizeutf(text):
    return list(text.encode('utf-8'))

print(tokenizeutf(input))