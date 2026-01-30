import os
import re

# Directory
base_dir = r'd:\AIDesign\AppVN'

# V20 Link HTML to insert
v20_html = """
                            <a href="index_v20.html"
                                class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                                <div
                                    class="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center font-bold text-xs shadow-sm">
                                    <span
                                        class="bg-gradient-to-br from-green-500 to-emerald-400 bg-clip-text text-transparent">V20</span>
                                </div>
                                <div class="text-sm font-medium text-slate-700">Module Colors</div>
                            </a>"""

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # check if V20 already exists
    if 'href="index_v20.html"' in content:
        print(f"Skipping {os.path.basename(filepath)}: V20 already present")
        return

    # Find V19 link block
    # We look for the closing </a> tag of V19 and insert after it.
    # V19 block roughly:
    # <a href="index_v19.html" ... > ... </a>
    
    # Regex to find V19 block. 
    # It catches <a href="index_v19.html" ... </a>
    # We use non-greedy match for content inside <a>...</a>
    
    pattern = r'(<a\s+href="index_v19\.html".*?</a>)'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        v19_block = match.group(1)
        # Check if there is a newline after
        replacement = v19_block + "\n" + v20_html
        new_content = content.replace(v19_block, replacement)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")
    else:
        print(f"Warning: Could not find V19 link in {os.path.basename(filepath)}")

# List all index*.html files
files = [f for f in os.listdir(base_dir) if f.startswith('index') and f.endswith('.html')]

for file in files:
    update_file(os.path.join(base_dir, file))
