def decrypt_caesar(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        c = ord(ciphertext[i])
        if c >= ord("A") and c <= ord("Z"):
            plaintext += chr((c - ord("A") - key) % 26 + ord("A"))
        elif c >= ord("a") and c <= ord("z"):
            plaintext += chr((c - ord("a") - key) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]
    return plaintext


for i in range(int(input())):
    s = input()
    key = int(input())
    print(decrypt_caesar(s, key))
