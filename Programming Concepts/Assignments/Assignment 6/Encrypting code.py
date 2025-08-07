# UID: U72087839
# Name: Claude Watson
# Description: To read a file and create a new, encrypted file with the given encryption code.

encryption_code = {'A': ')', 'a': '0', 'B': '(', 'b': '9', 'C': '*', 'c': '8', 'D': '&', 'd': '7', 'E': '^', 'e': '6','F': '%',
        'f': '5', 'G': '$', 'g': '4', 'H': '#', 'h': '3', 'I': '@', 'i': '2', 'J': '!', 'j': '1', 'K': 'Z', 'k': 'z',
        'L': 'Y', 'l': 'y', 'M': 'X', 'm': 'x', 'N': 'W', 'n': 'w', 'O': 'V', 'o': 'v', 'P': 'U', 'p': 'u', 'Q': 'T',
        'q': 't', 'R': 'S', 'r': 's', 'S': 'R', 's': 'r', 'T': 'Q', 't': 'q', 'U': 'P', 'u': 'p', 'V': 'O', 'v': 'o',
        'W': 'N', 'w': 'n', 'X': 'M', 'x': 'm', 'Y': 'L', 'y': 'l', 'Z': 'K', 'z': 'k', '!': 'J', '1': 'j', '@': 'I',
        '2': 'i', '#': 'H', '3': 'h', '$': 'G', '4': 'g', '%': 'F', '5': 'f', '^': 'E', '6': 'e', '&': 'D', '7': 'd',
        '*': 'C', '8': 'c', '(': 'B', '9': 'b', ')': 'A', '0': 'a', ': ': ', ', ', ': ': ', '?': '.', '.': '?',
        '<': '>', '>': '<', "'": '"', '"': "'", '+': '-', '-': '+', '=': ';', ';': '=', '{': '[', '[': '{', '}': ']',
        ']': '}'}

def encryption(text):
    file2 = str(input('What would you like to name the encrypted file?: '))
    secret = open(file2, 'w')

    for word in text:
        for letter in word:
            code = (encryption_code.get(letter, letter))
            secret.write(code)

    secret.close()
    return code


file = str(input('Enter the name of the input file: '))
new = open(file, 'r')
new = new.readlines()
encryption(new)