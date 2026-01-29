import re

# Đọc file HTML
with open('index_v9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Giảm size icon box từ w-14 h-14 xuống w-12 h-12
content = content.replace('w-14 h-14 rounded-2xl', 'w-12 h-12 rounded-2xl')

# 2. Giảm size icon từ text-2xl xuống text-xl
content = content.replace('text-2xl"></i>', 'text-xl"></i>')

# 3. Giảm độ dày title từ font-bold xuống font-semibold
pattern = r'<h3 class="font-bold text-slate-800'
replacement = '<h3 class="font-semibold text-slate-800'
content = content.replace(pattern, replacement)

# Ghi lại file
with open('index_v9.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Đã cập nhật thành công!")
print("- Icon box: w-14 h-14 → w-12 h-12")
print("- Icon size: text-2xl → text-xl")
print("- Title weight: font-bold → font-semibold")
