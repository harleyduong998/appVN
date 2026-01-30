import re

file_path = r'd:\AIDesign\AppVN\index_v20.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern:
# Find h3 tags with class containing 'truncate'
# <h3 class="... truncate ...">
# Replace 'truncate' with 'text-fade'

# Regex:
# We look for <h3 ... class="... truncate ...">
# But effectively, in this file, 'truncate' is used specifically for these titles.
# Let's verify context: "font-bold text-slate-800 text-sm truncate group-hover:..."

regex = r'(<h3[^>]*class="[^"]*)truncate([^"]*")'
replacement = r'\1text-fade\2'

# We can replace all instances of 'truncate' if we are sure it's only used for titles?
# Or replace "truncate" inside the specific class string structure?
# Given the repetitive structure, global replace of 'truncate' inside h3 tags is best.

# Let's simply target the string " truncate " assuming space delimiters, or "truncate" in general.
# The class list is space separated.
# "text-sm truncate group-hover" -> "text-sm text-fade group-hover"

new_content = content.replace(' truncate ', ' text-fade ')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced truncate with text-fade in {file_path}")
