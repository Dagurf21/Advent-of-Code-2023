def open_file(filename):
    lines_in_file = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            lines_in_file.append(line)
    return lines_in_file


def main():
    filename = "Day1-Trebuchet\day_one_input.txt"
    lines_in_file = open_file(filename)

    print (lines_in_file)


if __name__ == "__main__":
    main()  