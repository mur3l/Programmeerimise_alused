import Python_koolis_5_2 as second

def reverse_dictionary(dictionary):
    reversed_dictionary = {}
    for key, value in dictionary.items():
        reversed_dictionary[value] = key
    return reversed_dictionary
e_english = reverse_dictionary(second.dictionary.english)
e_italian = reverse_dictionary(second.dictionary.italian)

if __name__ == "__main__":
    print(e_english)
    print(e_italian)