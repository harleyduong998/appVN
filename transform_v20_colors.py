import re

file_path = r'd:\AIDesign\AppVN\index_v20.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern to find module cards
# We look for the anchor tag with class containing 'module-card'
# Then we look for the icon div inside it to get the text color
# We need to capture the full class string of the module card to replace bg-white

# Regex strategy:
# 1. Find the module card opening tag.
# 2. Find the icon color class within a reasonable distance.
# 3. Replace bg-white in the card class with the matching bg color.

# Since HTML structure is consistent, we can iterate through the file line by line or use a more robust parsing approach.
# Given the repetitive structure, regex on the content string is feasible if we are careful.

# Let's try to match the entire block approximately or find all module-card tags and their subsequent icon colors.

# Better approach:
# Loop through the content using regex finditer to locate each module card.

pattern_card = re.compile(r'(<a\s+href="[^"]+"\s+data-categories="[^"]+"\s+class=")([^"]*module-card[^"]*)("[\s\S]*?<div\s+class="[^"]*text-([a-z]+)-[0-9]+)')

# The structure we are looking for is:
# <a href="..." data-categories="..."
#    class="module-card bg-white ...">
#    <div class="...">
#       <i class="... text-{COLOR}-..." ...>
# OR the text color is on the div wrapper of the icon:
# <div class="... text-{COLOR}-500 ...">

# In index_v19.html (which v20 is copied from):
# <div class="... text-blue-500 ...">
# So the color is in the div class list.

def replace_callback(match):
    prefix = match.group(1)
    class_string = match.group(2)
    suffix = match.group(3)
    color = match.group(4) # captured from text-{color}-...
    
    # Check if color is valid
    if not color:
        return match.group(0)
        
    # Replace bg-white with bg-{color}-50
    # Also we might need to adjust card-hover border if needed, but user asked for background.
    
    # Special handling for slate/gray/zinc which might be 'bg-slate-50' etc.
    # The user said "nền giống màu icon nhưng nhạt" (background like icon color but pale).
    
    new_bg = f"bg-{color}-50"
    
    # Replace the *first* bg-white. 
    # Note: class_string contains the whole class list of the <a> tag.
    new_class_string = class_string.replace('bg-white', new_bg)
    
    return f"{prefix}{new_class_string}{suffix}"

# The regex needs to be careful about newlines.
# Pattern explanation:
# 1. Start of <a> tag with class 'module-card': (<a[^>]*class="[^"]*module-card[^"]*)
# 2. Capture the class string? No, simpler to match the whole `bg-white` inside `class="...module-card...`.
# 
# Let's try a two-step approach for safety.
# 1. Find all `<a>` blocks that are module cards.
# 2. Extract the color.
# 3. Perform replacement.

updated_content = content

# Regex to capture the whole module card block roughly from <a to </a>
# But let's be more precise.
# We will look for `class="module-card bg-white` and the subsequent `text-{color}-`
# Since the text-{color} is inside the inner div, we need to span lines.

# Finds: class="module-card bg-white ... (capture rest of class)" ... (some html) ... text-(capture color)-
regex = r'(class="module-card\s+)bg-white(\s+[^"]*".*?text-)([a-z]+)(-[0-9]+)'

# re.DOTALL is essential to span lines
# Group 1: 'class="module-card '
# Group 2: ' rounded-xl ... " ... <div ... ' (everything up to text-COLOR-)
# Group 3: 'blue' (the color)
# Group 4: '500' (the shade)

new_content = re.sub(regex, r'\1bg-\3-50\2\3\4', content, flags=re.DOTALL)

# Update the title as well
new_content = new_content.replace('<title>Dashboard V1 - Original</title>', '<title>Dashboard V20 - Colored Cards</title>')
new_content = new_content.replace('Dashboard V1 - Original', 'Dashboard V20 - Colored Cards') # Just in case

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Transformation complete for {file_path}")
