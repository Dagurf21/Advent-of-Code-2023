def open_file(filename):
    lines_in_file = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            lines_in_file.append(line)
    return lines_in_file

def find_numbers(line):
    # Define a dictionary to map spelled-out digits to their numerical values
    digit_mapping = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Extract individual words from the line
    words = line.split()

    number = ""
    for word in words:
        # Check if the word is a spelled-out digit
        if word in digit_mapping:
            number += digit_mapping[word]
        else:
            # Check if the word contains numeric characters
            numeric_part = ''.join(char for char in word if char.isdigit())
            if numeric_part:
                number += numeric_part

    # Convert the numerical values to integers and return the sum
    return sum(map(int, number))

def main():
    filename = "Day1-Trebuchet\day_one_input_part_two.txt"
    lines_in_file = open_file(filename)

    numbers = []
    for line in lines_in_file:
        number = find_numbers(line)
        numbers.append(number)

    print(sum(numbers))

if __name__ == "__main__":
    main()
