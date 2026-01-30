import re

file_path = r'd:\AIDesign\AppVN\index_v20.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern:
# We just replaced mr-5 with mr-3. Now we want to remove mr-3 entirely.
# Context: "flex-shrink-0 z-10 mr-3" -> "flex-shrink-0 z-10"
# This avoids accidentally removing mr-3 from other unintended places.

regex = r'(flex-shrink-0 z-10 )mr-3'
replacement = r'\1' # Just keep the prefix

new_content = re.sub(regex, replacement, content)

# Also check if reducing gap-3 to gap-2 is needed.
# User said "hẹp hơn" (narrower).
# Currently gap-3 (12px) + mr-3 (12px) = 24px.
# Removing mr-3 => 12px. That is significantly narrower.
# If user wanted even narrower, we could change gap-3 to gap-2 (8px).
# Let's start by removing mr-3 as that corrects the redundancy.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Removed mr-3 from module cards in {file_path}")
