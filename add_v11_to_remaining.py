import re

# Template HTML cho V11 entry
v11_entry = '''                        <a href="index_v11.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-emerald-500 to-teal-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V11</div>
                            <div class="text-sm font-medium text-slate-700">Icon Box V2</div>
                        </a>'''

files_to_update = ['index_v7.html', 'index_v8.html', 'index_v9.html', 'index_v10.html']

print("🔧 Đang thêm V11 vào các file còn thiếu...\n")

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem đã có V11 chưa
        if 'index_v11.html' in content:
            print(f"✅ {filename} - Đã có V11")
            continue
        
        # Tìm vị trí sau V10 link cuối cùng để thêm V11
        # Pattern tìm V10 link và thêm V11 ngay sau đó
        pattern = r'(<a href="index_v10\.html".*?</a>)\s*(</div>\s*</div>)'
        
        def add_v11_after_v10(match):
            v10_link = match.group(1)
            closing_divs = match.group(2)
            return f"{v10_link}\n{v11_entry}\n                    {closing_divs}"
        
        new_content = re.sub(pattern, add_v11_after_v10, content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename} - Đã thêm V11")
        else:
            print(f"⚠️  {filename} - Không tìm thấy vị trí phù hợp")
            
    except FileNotFoundError:
        print(f"❌ {filename} - File không tồn tại")
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất cập nhật!")
