import re
import os

files = ['index_v20.html', 'index_v21.html']
new_link = '''
                            <a href="index_v22.html"
                                class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                                <div
                                    class="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center font-bold text-xs shadow-sm">
                                    <span
                                        class="bg-gradient-to-br from-blue-600 to-blue-400 bg-clip-text text-transparent">V22</span>
                                </div>
                                <div class="text-sm font-medium text-slate-700">Dual Tone Blue</div>
                            </a>'''

for file_path in files:
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'index_v22.html' in content:
        print(f"V22 link already exists in {file_path}")
        continue
        
    # Find the V21 link block
    # We look for the closing </a> of the V21 link
    v21_link_pattern = r'(<a href="index_v21\.html".*?</a>)'
    
    match = re.search(v21_link_pattern, content, re.DOTALL)
    if match:
        end_pos = match.end()
        # Insert V22 after V21
        new_content = content[:end_pos] + '\n' + new_link + content[end_pos:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Added V22 link to {file_path}")
    else:
        print(f"Could not find V21 link in {file_path}")
