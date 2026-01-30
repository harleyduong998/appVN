import re
import os

def standardize_dropdowns():
    source_file = 'index_v17.html'
    
    # 1. Read Source Content
    with open(source_file, 'r', encoding='utf-8') as f:
        v17_content = f.read()

    # Extract the inner HTML of the dropdown
    # Looking for content between <div id="versionDropdown" ... > and the closing </div>
    # Structure:
    # <div id="versionDropdown" ... onclick="event.stopPropagation()">
    #    CONTENT
    # </div>
    # <script>
    
    start_marker = 'id="versionDropdown"'
    end_marker = '<script>'
    
    start_idx = v17_content.find(start_marker)
    script_idx = v17_content.find(end_marker, start_idx)
    
    if start_idx == -1 or script_idx == -1:
        print("Could not find dropdown in source file")
        return

    # Find the end of the opening tag
    opening_tag_end = v17_content.find('>', start_idx)
    
    # Find the last </div> before the script
    # We assume the layout is ... </div> \n \n <script>
    dropdown_end_idx = v17_content.rfind('</div>', start_idx, script_idx) # This is the closing of "versionDropdown"
    
    # The content we want to propagate is the inner DIV
    # <div class="p-1 max-h-80 overflow-y-auto"> ... </div>
    
    # Actually, let's just grab the whole inner HTML
    master_html = v17_content[opening_tag_end+1 : dropdown_end_idx]
    
    # Clean the master HTML: Remove "bg-slate-50" from the V17 link
    # V17 link line: ... class="... bg-slate-50">
    master_html_clean = master_html.replace(' bg-slate-50', '')

    # 2. Identify Target Files
    directory = '.'
    files = [f for f in os.listdir(directory) if f.startswith('index') and f.endswith('.html') and f != 'index_v17.html']
    
    print(f"Updating {len(files)} files...")

    for filename in files:
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find local dropdown location
        f_start_idx = content.find(start_marker)
        f_script_idx = content.find(end_marker, f_start_idx)
        
        if f_start_idx == -1 or f_script_idx == -1:
            print(f"Skipping {filename} (dropdown structure not found)")
            continue
            
        f_opening_tag_end = content.find('>', f_start_idx)
        f_dropdown_end_idx = content.rfind('</div>', f_start_idx, f_script_idx)
        
        # Prepare Active HTML
        # In current filename, find the link to itself and add bg-slate-50
        # Check href.
        # href="index.html" for index.html
        # href="index_vX.html" for index_vX.html
        
        current_html = master_html_clean
        
        search_href = f'href="{filename}"'
        
        # We need to inject bg-slate-50 into the class of the link matching this href
        # Regex replacement
        # <a href="FILENAME" ... class="... transition-colors">
        # Replace "transition-colors" with "transition-colors bg-slate-50" 
        # (Assuming the structure matches V17's links which end with transition-colors or similar)
        
        # Let's see V17 link structure:
        # class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors"
        
        # Helper function to add active class
        def hl_replacer(match):
             tag = match.group(0)
             # Check if we already added the active class (avoid double adding)
             if 'transition-colors bg-slate-50' not in tag:
                 return tag.replace('transition-colors', 'transition-colors bg-slate-50')
             return tag

        if search_href in current_html:
             # Add bg-slate-50 to the class list of this specific link
             # Regex to find the specific A tag opening
             import re
             pattern = re.compile(r'<a\s+href="' + re.escape(filename) + r'"[^>]*>', re.IGNORECASE)
             current_html = pattern.sub(hl_replacer, current_html)
        else:
            print(f"Warning: Self-link {filename} not found in dropdown list")

        # Reconstruct Content
        new_content = content[:f_opening_tag_end+1] + current_html + content[f_dropdown_end_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
    print("Done.")

if __name__ == "__main__":
    standardize_dropdowns()
