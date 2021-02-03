class MySecret:
    key = 129

    def encode(self, plain_text):
        result = ''
        for letter in plain_text:
            result += chr(ord(letter) ^ self.key)
        return result

    def decode(self, encoded_text):
        result = ''
        for letter in encoded_text:
            result += chr(ord(letter) ^ self.key)
        return result