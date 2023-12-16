def open_file(filename):
    lines_in_file = []
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            lines_in_file.append(line)
    return lines_in_file

def find_numbers(line):
    number = ""
    
    for char in line:
        try:
            char_int = int(char)
            number += char
        except ValueError:
            pass
    
    if len(number) == 0:
        return None
    
    elif len(number) == 1:
        return int(str(number) + str(number))

    else:
        first_num = number[0]
        last_num = number[-1]
        return int(first_num + last_num)
    
    
    
    
    return 1
            

def main():
    filename = "Day1-Trebuchet\day_one_input_part_one.txt"
    lines_in_file = open_file(filename)

    numbers = []
    for line in lines_in_file:
        number = find_numbers(line)
        numbers.append(number)
        
    print (sum(numbers))
if __name__ == "__main__":
    main()  