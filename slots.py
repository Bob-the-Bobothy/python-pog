import random

def main(rows=int, columns=int):
    output = []
    slots = (
        "🌮",
        "🌮",
        "🌮",
        "🌮",
        "🫓 ",
        "🫓 ",
        "🫓 ",
        "🍕",
        "🍕",
        "🦒",
        "🦒",
        "🍔",
        "🍒",
        "🌞",
    )

    for i in range(3):
        for i in range(5):
            choice = str(random.choice(slots))
            if choice == "🍒":
                if random.randint(1, 3) == 1:
                    output.append("🍒")
                else:
                    output.append("🌞")
            else:
                output.append(choice)

        print(" ".join(output))
        output.clear()

main()