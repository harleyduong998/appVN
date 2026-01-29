import re

filename = 'index_v12.html'

print(f"🔧 Đang giảm khoảng cách giữa icon và text...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Thay thế mr-5 thành mr-2 trong các icon box
    old_pattern = 'mr-5 group-hover'
    new_pattern = 'mr-2 group-hover'
    
    count = content.count(old_pattern)
    content = content.replace(old_pattern, new_pattern)
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Đã giảm margin-right từ mr-5 xuống mr-2")
    print(f"✅ Cập nhật {count} icon boxes")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất giảm khoảng cách!")
