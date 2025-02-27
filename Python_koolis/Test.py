file_name = "test.txt"

with open(file_name, "a", encoding="utf8") as file:
    file.write("tere\n")

with open(file_name, encoding="utf8") as file:
    print(file.readlines())
    file_name("error")