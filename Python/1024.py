def encrypt(text):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + 3 - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + 3 - 97) % 26 + 97)
        else:
            result += char
    return result[::-1]


text = input()
print(encrypt(text))

# TODO: Need sum adjustments
