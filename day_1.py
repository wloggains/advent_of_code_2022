# Get input
input_file = "day_1_input.txt"
with open(input_file) as f:
    lines = f.read().splitlines()

# Initialize
current_elf = 0
elves = []

# Parse each line
for line in lines:

    if line:
        current_elf += int(line)

    else:
        elves.append(current_elf)
        current_elf = 0

elves.sort()
print(f"The top elf is holding {elves[-1]}.")

print(f"The top three are holding {sum(elves[-3:])}.")
