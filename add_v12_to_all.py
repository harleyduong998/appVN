import re

# V12 dropdown entry
v12_entry = '''                        <a href="index_v12.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-teal-500 to-cyan-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V12</div>
                            <div class="text-sm font-medium text-slate-700">Refined</div>
                        </a>
'''

files_to_update = [
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
    'index_v11.html',
]

print("🔧 Đang thêm V12 vào dropdown của tất cả các file...\n")

for filename in files_to_update:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm vị trí cuối của dropdown (trước </div></div></div>)
        # Pattern: tìm V11 entry và thêm V12 sau nó
        pattern = r'(Icon Box V2</div>\s*</a>)'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, r'\1\n' + v12_entry, content)
            
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ {filename} - Đã thêm V12")
            else:
                print(f"⚠️  {filename} - Không có thay đổi")
        else:
            print(f"⚠️  {filename} - Không tìm thấy pattern")
            
    except FileNotFoundError:
        print(f"❌ {filename} - File không tồn tại")
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất thêm V12 vào tất cả dropdown!")
