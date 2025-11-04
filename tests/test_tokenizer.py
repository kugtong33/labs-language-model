import unittest
from libs.tokenize import tokenize

class Tokenizer(unittest.TestCase):
    def test_tokenize(self):
        input = "hello world!"
        output = tokenize(input)

        print(output)
        assert output == [104, 101, 108, 108, 111, 32, 119, 111, 114, 108, 100, 33]
