import random

user_choices = ["heads", "tails"]

random_pick = random.randint(0, 1)
user_pick = user_choices[random_pick]

print(user_pick)
