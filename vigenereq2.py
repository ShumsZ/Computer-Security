from operator import index
from tqdm import tqdm

characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
character_count = len(characters)

c1_text = "OJBYWNOYVP"

c2_text = "CBVHTJDNVQ"

p2_text = "BANALITIES"
p1_text = "NITROMETER"
print(c1_text)


def subtract_char(char1, char2):
    c1_code = characters.index(char1)
    c2_code = characters.index(char2)

    result_code = (c1_code - c2_code) % character_count

    result = characters[result_code]

    return result


def subtract_string(text1, text2):
    subtraction_result = ""

    for (text1_index, text1_character) in enumerate(text1):
        text2_index = text1_index % len(text2)
        text2_character = text2[text2_index]
        subtraction = subtract_char(text1_character, text2_character)

        subtraction_result += subtraction
    return subtraction_result
key = subtract_string(p1_text, c1_text)
print("Key= ", key)
key_test = subtract_string(p2_text, c2_text)
print ("Key test: ", key_test)




sol = subtract_string(c1_text, c2_text)
print(sol)

ten_letter_word_file = open("10letterwordslist.txt", "r")
word_list = ten_letter_word_file.readlines()
ten_letter_word_file.close()

converted_list = []
converted_list_copy = []

for element in word_list:
    converted_list.append(element.strip())
    converted_list_copy.append(element.strip())

final_list = []
#print(converted_list)

#for i in converted_list:
    #for j in converted_list_copy:
        #subtract_string()

        #print(i,j)


#for i in range(len(converted_list)):
#    for j in range(len(converted_list)):
#        subtraction_of_ciphers = subtract_string(i, j)
#        final_list.append(subtraction_of_ciphers)

    #print(final_list)


# print(converted_list[30000])



#for i in range(len(converted_list)):
 #   i = 0
  #  subtraction_of_ciphers = subtract_string(converted_list[i], converted_list[6])

#print(subtraction_of_ciphers)
#i = 0
#j = 1
#while tqdm(i < len(converted_list) - 1):
#    while j < len(converted_list) - 1:

#        subtraction_of_ciphers = subtract_string(converted_list[i], converted_list[j])
#        final_list.append(subtraction_of_ciphers)


#        j = j + 1
#        i = i + 1

    #print(final_list)

#for i in final_list:
#    if i == sol:
#        print(i)

#    print(subtraction_of_ciphers)

#i = 0
#while i < len(converted_list) - 1:
 #   subtraction_of_ciphers = subtract_string(converted_list[i], converted_list[1])
  #  i = i + 1

   # print(subtraction_of_ciphers)




