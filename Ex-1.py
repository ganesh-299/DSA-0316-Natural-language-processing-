import re

# Text to search
text = "Python is easy. Python is powerful. Learning Python is fun."

# Pattern to search
pattern = "Python"

# Search for first occurrence
match = re.search(pattern, text)

if match:
    print("Pattern found at position:", match.start())
else:
    print("Pattern not found")

# Find all occurrences
all_matches = re.findall(pattern, text)

print("All matches:", all_matches)
print("Total matches:", len(all_matches))
