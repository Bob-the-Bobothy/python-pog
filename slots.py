"""Module random.choice is used to pick random option from list of slots."""
import random
from threading import Thread

def main():
    output = []
    slots = (
        "🌮",
        "🫓 ",
        "🍕",
    )

    while True:
        for out in range(3):
            output.append(random.choice(slots))

        print(" | ".join(output))
        output = []
    

threads = []

for i in range(1000):
    x = Thread(target=main)
    threads.append(x)
    x.start()
