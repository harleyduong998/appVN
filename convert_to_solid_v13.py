import re

filename = 'index_v13.html'

print(f"🔧 Đang chuyển đổi icon sang dạng solid (filled)...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Đoạn script mới: chỉ khởi tạo Lucide với fill="currentColor"
    # và stroke-width có thể điều chỉnh (vd: 1.5)
    new_script = '''    <script>
        // Khởi tạo Lucide Icons với dạng solid (filled)
        lucide.createIcons({
            attrs: {
                fill: "currentColor",
                "stroke-width": "1.5"
            }
        });
    </script>'''
    
    # 2. Tìm và thay thế đoạn script cũ (bao gồm cả phần fix gradient thừa)
    # Pattern tìm từ <script> đến </body> (hoặc hết script cũ)
    # Script cũ bắt đầu bằng <script> và chứa lucide.createIcons(); và setTimeout...
    
    # Sử dụng regex để match toàn bộ khối script cũ
    pattern = r'<script>\s*// Khởi tạo Lucide Icons\s*lucide\.createIcons\(\);\s*// Apply gradient.*?</script>'
    
    if re.search(pattern, content, re.DOTALL):
        content = re.sub(pattern, new_script, content, flags=re.DOTALL)
        print("✅ Đã cập nhật script Lucide (Solid Style)")
    else:
        # Fallback nếu pattern không match (do edit tay hoặc thay đổi trước đó)
        # Thử tìm script đơn giản hơn
        print("⚠️ Pattern script cũ không khớp chính xác, thử tìm và replace rộng hơn...")
        start_marker = '// Khởi tạo Lucide Icons'
        end_marker = '</script>'
        start_idx = content.find(start_marker)
        
        if start_idx != -1:
            script_start = content.rfind('<script', 0, start_idx)
            script_end = content.find(end_marker, start_idx) + len(end_marker)
            
            content = content[:script_start] + new_script + content[script_end:]
            print("✅ Đã cập nhật script (fallback method)")
        else:
            print("❌ Không tìm thấy script cũ!")

    # 3. Cập nhật CSS để bỏ stroke-width: 2.0 (vì đã set trong JS)
    # Hoặc để CSS override? JS attrs thường có độ ưu tiên thấp hơn CSS !important nhưng cao hơn style tag?
    # Không, attributes <svg stroke-width="1.5"> có độ ưu tiên thấp hơn CSS selector [data-lucide] { stroke-width: 2.0 }
    # Nên cần xoá hoặc update CSS.
    
    content = content.replace('stroke-width: 2.0;', '/* stroke-width: 2.0; handled by JS */')
    print("✅ Đã disable CSS stroke-width cũ")
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ File {filename} đã được cập nhật sang style Solid!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")
