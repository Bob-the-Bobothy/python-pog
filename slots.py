"""Module random.choice is used to pick random option from list of slots."""
import random

def main():
    """Function main() is used to print random slot from list of slots."""
    output = []
    slots = (
        "🌮",
        "🫓",
        "🍕",
        "🦒",
        "🍔",
        "7",
    )

    for i in range(5):
        output.append(random.choice(slots))

    print(output)
