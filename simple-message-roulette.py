import random

phrases = [
    "message1",
    "message2",
    "message3",
    "message4",
    "message5",
    "message6",
    "message7",
    "message8",
    "message9",
    "message10"
]

emoji = [
    "🔴",
    "🟠",
    "🟡",
    "🟢",
    "🔵"
]

# Randomly select how many phrases to print (between 1 and 5)
num_phrases = random.randint(1, 5)

for _ in range(num_phrases):
    print("message0 " + random.choice(phrases) + " " + random.choice(emoji))