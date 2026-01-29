import re

# Đọc header chuẩn từ index_v11.html
with open('index_v11.html', 'r', encoding='utf-8') as f:
    v11_content = f.read()

# Trích xuất phần script + Right Side từ index_v11.html
script_and_right_pattern = r'(<script>.*?</script>\s*</div>\s*<!-- Right Side -->.*?</header>)'
script_and_right_match = re.search(script_and_right_pattern, v11_content, re.DOTALL)

if not script_and_right_match:
    print("❌ Không tìm thấy script và Right Side trong index_v11.html")
    exit(1)

script_and_right_section = script_and_right_match.group(1)

files_to_fix = [
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
]

print("🔧 Đang khôi phục script và user profile...\n")

for filename in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm vị trí sau dropdown để thêm script và Right Side
        # Pattern: tìm kết thúc của dropdown và thay thế đến </header>
        pattern = r'(</div>\s*</div>\s*</div>)\s*</header>'
        
        def add_script_and_right(match):
            dropdown_closing = match.group(1)
            return f"{dropdown_closing}\n\n            {script_and_right_section}"
        
        new_content = re.sub(pattern, add_script_and_right, content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename} - Đã khôi phục")
        else:
            print(f"⚠️  {filename} - Không có thay đổi")
            
    except FileNotFoundError:
        print(f"❌ {filename} - File không tồn tại")
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất khôi phục!")
