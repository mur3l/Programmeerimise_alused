from Cooper import read_file

default_file_name = "delta_vaibad.txt"
long_rug = 5
with open(default_file_name, "w", encoding="utf-8") as file:
    file.write("""7
4.9
3.63
5
""")


def calculate_thread_length(rug_final_length: float, thread_count: int) -> float:
    """
    Calculate length of thread needed for given rug dimensions.
    single thread length - rug_final_length + 20% + 2 * 0,25
    :param rug_final_length:
    :param thread_count:
    :return: thread_count times single thread length
    """
    single_thread_length = rug_final_length * 1.2 + 0.5
    return round(single_thread_length * thread_count, 2)


if __name__ == '__main__':
    filename = input(f"Sisestage failinimi [{default_file_name}]: ")
    long_rug_thread_count = int(input(f"Sisestage {long_rug} meetriste ja pikemate vaipade lõimede arv: "))
    short_rug_thread_count = int(input("Sisetage lühemate vaipade lõimede arv: "))
    rug_lengths = read_file(filename if filename else default_file_name)
    total_thread_length = 0
    for length_txt in rug_lengths:
        rug_length = float(length_txt)
        if rug_length >= long_rug:
            thread_length = calculate_thread_length(rug_length, long_rug_thread_count)
        else:
            thread_length = calculate_thread_length(rug_length, short_rug_thread_count)
        print(F"{length_txt} m vaibale kulub {thread_length} m lõime.")
        total_thread_length += thread_length
    print(f"Kõikide vaipade peale läheb vaja {total_thread_length} meetrit lõime materjali.")