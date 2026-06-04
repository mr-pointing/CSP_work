sub_dict = {
    "A": "D",
    "B": "E",
    "C": "F",
    "D": "G",
    "E": "H",
    "F": "I",
    "G": "J",
    "H": "K",
    "I": "L",
    "J": "M",
    "K": "N",
    "L": "O",
    "M": "P",
    "N": "Q",
    "O": "R",
    "P": "S",
    "Q": "T",
    "R": "U",
    "S": "V",
    "T": "W",
    "U": "X",
    "V": "Y",
    "W": "Z",
    "X": "A",
    "Y": "B",
    "Z": "C"
}
symbols = ["!", ",", ".", "/", "(", ")", "{", "}",
           "?", "#", "@", "$", "%", "^", "&", "*",
           "-", "_", "+", "=", "|", " ", "\""]


def encrypt(word):
    encrypted = ""
    for w in word:
        if w.upper() in sub_dict:
            if w.isupper():
                encrypted += sub_dict[w.upper()].upper()
            else:
                encrypted += sub_dict[w.upper()].lower()
        elif w in symbols:
            encrypted += w
    return encrypted


def decrypt(word):
    decrypted = ""
    for w in word:
        new_letter = decrypt_char(w)
        decrypted += new_letter
    return decrypted


def decrypt_char(letter):
    for key, value in sub_dict.items():
        if letter.upper() == value:
            if letter.isupper():
                return key
            else:
                return key.lower()
    else:
        return letter


user_word = input("Enter a word: ")
new = encrypt(user_word)
print(new)
old = decrypt(new)
print(old)
