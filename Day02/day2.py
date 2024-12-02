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


# Part 2

def is_safe(levels):
    """Check if the given levels list is safe according to the rules."""
    differences = [abs(y - x) for x, y in zip(levels, levels[1:])]
    return (all(x < y for x, y in zip(levels, levels[1:])) or
            all(x > y for x, y in zip(levels, levels[1:]))) and \
           all(1 <= diff <= 3 for diff in differences)

safe = 0

try:
    with open(file_name, 'r') as file:
        for report in file:
            levels = list(map(int, report.split()))  # Convert strings to integers

            # Check if already safe
            if is_safe(levels):
                safe += 1
                continue

            # Simulate removing each level
            for i in range(len(levels)):
                modified_levels = levels[:i] + levels[i + 1:]  # Remove one level
                if is_safe(modified_levels):
                    safe += 1
                    break  # No need to check further removals for this report

except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")

print("Number of safe reports in Part 2 are: ", safe)