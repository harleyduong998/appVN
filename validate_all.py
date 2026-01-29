import os

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

print("=" * 60)
print("📋 BÁO CÁO KIỂM TRA HTML FILES")
print("=" * 60)

total_files = 0
files_with_v11 = 0
files_with_issues = []

for filename in html_files:
    if os.path.exists(filename):
        total_files += 1
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        has_v11 = 'index_v11.html' in content
        if has_v11:
            files_with_v11 += 1
        
        # Kiểm tra trùng lặp
        v8_count = content.count('href="index_v8.html"')
        v9_count = content.count('href="index_v9.html"')
        v10_count = content.count('href="index_v10.html"')
        v11_count = content.count('href="index_v11.html"')
        
        issues = []
        if not has_v11:
            issues.append("Thiếu V11")
        if v8_count > 1:
            issues.append(f"V8 trùng ({v8_count}x)")
        if v9_count > 1:
            issues.append(f"V9 trùng ({v9_count}x)")
        if v10_count > 1:
            issues.append(f"V10 trùng ({v10_count}x)")
        if v11_count > 1:
            issues.append(f"V11 trùng ({v11_count}x)")
        
        status = "✅ OK" if not issues else "⚠️  CÓ LỖI"
        print(f"\n{filename:20} {status}")
        if issues:
            files_with_issues.append(filename)
            for issue in issues:
                print(f"  - {issue}")

print("\n" + "=" * 60)
print(f"📊 TỔNG KẾT:")
print(f"  • Tổng số file: {total_files}/11")
print(f"  • File có V11: {files_with_v11}/{total_files}")
print(f"  • File có lỗi: {len(files_with_issues)}")
if files_with_issues:
    print(f"\n⚠️  Các file cần fix:")
    for f in files_with_issues:
        print(f"  - {f}")
else:
    print(f"\n✅ TẤT CẢ FILE ĐỀU OK!")
print("=" * 60)
