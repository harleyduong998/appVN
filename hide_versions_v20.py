import os
import re

base_dir = r'd:\AIDesign\AppVN'

# 1. Define Visible Chain
# Map visible versions to their filenames
# ordering is important
visible_chain = [
    'index.html',      # v1
    'index_v2.html',   # v2
    'index_v10.html',  # v10
    'index_v14.html',  # v14
    'index_v15.html',  # v15
    'index_v16.html',  # v16
    'index_v18.html',  # v18
    'index_v19.html',  # v19
    'index_v20.html',  # v20
]

# Versions to hide from dropdown
# Regex pattern for these filenames
hidden_pattern = r'index_v(3|4|5|6|7|8|9|11|12|13|17)\.html'

def update_file(filepath):
    filename = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # --- 2. Remove Hidden Versions from Dropdown ---
    # Pattern: <a href="index_vX.html" ... </a>
    # We use re.DOTALL to match across lines
    # We strictly look for matches inside the dropdown container? 
    # Or just globally remove existing dropdown links to these versions?
    # Global removal of specific 'dropdown item' looking links is safe if properly scoped.
    # But wait, checking context is better.
    # The dropdown items usually look like: <a href="index_vX.html" ... class="... group/item ..."> ... </a>
    
    item_pattern = r'(<a\s+href="index_v(3|4|5|6|7|8|9|11|12|13|17)\.html"[^>]*?class="[^"]*group/item[^"]*".*?</a>)'
    
    # We replace with empty string
    content = re.sub(item_pattern, '', content, flags=re.DOTALL)
    
    # --- 3. Update Next/Prev Buttons ---
    
    if filename in visible_chain:
        curr_idx = visible_chain.index(filename)
        
        # Determine Prev
        if curr_idx > 0:
            prev_file = visible_chain[curr_idx - 1]
            prev_link = prev_file
        else:
            prev_file = None # No prev
            
        # Determine Next
        if curr_idx < len(visible_chain) - 1:
            next_file = visible_chain[curr_idx + 1]
            next_link = next_file
        else:
            next_file = None
            
        # Replace Prev Button Link
        # Pattern: <a href="..." ... title="Phiên bản trước">
        if prev_file:
            # Update existing href
            # Look for <a href="[^"]*" ... title="Phiên bản trước">
            # We want to enable it if it was disabled? No, assuming standard structure.
            prev_btn_pattern = r'(<a\s+href=")[^"]*("\s+[^>]*title="Phiên bản trước">)'
            if re.search(prev_btn_pattern, content):
                content = re.sub(prev_btn_pattern, f'\\1{prev_link}\\2', content)
        
        # Replace Next Button Link
        # Pattern: <a href="..." ... title="Phiên bản tiếp theo">
        if next_file:
             next_btn_pattern = r'(<a\s+href=")[^"]*("\s+[^>]*title="Phiên bản tiếp theo">)'
             if re.search(next_btn_pattern, content):
                content = re.sub(next_btn_pattern, f'\\1{next_link}\\2', content)
                
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

# Run process
all_files = [f for f in os.listdir(base_dir) if f.startswith('index') and f.endswith('.html')]

for f in all_files:
    # Optional: only update visible files? 
    # User said "hide ... from dropdown", implying we should update ALL files so their dropdowns are clean.
    # But strictly speaking we only care about visible files because user won't nav to hidden ones.
    # Let's update all to be safe and consistent.
    update_file(os.path.join(base_dir, f))
