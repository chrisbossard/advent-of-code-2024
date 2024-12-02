file_name = "Day02/data.txt"
safe = 0

try:
    with open(file_name, 'r') as file:
        for report in file:
            levels = list(map(int, report.split()))  # Convert strings to integers
            is_increasing = all(x < y for x, y in zip(levels, levels[1:]))  # pairwise comparison
            is_decreasing = all(x > y for x, y in zip(levels, levels[1:]))
            
            # Pass over the level if it is neither increasing nor decreasing
            if not is_increasing and not is_decreasing:
                continue
            
            # Calculate differences between adjacent levels
            differences = [abs(y - x) for x, y in zip(levels, levels[1:])]

            # Check if all differences are between 1 and 3
            if all(1 <= diff <= 3 for diff in differences):
                safe += 1  
   
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

print("Number of safe reports are: ", safe)
