import re

def fix_version_switcher():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix V9 Entry
    # It currently looks like: <a href="index_v9.html" ... > ... V15 ... </a>
    # We want to change V15 back to V9 in that specific block.
    # Pattern: href="index_v9.html".*?>\s*<div.*?>\s*V15\s*</div>
    
    # Let's find the V9 block and replace V15 with V9.
    pattern_v9 = r'(href="index_v9.html"[^>]*>.*?<div[^>]*>\s*)V15(\s*</div>)'
    content = re.sub(pattern_v9, r'\1V9\2', content, flags=re.DOTALL)
    
    # 2. Insert V15 Entry
    # Find V14 entry and append V15 after it.
    # V14 entry: <a href="index_v14.html" ... </a>
    
    v14_end_pattern = r'(href="index_v14.html".*?</a>)'
    
    v15_entry = """
                        <a href="index_v15.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded-lg bg-gradient-to-br from-blue-500 to-indigo-600 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V15</div>
                            <div class="text-sm font-medium text-slate-700">MacOS Style</div>
                        </a>"""
    
    content = re.sub(v14_end_pattern, r'\1' + v15_entry, content, flags=re.DOTALL)
    
    # 3. Update Next/Prev buttons if needed
    # Prev: index_v8.html (Keep or change to v14?) -> Let's change to v14 since v15 follows v14.
    content = content.replace('href="index_v8.html"', 'href="index_v14.html"')
    
    # Next: index_v10.html -> Change to index.html (loop) or empty.
    content = content.replace('href="index_v10.html"', 'href="index.html"')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_version_switcher()
