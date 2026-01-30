import re
import os

def update_nav_buttons():
    # Define the orderly sequence of versions as they appear in the V17 dropdown
    version_order = [
         'index_v1.html',  # V1
         'index_v2.html',  # V2
         'index_v3.html',  # V3
         'index_v4.html',  # V4
         'index_v5.html',  # V5
         'index_v6.html',  # V6
         'index_v7.html',  # V7
         'index_v8.html',  # V8
         'index_v9.html',  # V9
         'index_v10.html', # V10 (was index.html)
         'index_v11.html', # V11
         'index_v12.html', # V12
         'index_v13.html', # V13
         'index_v14.html', # V14
         'index_v15.html', # V15
         'index_v16.html', # V16
         'index_v17.html'  # V17
    ]
    
    # We will assume circular navigation
    # Prev of First is Last
    # Next of Last is First
    
    directory = '.'
    
    print(f"Updating navigation buttons for {len(version_order)} files...")
    
    for i, current_file in enumerate(version_order):
        prev_file = version_order[i-1] # Python handles -1 correctly as last element
        next_file = version_order[(i+1) % len(version_order)]
        
        # Read file
        file_path = os.path.join(directory, current_file)
        if not os.path.exists(file_path):
            print(f"Skipping {current_file} (not found)")
            continue
            
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update Prev Button
        # Look for the link with title="Phiên bản trước"
        # Regex: <a href="[^"]*" [^>]*title="Phiên bản trước"[^>]*>
        # We capture the whole tag to replace the href
        
        # Strategy: matching the href attribute specifically within the tag context is hard with pure regex without parsing.
        # But since the structure is consistent:
        # <a href="OLD_LINK" ... title="Phiên bản trước">
        # We can find the tag containing the title, then replace the href in that tag.
        
        # Prev Button Regex
        # Matches: <a href="..." ... title="Phiên bản trước">
        # We use a lookahead or just flexible matching.
        
        prev_pattern = r'(<a\s+href=")([^"]+)("\s+[^>]*title="Phiên bản trước"[^>]*>)'
        
        if re.search(prev_pattern, content):
            content = re.sub(prev_pattern, f'\\1{prev_file}\\3', content)
        else:
            print(f"Warning: Prev button not found in {current_file}")
            
        # Next Button Regex
        next_pattern = r'(<a\s+href=")([^"]+)("\s+[^>]*title="Phiên bản tiếp theo"[^>]*>)'
        
        if re.search(next_pattern, content):
            content = re.sub(next_pattern, f'\\1{next_file}\\3', content)
        else:
            print(f"Warning: Next button not found in {current_file}")
            
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        # If current file is index_v1.html, also update index.html
        if current_file == 'index_v1.html':
            index_path = os.path.join(directory, 'index.html')
            if os.path.exists(index_path):
                 with open(index_path, 'w', encoding='utf-8') as f:
                    f.write(content) # Same content as v1

            
    print("Navigation update complete.")

if __name__ == "__main__":
    update_nav_buttons()
