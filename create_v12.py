import re

filename = 'index_v12.html'

print(f"🎨 Đang tùy chỉnh {filename}...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Thay đổi title
    content = content.replace('<title>Dashboard V11 - Appvn</title>', '<title>Dashboard V12 - Appvn</title>')
    print("✅ Đã cập nhật title thành V12")
    
    # 2. Tăng stroke width từ 1.5 lên 2.0 trong CSS
    content = content.replace('stroke-width: 1.5;', 'stroke-width: 2.0;')
    print("✅ Đã tăng stroke width lên 2.0")
    
    # 3. Tăng stroke width trong JavaScript từ 1.5 lên 2.0
    content = content.replace("icon.style.strokeWidth = '1.5';", "icon.style.strokeWidth = '2.0';")
    print("✅ Đã tăng stroke width trong JavaScript lên 2.0")
    
    # 4. Giảm font-weight từ font-bold (700) xuống font-semibold (600)
    # Tìm tất cả h3 với font-bold và thay bằng font-semibold
    content = re.sub(
        r'(<h3 class="[^"]*?)font-bold([^"]*?")',
        r'\1font-semibold\2',
        content
    )
    print("✅ Đã giảm font-weight từ bold xuống semibold")
    
    # 5. Giảm gap từ gap-3 xuống gap-2
    content = content.replace('gap-3 h-[85px]', 'gap-2 h-[85px]')
    print("✅ Đã giảm gap từ gap-3 xuống gap-2")
    
    # 6. Cập nhật dropdown để highlight V12
    # Tìm V11 entry và remove bg-slate-50
    v11_pattern = r'(<a href="index_v11\.html"[^>]*class="[^"]*) bg-slate-50([^"]*")'
    content = re.sub(v11_pattern, r'\1\2', content)
    
    # Thêm V12 entry vào dropdown (sau V11)
    v12_entry = '''                        <a href="index_v12.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-teal-500 to-cyan-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V12</div>
                            <div class="text-sm font-medium text-slate-700">Refined</div>
                        </a>'''
    
    # Tìm vị trí sau V11 entry và thêm V12
    v11_end_pattern = r'(</a>\s*</div>\s*</div>\s*</div>\s*<script>)'
    content = re.sub(v11_end_pattern, v12_entry + '\n                    \\1', content)
    print("✅ Đã thêm V12 vào dropdown")
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ File {filename} đã được tạo và tùy chỉnh!")
    print("\n📋 Tóm tắt thay đổi:")
    print("  • Stroke width: 1.5 → 2.0")
    print("  • Font weight: bold → semibold")
    print("  • Gap: gap-3 → gap-2")
    print("  • Dropdown: Thêm V12 entry")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất tạo V12!")
