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

# Part 2 - Simple state machine
answer = 0
match_re = r"do\(\)|don't\(\)|mul\(\d+,\d+\)"

mul_on = True # By default mul is on until we find the first 'don't'

try:
    with open(file_name, 'r') as file:
        data = file.read()
        matches = re.findall(match_re, data)

        if matches:
            #print("Matches found:", matches)
            for match in matches:
                if match == "do()":
                    mul_on = True
                elif match == "don't()":
                    mul_on = False
                if match.startswith("mul") and mul_on:
                    values = list(map(int, re.findall(r'\d+', match)))
                    answer = answer + (values[0] * values[1]) # Will always contain two values that are ints
                
        else:
            print("No match")
   
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

print("Part B answer is: ", answer)