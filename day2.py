input_file = "input/day2.txt"


def part1():
    maxes = {"red": 12, "green": 13, "blue": 14}

    with open(input_file) as inputfile:
        games = inputfile.read().splitlines()

    result = 0

    for i, game in enumerate(games):
        valid = True
        plays = game.split(": ")[1].split("; ")
        for play in plays:
            for move in play.split(", "):
                count, color = move.split(" ")
                if int(count) > maxes[color]:
                    valid = False
                    break

            if not valid:
                break

        if valid:
            result += i + 1

    return result


def part2():
    with open(input_file) as inputfile:
        games = inputfile.read().splitlines()

    result = 0
    for game in games:
        red = green = blue = 0
        plays = game.split(": ")[1].split("; ")
        for play in plays:
            for move in play.split(", "):
                count, color = move.split(" ")
                count = int(count)
                if color == "red" and count > red:
                    red = count
                if color == "green" and count > green:
                    green = count
                if color == "blue" and count > blue:
                    blue = count

        result += red * green * blue

    return result


print(part1())
print(part2())
