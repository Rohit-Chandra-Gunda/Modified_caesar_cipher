import string
alphabet = string.ascii_letters + string.digits + string.punctuation + " " + "\n"
letters = dict(enumerate(alphabet))
lenght = len(alphabet)


def caesar(message, key):
    # return the encoded message as a single string!
    coded_message = {}
    for index in letters:
        numb = (index+key) % lenght
        if numb < 0:
            numb += lenght
        coded_message[letters[index]] = numb
    strcode = ""
    for letter in message:
        strcode += letters[coded_message[letter]]
    return strcode
f = open("input.txt", "r")
inp = f.read()
f.close()
while True:
    try:
        key = int(input("Please enter a numerical key."))
        break
    except:
        continue
option = 3
while option not in [1, 2]:
    try:
        option = int(input("Enter 1 to encode.\n 2 to decode"))
    except:
        continue
if option == 2:
    key *= -1
result = caesar(inp, key)
f = open("output.txt", "w")
f.write(result)
f.close()
