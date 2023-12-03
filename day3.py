input_file = "input/day3.txt"

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
non_symbols = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def check(i, j, schematics):
    max_a = len(schematics)
    max_b = len(schematics[0])
    for a in range(i - 1, i + 2):
        for b in range(j - 1, j + 2):
            if (
                a > -1
                and a < max_a
                and b > -1
                and b < max_b
                and schematics[a][b] not in non_symbols
            ):
                return True

    return False


def part1():
    with open(input_file) as inputfile:
        schematics = inputfile.read().splitlines()

    total = 0
    for i, schematic in enumerate(schematics):
        number = ""
        valid = False
        for j, character in enumerate(schematic):
            if character in numbers:
                number += character
                if not valid:
                    if check(i, j, schematics):
                        valid = True
            if character not in numbers:
                if number != "" and valid:
                    total += int(number)
                number = ""
                valid = False
        if number != "" and valid:
            total += int(number)

    return total


def part2():
    with open(input_file) as inputfile:
        schematics = inputfile.read().splitlines()

    total = 0
    for i, schematic in enumerate(schematics):
        for j, character in enumerate(schematic):
            if character == "*":
                print("new gear")
                count = 0
                product = 1
                # check left
                if j > 0 and schematic[j - 1] in numbers:
                    count += 1
                    number = ""
                    temp_idx = j - 1
                    while temp_idx > -1 and schematic[temp_idx] in numbers:
                        number = schematic[temp_idx] + number
                        temp_idx -= 1
                    print("left: ", number)
                    product *= int(number)

                # check right
                if j < len(schematic) - 1 and schematic[j + 1] in numbers:
                    count += 1
                    number = ""
                    temp_idx = j + 1
                    while temp_idx < len(schematic) and schematic[temp_idx] in numbers:
                        number += schematic[temp_idx]
                        temp_idx += 1
                    print("right: ", number)
                    product *= int(number)

                # check top
                if i > 0 and any(
                    (
                        schematics[i - 1][max(0, j - 1)] in numbers,
                        schematics[i - 1][j] in numbers,
                        schematics[i - 1][min(j + 1, len(schematic))] in numbers,
                    )
                ):
                    temp_idxs = []
                    if schematics[i - 1][j] in numbers:
                        temp_idxs.append(j)
                    else:
                        if j > 0 and schematics[i - 1][j - 1] in numbers:
                            temp_idxs.append(j - 1)
                        if (
                            j < len(schematic) - 1
                            and schematics[i - 1][j + 1] in numbers
                        ):
                            temp_idxs.append(j + 1)

                    for temp_idx in temp_idxs:
                        count += 1
                        number = ""

                        temp_idx_l = temp_idx
                        while (
                            temp_idx_l > -1 and schematics[i - 1][temp_idx_l] in numbers
                        ):
                            number = schematics[i - 1][temp_idx_l] + number
                            temp_idx_l -= 1

                        tmp_idx_r = temp_idx + 1
                        while (
                            tmp_idx_r < len(schematic)
                            and schematics[i - 1][tmp_idx_r] in numbers
                        ):
                            number += schematics[i - 1][tmp_idx_r]
                            tmp_idx_r += 1

                        print("top: ", number)
                        product *= int(number)

                # check bottom
                if i < len(schematics) - 1 and any(
                    (
                        schematics[i + 1][max(0, j - 1)] in numbers,
                        schematics[i + 1][j] in numbers,
                        schematics[i + 1][min(j + 1, len(schematic))] in numbers,
                    )
                ):
                    temp_idxs = []
                    if schematics[i + 1][j] in numbers:
                        temp_idxs.append(j)
                    else:
                        if j > 0 and schematics[i + 1][j - 1] in numbers:
                            temp_idxs.append(j - 1)
                        if (
                            j < len(schematic) - 1
                            and schematics[i + 1][j + 1] in numbers
                        ):
                            temp_idxs.append(j + 1)

                    for temp_idx in temp_idxs:
                        count += 1
                        number = ""

                        temp_idx_l = temp_idx
                        while (
                            temp_idx_l > -1 and schematics[i + 1][temp_idx_l] in numbers
                        ):
                            number = schematics[i + 1][temp_idx_l] + number
                            temp_idx_l -= 1

                        tmp_idx_r = temp_idx + 1
                        while (
                            tmp_idx_r < len(schematic)
                            and schematics[i + 1][tmp_idx_r] in numbers
                        ):
                            number += schematics[i + 1][tmp_idx_r]
                            tmp_idx_r += 1

                        print("bottom: ", number)
                        product *= int(number)

                if count == 2:
                    total += product

    return total


print(part1())
print(part2())
