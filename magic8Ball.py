import random

positive_answers = ["Hell yeah!", "I would be happy to help", "You've got this buddy", "I see great things in your future", "Yes definitely", "Tell them how you feel and I am 70% sure they will understand", "You are amazing" ," Absolutely!!", "You were raised right", "Sure!" ]
negative_answers = ["If I were human, I would stay away from you", "Definitely not", "You are on your own on this one buddy", "Did you honestly think asking me would help", "Nope, but thank you for asking"]
vague_answers = [" I don't feel like talking right now"," I don't feel like talking right now","You should see someone about that","Could you speak up please","Loading, please wait...lol"]
answers = [positive_answers + negative_answers + vague_answers]

question = input("Enter the question you want answered: ")
result = ""

result += random.choice(positive_answers + negative_answers)

print(result)
