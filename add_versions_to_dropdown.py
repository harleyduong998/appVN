import re

# Định nghĩa HTML cho các version mới
v8_html = '''                        <a href="index_v8.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-white text-slate-800 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V8</div>
                            <div class="text-sm font-medium text-slate-700">White & Shadow</div>
                        </a>'''

v9_html = '''                        <a href="index_v9.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-[#F7F8F9] text-slate-800 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V9</div>
                            <div class="text-sm font-medium text-slate-700">Colored Box</div>
                        </a>'''

v10_html = '''                        <a href="index_v10.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-white text-amber-500 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V10</div>
                            <div class="text-sm font-medium text-slate-700">Icon Box</div>
                        </a>'''

files_to_update = [
    ('index_v7.html', 'V7', 'Compact'),
    ('index_v8.html', 'V8', 'White & Shadow'),
    ('index_v9.html', 'V9', 'Colored Box'),
    ('index_v10.html', 'V10', 'Icon Box')
]

for filename, active_version, active_label in files_to_update:
    print(f"\n🔧 Đang cập nhật {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tìm vị trí kết thúc của dropdown (trước </div></div>)
        # Pattern: tìm V7 link cuối cùng trong dropdown
        v7_pattern = r'(<a href="index_v7\.html".*?</a>)\s*</div>\s*</div>'
        
        # Tạo replacement với V8, V9, V10
        def add_versions(match):
            v7_link = match.group(1)
            
            # Cập nhật class cho version đang active
            if active_version == 'V7':
                v7_link = v7_link.replace('transition-colors">', 'transition-colors bg-slate-50">')
            
            # Build các link mới
            v8_link = v8_html
            v9_link = v9_html
            v10_link = v10_html
            
            # Thêm bg-slate-50 cho version đang active
            if active_version == 'V8':
                v8_link = v8_link.replace('transition-colors">', 'transition-colors bg-slate-50">')
            elif active_version == 'V9':
                v9_link = v9_link.replace('transition-colors">', 'transition-colors bg-slate-50">')
            elif active_version == 'V10':
                v10_link = v10_link.replace('transition-colors">', 'transition-colors bg-slate-50">')
            
            return f"{v7_link}\n{v8_link}\n{v9_link}\n{v10_link}\n                    </div>\n                </div>"
        
        # Thực hiện replacement
        new_content = re.sub(v7_pattern, add_versions, content, flags=re.DOTALL)
        
        # Ghi lại file
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Đã cập nhật {filename} thành công!")
        
    except FileNotFoundError:
        print(f"⚠️  Không tìm thấy {filename}")
    except Exception as e:
        print(f"❌ Lỗi khi cập nhật {filename}: {str(e)}")

print("\n🎉 Hoàn tất cập nhật tất cả các file!")
