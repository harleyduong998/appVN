import re

filename = 'index_v13.html'

print(f"🎨 Đang chuyển đổi V13 (Icon luôn ở trạng thái hover của V12)...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title
    content = content.replace('<title>Dashboard V12 - Appvn</title>', '<title>Dashboard V13 - Appvn</title>')

    # 2. Logic để thay đổi class của icon container
    # Pattern tìm div chứa icon classes
    # Tìm class cụ thể để replace an toàn
    # Class V12: w-14 h-14 rounded-2xl bg-white border border-slate-100 shadow-[...] flex items-center justify-center text-{color} flex-shrink-0 z-10 mr-2 group-hover:bg-gradient-to-br from-{color} to-{color} group-hover:text-white transition-colors duration-300
    
    # Bước 1: Loại bỏ bg-white, border, border-slate-100
    content = content.replace('bg-white border border-slate-100', '')
    
    # Bước 2: Thay text-{color} bằng text-white
    # Regex tìm text-{color} trong ngữ cảnh của icon box (sau justify-center)
    # Lưu ý: text-{color} cũng có thể xuất hiện ở places khác, nên cần cẩn thận.
    # Pattern: justify-center text-xxx-xxx flex-shrink-0
    content = re.sub(r'(justify-center) text-[a-z]+-\d+ (flex-shrink-0)', r'\1 text-white \2', content)
    
    # Bước 3: Thay group-hover:bg-gradient-to-br thành bg-gradient-to-br
    content = content.replace('group-hover:bg-gradient-to-br', 'bg-gradient-to-br')
    
    # Bước 4: Xóa group-hover:text-white (vì đã set text-white rồi)
    content = content.replace('group-hover:text-white', '')
    
    # Bước 5: Thêm V13 Entry vào dropdown
    # Remove bg-slate-50 from V12 entry
    v12_pattern = r'(<a href="index_v12\.html"[^>]*class="[^"]*) bg-slate-50([^"]*")'
    content = re.sub(v12_pattern, r'\1\2', content)
    
    v13_entry = '''                        <a href="index_v13.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-indigo-500 to-violet-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V13</div>
                            <div class="text-sm font-medium text-slate-700">Gradient Icon</div>
                        </a>'''
    
    v12_end_pattern = r'(Refined</div>\s*</a>)'
    content = re.sub(v12_end_pattern, r'\1\n' + v13_entry, content)
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"✅ Đã tạo index_v13.html thành công!")
    print(f"✅ Icon containers đã chuyển sang style gradient mặc định.")

except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")
