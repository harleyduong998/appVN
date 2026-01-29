import re

# Dropdown template chuẩn - CHỈ PHẦN DROPDOWN, KHÔNG BAO GỒM SCRIPT VÀ RIGHT SIDE
dropdown_only = '''<div id="versionDropdown"
                    class="absolute top-full left-0 mt-2 w-64 bg-white rounded-lg shadow-xl border border-slate-200 overflow-hidden hidden z-50 animate-in fade-in slide-in-from-top-2 duration-200"
                    onclick="event.stopPropagation()">
                    <div class="p-1">
                        <a href="index.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v1_active}">
                            <div
                                class="w-8 h-8 rounded bg-blue-100 text-blue-600 flex items-center justify-center font-bold text-xs">
                                V1</div>
                            <div class="text-sm font-medium text-slate-700">Original</div>
                        </a>
                        <a href="index_v2.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v2_active}">
                            <div
                                class="w-8 h-8 rounded bg-slate-100 text-slate-600 flex items-center justify-center font-bold text-xs">
                                V2</div>
                            <div class="text-sm font-medium text-slate-700">Clean White</div>
                        </a>
                        <a href="index_v3.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v3_active}">
                            <div
                                class="w-8 h-8 rounded bg-amber-100 text-amber-600 flex items-center justify-center font-bold text-xs">
                                V3</div>
                            <div class="text-sm font-medium text-slate-700">Colorful Waves</div>
                        </a>
                        <a href="index_v4.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v4_active}">
                            <div
                                class="w-8 h-8 rounded bg-purple-100 text-purple-600 flex items-center justify-center font-bold text-xs">
                                V4</div>
                            <div class="text-sm font-medium text-slate-700">Network</div>
                        </a>
                        <a href="index_v5.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v5_active}">
                            <div
                                class="w-8 h-8 rounded bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold text-xs">
                                V5</div>
                            <div class="text-sm font-medium text-slate-700">Minimalist</div>
                        </a>
                        <a href="index_v6.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v6_active}">
                            <div
                                class="w-8 h-8 rounded bg-slate-800 text-white flex items-center justify-center font-bold text-xs">
                                V6</div>
                            <div class="text-sm font-medium text-slate-700">Professional</div>
                        </a>
                        <a href="index_v7.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v7_active}">
                            <div
                                class="w-8 h-8 rounded bg-cyan-700 text-white flex items-center justify-center font-bold text-xs">
                                V7</div>
                            <div class="text-sm font-medium text-slate-700">Compact</div>
                        </a>
                        <a href="index_v8.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v8_active}">
                            <div
                                class="w-8 h-8 rounded bg-white text-slate-800 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V8</div>
                            <div class="text-sm font-medium text-slate-700">White & Shadow</div>
                        </a>
                        <a href="index_v9.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v9_active}">
                            <div
                                class="w-8 h-8 rounded bg-[#F7F8F9] text-slate-800 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V9</div>
                            <div class="text-sm font-medium text-slate-700">Colored Box</div>
                        </a>
                        <a href="index_v10.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v10_active}">
                            <div
                                class="w-8 h-8 rounded bg-white text-amber-500 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V10</div>
                            <div class="text-sm font-medium text-slate-700">Icon Box</div>
                        </a>
                        <a href="index_v11.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors{v11_active}">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-emerald-500 to-teal-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V11</div>
                            <div class="text-sm font-medium text-slate-700">Icon Box V2</div>
                        </a>
                    </div>
                </div>'''

files_to_fix = [
    ('index.html', 'v1'),
    ('index_v2.html', 'v2'),
    ('index_v3.html', 'v3'),
    ('index_v4.html', 'v4'),
    ('index_v5.html', 'v5'),
    ('index_v6.html', 'v6'),
    ('index_v7.html', 'v7'),
    ('index_v8.html', 'v8'),
    ('index_v9.html', 'v9'),
    ('index_v10.html', 'v10'),
]

print("🔧 Đang fix dropdown (chỉ thay thế phần dropdown)...\n")

for filename, active_version in files_to_fix:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Tạo dropdown với version active phù hợp
        active_flags = {
            'v1_active': ' bg-slate-50' if active_version == 'v1' else '',
            'v2_active': ' bg-slate-50' if active_version == 'v2' else '',
            'v3_active': ' bg-slate-50' if active_version == 'v3' else '',
            'v4_active': ' bg-slate-50' if active_version == 'v4' else '',
            'v5_active': ' bg-slate-50' if active_version == 'v5' else '',
            'v6_active': ' bg-slate-50' if active_version == 'v6' else '',
            'v7_active': ' bg-slate-50' if active_version == 'v7' else '',
            'v8_active': ' bg-slate-50' if active_version == 'v8' else '',
            'v9_active': ' bg-slate-50' if active_version == 'v9' else '',
            'v10_active': ' bg-slate-50' if active_version == 'v10' else '',
            'v11_active': '',
        }
        
        new_dropdown = dropdown_only.format(**active_flags)
        
        # Pattern chính xác hơn - CHỈ THAY THẾ DROPDOWN, KHÔNG ĐỘNG VÀO SCRIPT VÀ RIGHT SIDE
        pattern = r'<div id="versionDropdown"[^>]*>.*?</div>\s*</div>\s*</div>'
        
        new_content = re.sub(pattern, new_dropdown + '\n            </div>', content, flags=re.DOTALL)
        
        if new_content != content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename} - Đã fix dropdown")
        else:
            print(f"⚠️  {filename} - Không có thay đổi")
            
    except FileNotFoundError:
        print(f"❌ {filename} - File không tồn tại")
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất fix dropdown!")
