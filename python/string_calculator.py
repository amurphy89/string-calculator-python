import re

def add(numbers):
    
    if numbers == "":
        return 0

    # work out delimiter
    if re.match("\/\/\[(.+)\]", numbers):
        delimiter = re.match("\/\/\[(.+)\]", numbers)[1]
        delimiter = re.escape(delimiter)
        numbers = numbers.strip(f"//[{delimiter}]\n")
    elif numbers[0:2] == "//":
        delimiter = numbers[2]
        numbers = numbers.strip(f"//{delimiter}\n")
    else :
        delimiter = ","

    #  cast string numbers to integers
    numbers = re.split(f"{delimiter}|\n", numbers)
    casted_numbers = []
    for number in numbers:
        casted_numbers.append(int(number))

    # look for negatives and raise an error if they exist
    is_negative = [number for number in casted_numbers if number < 0]
    if is_negative:
        raise Exception(f"negatives not allowed: {delimiter.join(is_negative)}")

    # exlude numbers larger than 1000
    non_large_numbers = []
    for number in casted_numbers:
        if number < 1001:
            non_large_numbers.append(number)
            
    return sum(non_large_numbers)
    