import re

def fix_v10_link():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The issue: <a href="index.html"... > ... V10 ... </a>
    # We want <a href="index_v10.html"... > ... V10 ... </a>
    
    # Pattern to match the V10 block with wrong href
    # <a href="index.html"\s+class="[^"]*">\s*<div[^>]*>\s*V10
    
    pattern = r'(<a href=")index.html("[\s\S]*?V10)'
    
    # We replace only if it matches V10 context
    if re.search(pattern, content):
        content = re.sub(pattern, r'\1index_v10.html\2', content)
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_v10_link()
