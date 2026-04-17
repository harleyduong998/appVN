import re

file_path = 'index_v22.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex to find the module cards (anchor tags with specific classes)
# We look for <a href="..." class="..."> ... </a>
# We target class "bg-white rounded-xl p-4 shadow-sm border border-slate-200/30 card-hover group"

# Strategy:
# 1. Identify valid card blocks.
# 2. Inside each block:
#    a. Add 'card-v22' to the main class list.
#    b. Remove any hover:border-*-500/600/700
#    c. Locate the icon div (w-14 class).
#       - Remove text-* classes (colors)
#       - Remove group-hover:* classes
#       - Add 'text-gradient-blue'
#    d. Locate the h3 tag.
#       - Remove group-hover:text-* classes

def process_card_match(match):
    full_block = match.group(0)
    
    # 1. Update main card classes
    # Add card-v22 if not present
    if 'card-v22' not in full_block:
        full_block = re.sub(r'class="([^"]+)"', r'class="\1 card-v22"', full_block, count=1)
    
    # Remove existing hover border colors to let card-v22 take precedence
    full_block = re.sub(r'hover:border-[a-z]+-\d+', '', full_block)
    
    # 2. Process Icon Div
    # Find the div with w-14
    def icon_div_sub(m):
        div_tag = m.group(0)
        # Remove text color (text-*-500/600)
        div_tag = re.sub(r'\btext-[a-z]+-\d+\b', '', div_tag)
        # Remove group-hover classes
        div_tag = re.sub(r'\bgroup-hover:[^"\s]+\b', '', div_tag)
        # Add gradient class
        if 'text-gradient-blue' not in div_tag:
            div_tag = div_tag.replace('class="', 'class="text-gradient-blue ')
        return div_tag

    full_block = re.sub(r'<div[^>]*class="[^"]*w-14[^"]*"[^>]*>', icon_div_sub, full_block)
    
    # 3. Process H3
    def h3_sub(m):
        h3_tag = m.group(0)
        # Remove group-hover text color
        h3_tag = re.sub(r'\bgroup-hover:text-[a-z]+-\d+\b', '', h3_tag)
        return h3_tag

    full_block = re.sub(r'<h3[^>]*>', h3_sub, full_block)
    
    return full_block

# Regex to capture the card <a> block. 
# We assume standard structure from index.html. 
# Using a pattern that matches the specific classes to avoid replacing other links.
pattern = r'<a href="[^"]+"[^>]*class="[^"]*card-hover[^"]*"[^>]*>.*?</a>'

# DOTALL to match across newlines
new_content = re.sub(pattern, process_card_match, content, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"Standardized cards in {file_path}")
