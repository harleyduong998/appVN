import re
import glob

# Pattern to find inner div of version dropdown
# We look for id="versionDropdown"... then immediately inside <div class="p-1">
# But regex across multiple lines is tricky. 
# We can find the specific string <div class="p-1"> but it might be used elsewhere?
# Only one <div class="p-1"> inside the dropdown structure.
# But let's be safer.
# Find the whole dropdown block start.

files = glob.glob('index*.html')

print(f"🔧 Đang thêm scroll cho dropdown list trong {len(files)} files...\n")

for filename in files:
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Strategy: Find <div id="versionDropdown"...>...<div class="p-1">
        # Replacement: <div class="p-1 max-h-80 overflow-y-auto">
        
        # Regex explanation:
        # (<div id="versionDropdown"[^>]*>         : Match outer div opening
        # \s*                                       : Whitespace/newlines
        # onclick="event.stopPropagation\(\)">      : specific attribute often there
        # \s*)                                      : Whitespace
        # <div class="p-1">                         : The target inner div
        
        pattern = r'(<div id="versionDropdown"[^>]*>\s*onclick="event\.stopPropagation\(\)">\s*)<div class="p-1">'
        
        # New class: max-h-80 (320px) overflow-y-auto
        replacement = r'\1<div class="p-1 max-h-80 overflow-y-auto">'
        
        if re.search(pattern, content):
            new_content = re.sub(pattern, replacement, content)
            
            # Check if change actually happened (maybe already applied?)
            if new_content != content:
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ {filename} - Đã thêm scroll")
            else:
                 # Check if already has scroll
                if 'max-h-80 overflow-y-auto' in content:
                    print(f"skipping {filename} - Đã có scroll")
                else:
                    print(f"⚠️ {filename} - Pattern match nhưng không thay đổi (Lạ?)")
        else:
            # Fallback pattern if onclick is different or order different
            # Tìm class="p-1" ngay sau id="versionDropdown" (ignoring middle content)
            # This is riskier if p-1 is used elsewhere.
            # But "versionDropdown" is unique.
            # Let's try searching simpler string logic if regex fails
            
            # Simple string replace if exact match found
            # Target:
            #                     onclick="event.stopPropagation()">
            #                     <div class="p-1">
            
            target_str = 'onclick="event.stopPropagation()">\n                    <div class="p-1">'
            replace_str = 'onclick="event.stopPropagation()">\n                    <div class="p-1 max-h-80 overflow-y-auto">'
            
            # Try flexible whitespace
            pattern2 = r'(onclick="event\.stopPropagation\(\)">\s*)<div class="p-1">'
            if re.search(pattern2, content):
                 new_content = re.sub(pattern2, r'\1<div class="p-1 max-h-80 overflow-y-auto">', content)
                 with open(filename, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                 print(f"✅ {filename} - Đã thêm scroll (Pattern 2)")
            else:
                 print(f"❌ {filename} - Không tìm thấy vị trí dropdown")

    except Exception as e:
        print(f"❌ {filename} - Lỗi: {str(e)}")

print("\n🎉 Hoàn tất!")
