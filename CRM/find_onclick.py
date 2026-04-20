import re
with open(r'd:\AIDesign\lixi\stuff2\CRM\CRM_Lead_v2.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
    
with open(r'd:\AIDesign\lixi\stuff2\CRM\lines_out.txt', 'w', encoding='utf-8') as out:
    for i, line in enumerate(lines):
        if 'openAddLeadModal' in line or 'openLeadModal' in line:
            out.write(f'Line {i+1}: {line.strip()}\n')
