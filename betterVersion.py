import random


def pass_gen():
    # double the number occurances to increase their chances of being selected by random.choice
    variables = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z',
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y', 'Z',
                 '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
                 '£', '$', '%', '&', '!', '*', '£', '$', '%', '&', '!', '*', '£', '$', '%', '&', '!', '*']

    chars = int(input('Enter required number of characters for your password: '))

    password = ""
    warning = "WARNING: YOUR PASSWORD MAY BE TOO SHORT"

    for i in range(1, chars + 1):
        password += random.choice(variables)

    if len(password) <= 6:
        return password + " ; " + warning
    return password


solution = pass_gen()

print(solution)
