#This is a very interesting assignment problem I worked on for a coursework a few months ago.

#The question demonstrates the importance of Padding using RSA, without which, it is open to potential risks.
#Here we are given a list of words ('english.txt') alsong with a ciphertext and our modulus N and public exponent e which I have hardcoded in.
#the modulus N is too large to factorise so we know 'p' and 'q' were good choices.
#The trick here is to use the provided list of words and to run a for loop through them all and encrypt each word using the RSA encryption algorithm
#We then compare encrypted word with the ciphertext and the one that matches points to the original message.
#Padding would add a layer of security and prevent this from happening


import math
from tqdm import tqdm

cipher = 1259431684015253725655874579299083675955925441758000443136820821936735505939946424913971913132030607812069425589817918334202189630262486478769590738032280
exponent = 65537
N = 7527229557779400974577643426792404070454959846512204796403613804141551092587560948340441193861324957081926399543592753685519533512417551574685641681126353

word_file = open("english.txt")
word_list = word_file.readlines()
word_file.close()

converted_list = []

for element in tqdm(word_list):
    converted_list.append(element.strip())


for word in tqdm(converted_list):
    word_a = word.encode('utf-8')
    hex = word_a.hex()
    hex_to_decimal = int(hex, 16)
    decimal = str(hex_to_decimal)
    print(decimal)
    encrypted_word = int(decimal) ** exponent % N
    # print(encrypted_word)
    if encrypted_word == cipher:
        print(word)


