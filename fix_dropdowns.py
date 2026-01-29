import re

# Template HTML cho V11 entry
v11_entry = '''                        <a href="index_v11.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-emerald-500 to-teal-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V11</div>
                            <div class="text-sm font-medium text-slate-700">Icon Box V2</div>
                        </a>'''

files_to_fix = [
    ('index.html', 'V1', 'Original'),
    ('index_v2.html', 'V2', 'Clean White'),
    ('index_v3.html', 'V3', 'Colorful Waves'),
    ('index_v4.html', 'V4', 'Network'),
    ('index_v5.html', 'V5', 'Minimalist'),
    ('index_v6.html', 'V6', 'Professional'),
]

print("🔧 Đang fix các file HTML...\n")

for filename, active_version, active_label in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Kiểm tra xem đã có V11 chưa
        if 'index_v11.html' in content:
            print(f"✅ {filename} - Đã có V11, bỏ qua")
            continue
        
        # Tìm vị trí cuối dropdown (trước </div></div>)
        # Pattern: tìm V7 hoặc V10 link cuối cùng
        pattern = r'(</a>)\s*</div>\s*</div>\s*</div>\s*<script>'
        
        def add_v11(match):
            return f"</a>\n{v11_entry}\n                    </div>\n                </div>\n            </div>\n\n            <script>"
        
        new_content = re.sub(pattern, add_v11, content)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename} - Đã thêm V11")
        else:
            print(f"⚠️  {filename} - Không tìm thấy vị trí để thêm V11")
            
    except FileNotFoundError:
        print(f"❌ {filename} - File không tồn tại")
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất!")
