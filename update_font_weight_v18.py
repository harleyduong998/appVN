
file_path = 'd:/AIDesign/AppVN/index_v18.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
count = 0

for line in lines:
    # Target the specific h3 class structure used in module cards
    if '<h3 class="font-bold text-slate-800' in line:
        new_line = line.replace('font-bold', 'font-semibold')
        count += 1
    else:
        new_line = line
    new_lines.append(new_line)

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Updated {count} instances of font-bold to font-semibold in index_v18.html")
