import re
import os

files = ['index.html', 'index_v20.html', 'index_v21.html', 'index_v22.html']
new_link = '<a href="index_v22.html" class="block px-4 py-2 text-sm text-slate-700 hover:bg-slate-50 hover:text-blue-600">V22 - Dual Tone Blue</a>'

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'index_v22.html' in content and file_path != 'index_v22.html':
        print(f"V22 link already exists in {file_path}")
        continue

    # Find the displayDropdown div
    # We look for the closing div of the dropdown or the last link
    # Pattern: Look for the last <a href="index_v..." ...>...</a> inside the dropdown area
    # Robust approach: Find id="displayDropdown", then find the last </a> inside it.
    
    dropdown_match = re.search(r'(id="displayDropdown"[^>]*>)(.*?)(</div>)', content, re.DOTALL)
    
    if dropdown_match:
        dropdown_content = dropdown_match.group(2)
        if 'index_v22.html' not in dropdown_content:
            # Find the last </a>
            last_a_match = list(re.finditer(r'<a href="[^"]+".*?</a>', dropdown_content, re.DOTALL))
            if last_a_match:
                last_a = last_a_match[-1]
                end_pos = last_a.end()
                
                # Insert the new link after the last one
                new_dropdown_content = dropdown_content[:end_pos] + '\n' + ' ' * 24 + new_link + dropdown_content[end_pos:]
                
                # Replace the dropdown content in the main content
                full_dropdown_block = dropdown_match.group(0).replace(dropdown_content, new_dropdown_content)
                content = content.replace(dropdown_match.group(0), full_dropdown_block)
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Added V22 link to {file_path}")
            else:
                print(f"Could not find any links in dropdown of {file_path}")
        else:
            print(f"V22 link already in dropdown of {file_path}")
    else:
        print(f"Could not find displayDropdown in {file_path}")
