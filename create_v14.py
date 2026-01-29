import re

filename = 'index_v14.html'

print(f"🎨 Đang thêm quarter circle decoration cho {filename}...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Update Title
    content = content.replace('<title>Dashboard V12 - Appvn</title>', '<title>Dashboard V14 - Appvn</title>')
    
    # 2. Logic thêm quarter circle
    # Tìm thẻ <a> module
    # Pattern: <a href="modules/[^"]+" class="[^"]*hover:border-([a-z]+)-([0-9]+)[^"]*">
    # Lấy color và shade từ hover:border
    # Thêm div quarter circle vào ngay sau thẻ mở <a> (hoặc trước thẻ đóng </a> - nhưng trước nội dung thì tốt hơn nếu dùng absolute z-0)
    # Cấu trúc V12:
    # <a ... relative overflow-hidden ...>
    #    <div ... icon ...>...</div>
    #    <div ... text ...>...</div>
    # </a>
    # Tôi sẽ thêm div quarter circle vào đầu tiên bên trong thẻ <a>
    
    def add_decoration(match):
        full_match = match.group(0) # Toàn bộ thẻ a mở
        
        # Extract color from hover:border-xxx-xxx or text-xxx-xxx
        # Ưu tiên hover:border vì nó nằm ngay trong class của thẻ a
        color_match = re.search(r'hover:border-([a-z]+)-([0-9]+)', full_match)
        if not color_match:
             # Try text color inside internal div (phức tạp hơn vì regex match thẻ a mở thôi)
             # Fallback: check if we captured the whole block? No, substitute on opening tag implies we only have opening tag.
             # But wait, I can use a simpler approach.
             # Search for the class string in the opening tag.
             return full_match 
        
        color_name = color_match.group(1)
        # shade = color_match.group(2) # Thường là 500, 600. Ta sẽ dùng shade 500 hoặc giữ nguyên shade mà giảm opacity.
        # User yêu cầu: "đồng màu với màu icon nhưng nhạt nhạt"
        # Icon thường là text-{color}-500 hoặc 600.
        # Ta sẽ dùng bg-{color}-500/10 (opacity 10%) hoặc /5.
        
        # Quarter circle style: absolute bottom-0 right-0 w-20 h-20 bg-{color}-500/10 rounded-tl-full -z-0 pointer-events-none
        # Note: z-0 might cover content if content doesn't have z-index.
        # Icon box in V12 has z-10. Text div has z-0? 
        # Text div: <div class="flex-1 min-w-0">. No z-index.
        # So background decoration needs z-0. Text needs z-10 or decoration needs to be BEFORE text?
        # If absolute, order in DOM matters if z-index is auto. Later elements are on top.
        # But if we use z-0, and text is z-auto (default 0), and parent is stacking context...
        # Safer: set z-0 for decoration, and ensure icons/text have z-10 or relative.
        # Icon box V12 HAS z-10. Text does NOT.
        # So I should add relative z-10 to text div?
        # Or just put decoration as the FIRST child of <a>?
        # If decoration is first child, and absolute, subsequent static children (text) will be on top?
        # Yes, usually.
        
        decoration_div = f'\n                <div class="absolute -bottom-2 -right-2 w-16 h-16 bg-{color_name}-500/10 rounded-full z-0 pointer-events-none"></div>'
        # Tôi dùng rounded-full và đặt vị trí offset để tạo cảm giác quarter circle mềm mại hơn.
        # Hoặc style chính xác quarter circle: bottom-0 right-0 rounded-tl-full.
        # "quarter circle ở góc phải dưới" -> rounded-tl-full (top-left rounded của box ở góc phải dưới)
        
        decoration_div = f'\n                <div class="absolute bottom-0 right-0 w-12 h-12 bg-{color_name}-500/5 rounded-tl-full z-0 pointer-events-none"></div>'

        return full_match + decoration_div

    # Regex tìm thẻ a mở có chứa class hover:border
    # <a href="modules/sales.html" \n class="... hover:border-blue-500 ...">
    # Note: re.sub với func
    pattern = r'<a href="modules/[^"]+"\s+class="[^"]*hover:border-[a-z]+-[0-9]+[^"]*">'
    
    new_content = re.sub(pattern, add_decoration, content)
    
    # 3. Add V14 to Dropdown
    v13_pattern = r'(<a href="index_v13\.html"[^>]*class="[^"]*) bg-slate-50([^"]*")'
    new_content = re.sub(v13_pattern, r'\1\2', new_content)
    
    v14_entry = '''                        <a href="index_v14.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded bg-gradient-to-br from-rose-500 to-pink-500 text-white flex items-center justify-center font-bold text-xs shadow-sm">
                                V14</div>
                            <div class="text-sm font-medium text-slate-700">Quarter Circle</div>
                        </a>'''
    
    v13_end_pattern = r'(Gradient Icon</div>\s*</a>)'
    new_content = re.sub(v13_end_pattern, r'\1\n' + v14_entry, new_content)

    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"✅ Đã tạo index_v14.html với decoration quarter circle!")

except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")
