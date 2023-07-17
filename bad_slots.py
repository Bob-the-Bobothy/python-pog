import random
import base64

output = []
foods = {
    "🌮": 1,
    "🍔": 2,
    "🍕": 3,
    "🍟": 4,
    "🍣": 5,
}
wins = 0
total_wins = 0

for i in range(10):
    for i in range(3):
        output.append(random.choice(list(foods.keys())))

    if output[0] == output[1] == output[2]:
        wins += 1

    print(" |".join(output))

    output = []

if wins > 0:
    with open('wins.txt', 'a') as file:
        message = f"{wins}"
        message_bytes = message.encode('utf-8')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('utf-8')
        file.write(f"{base64_message}\n")

try:
    with open('wins.txt', 'r') as file:
        data = file.readlines()
        for line in data:
            line_bytes = line.encode('utf-8')
            message_bytes = base64.b64decode(line_bytes)
            message = message_bytes.decode('utf-8')
            total_wins += int(message)

except FileNotFoundError:
    pass

if wins == 0:
    print(f"you didn't win, and you've won {total_wins} times ever")

elif wins == 1:
    print(f"you won {wins} time, and you've won {total_wins} times ever")

else:
    print(f"you won {wins} times, and you've won {total_wins} times ever")