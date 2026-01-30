import re

file_path = r'd:\AIDesign\AppVN\index_v20.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern:
# We want to find the div that contains the icon inside a module card.
# The class usually looks like:
# class="w-14 h-14 ... mr-5 group-hover:bg-..."
# We want to change mr-5 to mr-3.

# Let's be specific to avoid changing other mr-5s if they exist.
# The module card icon container always starts with w-14 h-14.

# Regex: find 'w-14 h-14' followed eventually by 'mr-5' inside the same class attribute?
# Or strictly: `mr-5` inside the class string of the div.

# Only replace mr-5 if it follows w-14 h-14 in the same tag line, or checking the context.
# Almost all lines in the grep output showed the same structure:
# ... class="w-14 h-14 ... flex-shrink-0 z-10 mr-5 group-hover:..."

# So we can safely replace "flex-shrink-0 z-10 mr-5" with "flex-shrink-0 z-10 mr-3"
# This provides enough context to be safe.

regex = r'(flex-shrink-0 z-10 )mr-5'
replacement = r'\1mr-3'

new_content = re.sub(regex, replacement, content)

# Check if any mr-5 remain that might be relevant?
# The grep showed uniform usage.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Replaced mr-5 with mr-3 in {file_path}")
