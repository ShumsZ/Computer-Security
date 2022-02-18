import numpy as np



c1 = "OJBYWNOYVP"
#c1bin = ' '.join(format(ord(x), 'b') for x in c1)


c2 = "CBVHTJDNVQ"
#c2bin = ' '.join(format(ord(x), 'b') for x in c2)


c3 = "ABATEMENTS"

XOR = [chr(ord(a) ^ ord(b)) for a,b in zip(c1,c2)]
P1_XOR_P2 = "".join(XOR)


##########################################

for word in ten_letter_word_file:
    words = []
    each_word = word.strip()
    words.append(each_word)
    print(words)

    subtraction_of_ciphers = subtract_string(converted_list[word], converted_list[word + 1])

for i in converted_list:
    i = 0 and i < len(converted_list)
    for j in converted_list:
        j = 1 and j < len(converted_list)
        subtraction_of_ciphers = subtract_string(converted_list[i], converted_list[j])
        j +=1
    i+=1


#####works###########

i = 0
j = 1
while i < len(converted_list)-1:
    while j < len(converted_list)-1:
        subtraction_of_ciphers = subtract_string(converted_list[i], converted_list[j])
        j = j + 1
        i = i + 1

        print(subtraction_of_ciphers)



######factorise
#prime factors
n = int(input("Enter the number for calculating the prime factors :\n"))
for i in range(2,n + 1):
    if n % i == 0:
        count = 1
        for j in range(2,(i//2 + 1)):
            if(i % j == 0):
                count = 0
                break
        if(count == 1):
            print(i)

