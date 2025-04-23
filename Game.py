import pymongo
import random

client = pymongo.MongoClient()
db = client["News"]
fake = db["Fake"]
real = db["Real"]


def get_random_headline():
    if random.choice(["real", "fake"]) == "real":
        headline = real.aggregate([{"$sample": {"size": 1}}]).next()
        return headline['title'], True
    else:
        headline = fake.aggregate([{"$sample": {"size": 1}}]).next()
        return headline['title'], False


def play_game():
    print("\n--------------------- Welcome to HEADLINE HUSTLE ---------------------\n")
    rounds = int(input("How many rounds do you dare to play?!?\n>"))
    correct = 0
    for i in range(rounds):
        print(f"\n\nRound {i + 1}/{rounds}")
        headline, is_real = get_random_headline()
        print("Headline: ", headline)
        guess = input("Is this Real or Fake? (r/f): ").strip().lower()

        if (guess == 'r' and is_real) or (guess == 'f' and not is_real):
            print("\nCorrect!")
            correct += 1

        else:
            print("\nWrong!")
            print("\nIt was actually", "Real." if is_real else "Fake.")

    accuracy = correct / rounds * 100
    print(f"\nGame Over! You got {correct} out of {rounds} correct.")
    print(f"Accuracy: {accuracy:.2f}%")


if __name__ == "__main__":
    play_game()
