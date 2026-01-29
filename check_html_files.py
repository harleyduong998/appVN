import os
import re

# Danh sách các file cần kiểm tra
html_files = [
    'index.html',
    'index_v2.html',
    'index_v3.html',
    'index_v4.html',
    'index_v5.html',
    'index_v6.html',
    'index_v7.html',
    'index_v8.html',
    'index_v9.html',
    'index_v10.html',
    'index_v11.html'
]

print("🔍 Kiểm tra các file HTML...\n")

for filename in html_files:
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem có V11 trong dropdown không
        has_v11 = 'index_v11.html' in content
        
        # Đếm số lần xuất hiện của mỗi version link
        v8_count = content.count('href="index_v8.html"')
        v9_count = content.count('href="index_v9.html"')
        v10_count = content.count('href="index_v10.html"')
        v11_count = content.count('href="index_v11.html"')
        
        status = "✅" if has_v11 and v8_count <= 1 and v9_count <= 1 and v10_count <= 1 and v11_count <= 1 else "⚠️"
        
        print(f"{status} {filename}")
        if not has_v11:
            print(f"   ❌ Thiếu V11 trong dropdown")
        if v8_count > 1:
            print(f"   ⚠️  V8 xuất hiện {v8_count} lần (trùng lặp)")
        if v9_count > 1:
            print(f"   ⚠️  V9 xuất hiện {v9_count} lần (trùng lặp)")
        if v10_count > 1:
            print(f"   ⚠️  V10 xuất hiện {v10_count} lần (trùng lặp)")
        if v11_count > 1:
            print(f"   ⚠️  V11 xuất hiện {v11_count} lần (trùng lặp)")
    else:
        print(f"❌ {filename} - File không tồn tại")

print(f"\n📊 Tổng số file: {len([f for f in html_files if os.path.exists(f)])}/11")
