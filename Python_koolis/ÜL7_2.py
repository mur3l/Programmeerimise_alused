with open("luuletus.txt", encoding="utf-8") as file:
    for nr, line in enumerate(file):
        print(f"{nr + 1} {line.rstrip()} ({len(line) - 1})")

