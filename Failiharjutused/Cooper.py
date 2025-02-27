file_name = "cooper.txt"
def read_file(file_name) -> list:
    result =[]
    with open(file_name, "r", encoding="utf8") as file:
        for line in file:
            result.append(line.rstrip())
    return result

def get_cooper_result(distance: int, is_male :bool) -> tuple[str, None]:
    result = "väga hea"
    distance_to_next = None
    if distance < 2000 and is_male or distance < 1800 and not is_male:
        result ="Nõrk"
        distance_to_next = 2000 - distance if is_male else 1800 - distance
    elif distance < 2800 and is_male or distance < 2600 and not is_male:
        result ="Rahuldav"
        distance_to_next = 2800 - distance if is_male else 2600 - distance
    return result, distance_to_next

def process_results(results_from_file :[str]):
    results = []
    male_distance_count = 0
    male_distance_sum = 0
    female_distance_count = 0
    female_distance_sum = 0
    for line in results_from_file:
        distance_txt, gender_txt = tuple(line.split())
        distance = int(distance_txt)
        if gender_txt == "M":
            male_distance_sum += distance
            male_distance_count += 1
            cooper_result = get_cooper_result(distance, True) + (gender_txt, distance_txt)
        else:
            female_distance_sum += distance
            female_distance_count += 1
            cooper_result = get_cooper_result(distance, False) + (gender_txt, distance_txt)
        results.append(cooper_result)
    average_distance = round(male_distance_sum / male_distance_count)
    male_average_result = get_cooper_result(average_distance, True) + ("M", str(average_distance))
    average_distance = round(female_distance_sum / female_distance_count)
    female_average_result = get_cooper_result(average_distance, False) + ("N", str(average_distance))
    return results, [male_average_result, female_average_result]

def display_cooper_results(cooper_results):
    for result, distance_to_next, gender, distance in cooper_results:
        if distance_to_next:
            print(
                f"{gender} {distance} m, {result}, järgmisest hindest puudu {distance_to_next} m")
        else:
            print(f"{gender} {distance} m, {result}")


if __name__ == '__main__':
        file_name = input("Sisesta faili nimi: ")
        results_from_file = read_file(file_name)
        cooper_results = process_results(results_from_file)
        display_cooper_results(cooper_results[0])
        print("Keskmised:")
        display_cooper_results(cooper_results[1])






