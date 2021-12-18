import random

variables = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890","£$%&!*"]

result = '' # need to define result variable to store the value of result in for each iteration of the loop
for i in range(3):

    for element in variables:
        result += str(random.choice(element)) # the '+=' adds the value of the result for each section in the list together and displays it in a string (using str).
        # This is done 4 times (for i in range 4) which gives us 16 characters
        # print(result) - Having the print statement here means that the loop iterates once, gets a result from the first element of the list, prints it and THEN
        # goes back and find the next element, adds that to the original result and prints that and so on. If we want one final answer, we place the print statement outside the for loop

print(result)
