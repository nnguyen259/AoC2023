input_file = "input/day1.txt"

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def part1():
    with open(input_file) as inputfile:
        documents = inputfile.read().splitlines()

    total = 0
    for document in documents:
        first = last = None
        for character in document:
            if character in numbers:
                last = character
                if first is None:
                    first = character

        number = int(f"{first}{last}")
        total += number

    return total


def part2():
    numbers.extend(
        ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    )
    number_mapping = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    with open(input_file) as inputfile:
        documents = inputfile.read().splitlines()

    total = 0
    for document in documents:
        first = last = None
        first_idx = len(document)
        last_idx = -1

        for number in numbers:
            n_first_idx = document.find(number)
            if n_first_idx > -1 and n_first_idx < first_idx:
                first_idx = n_first_idx
                if number in number_mapping:
                    first = number_mapping[number]
                else:
                    first = number

            n_last_idx = document.rfind(number)
            if n_last_idx > -1 and n_last_idx > last_idx:
                last_idx = n_last_idx
                if number in number_mapping:
                    last = number_mapping[number]
                else:
                    last = number

        result = int(f"{first}{last}")
        total += result

    return total


print(part1())
print(part2())
