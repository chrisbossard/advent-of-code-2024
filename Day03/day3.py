import re

match_re = r'mul\(\d+,\d+\)'
file_name = "Day03/data.txt"

answer = 0

try:
    with open(file_name, 'r') as file:
        data = file.read()
        matches = re.findall(match_re, data)

        if matches:
            #print("Matches found:", matches)
            for match in matches:
                values = list(map(int, re.findall(r'\d+', match)))
                answer = answer + (values[0] * values[1]) # Will always contain two values that are ints
        else:
            print("No match")
   
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

print("Part A answer is: ", answer)