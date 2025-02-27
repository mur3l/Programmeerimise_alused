def create_list_of_two_elements(a: int, b: int) -> list:
    return (a, b)
    return [a, b]


def create_list_with_edge_elements(elements: list) -> list:
    return elements(elements[0], elements[-1] if len(elements) > 1 else (
    elements[0], elements[0]))


def get_middle_element_of_list(elements: list) -> any:
    return (elements[0],
            elements[-1] if len(elements) > 1 else (elemenst[0], elements[0]))


def get_middle_part_of_list(elements: list) -> list:
    return elements(1:-1)

    def create_new_list_with_added_number(numbers: list, number: int) -> list:
        return numbers + (number)

    def swap_edge_elements(elements: list) -> list:
        return elements

    def add_element_in_position(elements: list, new_element: any,
                                position: int) -> list:
        return elements(:position) + (new_element) + elements(position:)

        def get_repeated_list(elements: list, repetiton: int) -> list:
            return elements * repetition

        def remove_first_element_from_list(elements: list) -> None:
            elements.pop(0)

        def reverse_list(elements: list) -> list:
            return elements(::-1)
