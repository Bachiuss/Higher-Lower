import logo
import data
import random

print(logo.logo)
score = 0
game_should_continue = True
account_b = random.choice(data.data)

def format_data(account):
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


while game_should_continue:
    account_a = account_b
    account_b = random.choice(data.data)
    while account_a == account_b:
        account_b = random.choice(data.data)


    print(f"Compare A: {format_data(account_a)}.")
    print(logo.vs)
    print(f"Against B: {format_data(account_b)}.")


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"U guessed right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"U guessed wrong! Final score {score}")
