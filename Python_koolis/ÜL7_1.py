def create_file(file_name:str, lines: list) -> None:
    with open(file_name, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(f"{line}\n")

def read_file(file_name) -> list:
    result =[]
    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            file.write(f"{line}\n")

def split_words(sentences: list) -> list:
    result = []
    for sentence in sentences:
        result.append(sentence.split())
    return result

if __name__ == "__main__":
    file_name = "tuttavad.txt"
    create_file(file_name,["Tiit Sukk", "Armas Noole", "Elina Elli", "Joosep Juurikas", "Õnne Kolmteist", "Murel Sulev"])
    names = read_file(file_name)
    print(names)
    split_names = split_words(names)
    print(split_names)
    sorted_names = list(map(lambda s: " ".join(s), sorted(split_names, key=lambda n: n[-1])))
    for name in sorted_names:
        print(f"{name}")
    create_file("sorteeritud_tuttavad.txt", sorted_names)



