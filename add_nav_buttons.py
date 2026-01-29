import re
import glob

# 1. Prepare File List
files = ['index.html']
for i in range(2, 15):
    files.append(f'index_v{i}.html')

print(f"🔧 Đang thêm nút điều hướng (Next/Back) cho {len(files)} files...\n")

# 2. Extract Template from index_v2.html (Cleanest source)
try:
    with open('index_v2.html', 'r', encoding='utf-8') as f:
        content_v2 = f.read()
    
    # Extract existing switcher block
    # Note: Regex needs to be robust for whitespace
    switcher_pattern = r'(<!-- Version Switcher -->\s*)([\s\S]*?)(\s*<!-- Right Side -->)'
    match = re.search(switcher_pattern, content_v2)
    
    if not match:
        raise Exception("Không tìm thấy block Version Switcher trong index_v2.html")
    
    raw_switcher = match.group(2)
    
    # Clean up: Remove active state (bg-slate-50 on link)
    # Pattern: class="... bg-slate-50"
    clean_switcher = re.sub(r' bg-slate-50"', '"', raw_switcher)
    
    # Enhance: Add h-9 to the button for alignment
    # Button class ends with cursor-pointer" usually
    if 'h-9' not in clean_switcher:
        clean_switcher = clean_switcher.replace('cursor-pointer"', 'cursor-pointer h-9"')
        
    print("✅ Đã chuẩn bị template")
    
except Exception as e:
    print(f"❌ Lỗi setup: {str(e)}")
    exit(1)

# 3. Process All Files
for i, filename in enumerate(files):
    try:
        # Calculate Prev/Next
        prev_idx = (i - 1) % len(files)
        next_idx = (i + 1) % len(files)
        
        prev_file = files[prev_idx]
        next_file = files[next_idx]
        
        # Prepare Active Switcher (Add highlight)
        current_switcher = clean_switcher
        escaped_filename = re.escape(filename)
        # Find link and add bg-slate-50
        # If filename is index.html, handled correctly by re.escape
        link_pattern = r'(<a href="' + escaped_filename + r'"[^>]*class="[^"]*)"'
        current_switcher = re.sub(link_pattern, r'\1 bg-slate-50"', current_switcher)
        
        # Construct New Block
        # Flex container with Prev - Switcher - Next
        
        new_block = f'''
            <!-- Version Switcher -->
            <div class="flex items-center gap-2">
                <!-- Prev Button -->
                <a href="{prev_file}"
                    class="flex items-center justify-center w-9 h-9 text-white/90 hover:text-white bg-white/10 rounded-lg border border-white/10 hover:bg-white/20 transition-all"
                    title="Phiên bản trước">
                    <i class="fa-solid fa-chevron-left text-xs"></i>
                </a>

{current_switcher}

                <!-- Next Button -->
                <a href="{next_file}"
                    class="flex items-center justify-center w-9 h-9 text-white/90 hover:text-white bg-white/10 rounded-lg border border-white/10 hover:bg-white/20 transition-all"
                    title="Phiên bản tiếp theo">
                    <i class="fa-solid fa-chevron-right text-xs"></i>
                </a>
            </div>
'''
        # Read Target File
        with open(filename, 'r', encoding='utf-8') as f:
            target_content = f.read()
            
        # Replace Block
        # We replace <!-- Version Switcher --> ... <!-- Right Side -->
        # We need to preserve the <!-- Right Side --> tag in the output (group 3)
        # But wait, new_block has <!-- Version Switcher --> at start.
        # My output logic:
        # re.sub(pattern, lambda m: new_block + m.group(3), ...)
        
        new_content = re.sub(switcher_pattern, lambda m: new_block + m.group(3), target_content)
        
        if new_content != target_content:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ {filename}: Prev={prev_file}, Next={next_file}")
        else:
            print(f"⚠️ {filename}: Không thay đổi (Pattern mismatch?)")

    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất thêm nút điều hướng!")
