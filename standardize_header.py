import re
import glob

source_file = 'index.html'

print(f"🔧 Đang chuẩn hóa Header từ {source_file} sang các file khác...\n")

# 1. Đọc và chuẩn bị Header mẫu
try:
    with open(source_file, 'r', encoding='utf-8') as f:
        source_content = f.read()

    # Extract Header block
    header_pattern = r'(<header[\s\S]*?</header>)'
    header_match = re.search(header_pattern, source_content)
    
    if not header_match:
        raise Exception("Không tìm thấy thẻ <header> trong index.html")
    
    raw_header = header_match.group(1)
    
    # Inline Styles & Cleanup
    # Add inline gradient style
    if 'style="background: linear-gradient' not in raw_header:
        raw_header = raw_header.replace('<header', '<header style="background: linear-gradient(135deg, #1B3DA1 0%, #0F256E 100%);"')
    
    # Remove 'gradient-header' class (optional/clean up)
    raw_header = raw_header.replace('gradient-header', '')
    
    # Remove 'bg-slate-50' from V1 link (to make a generic template)
    # V1 link: <a href="index.html" ... bg-slate-50">
    # Regex find href="index.html" ... class="... bg-slate-50"
    # We remove ' bg-slate-50' from the class string
    raw_header = re.sub(r'(<a href="index\.html"[^>]*class="[^"]*) bg-slate-50([^"]*")', r'\1\2', raw_header)
    
    print("✅ Đã trích xuất và xử lý Header mẫu")

except Exception as e:
    print(f"❌ Lỗi khi đọc index.html: {str(e)}")
    exit(1)

# 2. Xử lý các file đích
target_files = glob.glob('index_v*.html')

fa_link = '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">'

for filename in target_files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # A. Thêm Font Awesome nếu chưa có
        if 'font-awesome' not in content:
            # Insert before </head>
            content = content.replace('</head>', f'    {fa_link}\n</head>')
            print(f"   + Đã thêm Font Awesome vào {filename}")
            
        # B. Thay thế Header
        # Thay thế toàn bộ thẻ <header>...</header> cũ bằng Header mẫu đã customized
        
        # Customize Header cho file hiện tại (Active State)
        current_header = raw_header
        
        # Tìm link tương ứng với filename hiện tại và add bg-slate-50
        # Pattern: href="{filename}" ... class="..."
        # Note: glob returns relative path (e.g., index_v2.html). dropdown uses href="index_v2.html"
        escaped_filename = re.escape(filename)
        
        # Regex to find the link and append bg-slate-50 inside class attribute
        # We look for: <a href="FILENAME" ... class="SOMETHING">
        link_pattern = r'(<a href="' + escaped_filename + r'"[^>]*class="[^"]*)"'
        
        if re.search(link_pattern, current_header):
            current_header = re.sub(link_pattern, r'\1 bg-slate-50"', current_header)
        else:
            print(f"⚠️  Không tìm thấy link cho {filename} trong dropdown")
            
        # Replace in content
        if re.search(header_pattern, content):
            new_content = re.sub(header_pattern, lambda _: current_header, content, count=1)
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename} - Đã update Header")
        else:
            print(f"❌ {filename} - Không tìm thấy thẻ <header> cũ để thay thế")
            
    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất chuẩn hóa Header!")
