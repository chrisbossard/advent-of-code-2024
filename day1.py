from collections import defaultdict

message = "Advent of Code 2024"
print(message)

list_a = []
list_b = []

total_distance = 0

def read_file_into_lists(file_name):
    list_a = []
    list_b = []
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Split the line into two parts
                values = line.split()
                
                # Check if the line has exactly two columns
                if len(values) == 2:
                    # Append the first value to list_a and the second to list_b
                    list_a.append(int(values[0]))
                    list_b.append(int(values[1]))
                else:
                    print(f"Skipping malformed line: {line.strip()}")
        
        return list_a, list_b
    
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
        return None, None

list_a, list_b = read_file_into_lists("data.txt")


list_a.sort()
list_b.sort()

print("List A:", list_a[0:5])
print("List B:", list_b[0:5])

distance = [abs(a-b) for a, b in zip(list_a, list_b)]

for value in distance:
    total_distance = total_distance + value

print("Total distance: ", total_distance)

# Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears 
# in the right list.

number_frequency = defaultdict(int)

for a in list_a:
    for b in list_b:
        if a == b: # Left list value equal to right list value
            number_frequency[b] += 1

similarity_score = 0
for a in list_a:
    if a in list(number_frequency.keys()):
        similarity_score = similarity_score + (a * number_frequency[a])

print("Similarity Score: ", similarity_score)

