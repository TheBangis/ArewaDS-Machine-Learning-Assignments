import random

random_responses = ["That is quite interesting, please tell me more.",
                    "I see. Do go on.",
                    "Why do you say that?",
                    "Funny weather we've been having, isn't it?",
                    "Let's change the subject.",
                    "Did you catch the game last night?"]

print("Hello, I am Marvin, the simple robot.\nYou can end this conversation at any time by typing 'bye'\nAfter typing each answer, press 'enter'\nHow are you today?")
    
while True:
    user = input("> ")
    if user.lower() == 'bye':
        break
    else:
        response = random.choice(random_responses)
        print(response)

print("It was nice talking to you, goodbye!")