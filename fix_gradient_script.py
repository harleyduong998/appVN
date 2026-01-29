import re

filename = 'index_v11.html'

# Script để apply gradient cho Lucide icons sau khi render
gradient_script = '''    <script>
        // Khởi tạo Lucide Icons
        lucide.createIcons();
        
        // Apply gradient cho icon stroke sau khi render
        setTimeout(() => {
            // Mapping class to gradient ID
            const gradientMap = {
                'icon-gradient-blue': 'gradient-blue',
                'icon-gradient-amber': 'gradient-amber',
                'icon-gradient-emerald': 'gradient-emerald',
                'icon-gradient-gray': 'gradient-gray',
                'icon-gradient-indigo': 'gradient-indigo',
                'icon-gradient-rose': 'gradient-rose',
                'icon-gradient-purple': 'gradient-purple',
                'icon-gradient-red': 'gradient-red',
                'icon-gradient-yellow': 'gradient-yellow',
                'icon-gradient-orange': 'gradient-orange',
                'icon-gradient-violet': 'gradient-violet',
                'icon-gradient-pink': 'gradient-pink',
                'icon-gradient-green': 'gradient-green',
                'icon-gradient-teal': 'gradient-teal',
                'icon-gradient-cyan': 'gradient-cyan',
                'icon-gradient-fuchsia': 'gradient-fuchsia',
                'icon-gradient-sky': 'gradient-sky',
                'icon-gradient-slate': 'gradient-slate'
            };
            
            // Tìm tất cả icon elements
            Object.keys(gradientMap).forEach(className => {
                const icons = document.querySelectorAll(`svg.${className}`);
                icons.forEach(icon => {
                    // Set stroke attribute trực tiếp vào SVG
                    icon.setAttribute('stroke', `url(#${gradientMap[className]})`);
                    icon.style.strokeWidth = '2.5';
                });
            });
        }, 100);
    </script>'''

print(f"🔧 Đang cập nhật script để apply gradient...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Tìm và thay thế script cũ
    old_script_pattern = r'<script>\s*// Khởi tạo Lucide Icons\s*lucide\.createIcons\(\);\s*</script>'
    
    if re.search(old_script_pattern, content):
        content = re.sub(old_script_pattern, gradient_script, content)
        print("✅ Đã thay thế script cũ bằng script mới")
    else:
        print("⚠️  Không tìm thấy script cũ, thêm script mới")
        content = content.replace('</body>', gradient_script + '\n</body>')
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ File {filename} đã được cập nhật!")
    print(f"✅ Script sẽ apply gradient cho SVG stroke sau khi Lucide render")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất! Gradient stroke giờ sẽ hoạt động!")
