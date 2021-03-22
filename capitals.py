"""
TODO: Capitals Console game

Game rules:
1. Two players: user and computer
2. Each player enters a capital name one after another
3. User starts first
4. The last letter of a capital name has to be the same as the first letter of another capital name
5. In case user does not know any capital to enter then some kind of stop word should terminate the game
6. In case computer does not know any capital to enter then it prints a win message for user

Requirements:
1. Do not hard code capitals list in Python code directly
2. Use context manager (`with` statement) to work with capitals database
3. Use decorator to measure the game time and print it out when the game ends
"""

import time
import json

def game_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Час гри: %s секунд" % int(end_time - start_time))
        return result
    return wrapper


def get_capitals():
    with open("capitals.json") as f:
        return {x.lower() for x in json.load(f)}


def error_message(user_capital, last_letter, used_capitals, capitals):
    if last_letter and not user_capital.startswith(last_letter):
        return "Last letter is not equal first letter"
    elif user_capital in used_capitals:
        return "The capital has already been used"
    elif user_capital not in capitals:
        return "Capital not found"


@game_time
def game():
    print("Stop word - 'stop'\n")
    print("-----CAPITALS-----")
    print("---GAME STARTED---\n")

    capitals = get_capitals()
    last_letter = ""
    used_capitals = set()

    while True:
        user_capital = input("> You: ").lower()

        if user_capital == "stop":
            print("\nCOMPUTER WIN")
            break

        error = error_message(user_capital, last_letter, used_capitals, capitals)
        if error:
            print(error)
            continue

        used_capitals.add(user_capital)
        capitals.remove(user_capital)
        last_letter = user_capital[-1]

        computer_capital = None
        for computer_capital in capitals:
            if computer_capital.startswith(last_letter):
                break

        time.sleep(1)

        if computer_capital:
            used_capitals.add(computer_capital)
            capitals.remove(computer_capital)
            last_letter = computer_capital[-1]
            print("> Computer: " + computer_capital.title())
        else:
            print("\nYOU ARE A WINNER")
            break

    print("\n---END---")


game()
