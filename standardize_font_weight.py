import re

filename = 'index_v12.html'

print(f"🔧 Đang chuẩn hóa font-weight cho tất cả module...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thay thế font-bold thành font-semibold trong các h3 module
    pattern = r'(<h3[^>]*class="[^"]*?)font-bold([^"]*text-slate-800 text-sm[^"]*")'
    replacement = r'\1font-semibold\2'
    
    new_content, count = re.subn(pattern, replacement, content)
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Đã thay thế {count} instance từ font-bold → font-semibold")
    print(f"✅ Tất cả module giờ đã có font-weight đồng nhất")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất chuẩn hóa font-weight!")
