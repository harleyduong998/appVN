import re

filename = 'index_v11.html'

print(f"🔧 Đang chuyển icon từ solid sang regular (border) trong {filename}...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Đếm số lượng icon solid
    solid_count = content.count('fa-solid')
    
    # Thay thế fa-solid thành fa-regular
    new_content = content.replace('fa-solid', 'fa-regular')
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Đã chuyển {solid_count} icon từ solid sang regular")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất!")
