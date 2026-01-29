import re

# Mapping Font Awesome icons sang Lucide Icons
icon_mapping = {
    'fa-cart-shopping': 'shopping-cart',
    'fa-box-open': 'package-open',
    'fa-user-group': 'users',
    'fa-warehouse': 'warehouse',
    'fa-chart-simple': 'bar-chart-3',
    'fa-chart-pie': 'pie-chart',
    'fa-robot': 'bot',
    'fa-tags': 'tags',
    'fa-bolt': 'zap',
    'fa-crown': 'crown',
    'fa-layer-group': 'layers',
    'fa-chart-area': 'area-chart',
    'fa-comments': 'messages-square',
    'fa-headset': 'headphones',
    'fa-comment-dots': 'message-circle',
    'fa-calendar-check': 'calendar-check',
    'fa-calendar-days': 'calendar-days',
    'fa-shield-halved': 'shield',
    'fa-file-invoice': 'file-text',
    'fa-file-invoice-dollar': 'receipt',
    'fa-credit-card': 'credit-card',
    'fa-money-check-dollar': 'banknote',
    'fa-globe': 'globe',
    'fa-handshake': 'handshake',
    'fa-plug': 'plug',
    'fa-truck': 'truck',
    'fa-palette': 'palette',
    'fa-envelope-open-text': 'mail-open',
    'fa-print': 'printer',
    'fa-hard-drive': 'hard-drive',
    'fa-gear': 'settings',
    'fa-building': 'building',
    'fa-laptop-code': 'code',
    'fa-table': 'table',
    'fa-bell': 'bell',
}

filename = 'index_v11.html'

print(f"🔧 Đang chuyển đổi sang Lucide Icons...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Thay thế Font Awesome CDN bằng Lucide CDN
    content = content.replace(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">',
        '<script src="https://unpkg.com/lucide@latest"></script>'
    )
    
    # 2. Thay thế các icon
    icon_count = 0
    for fa_icon, lucide_icon in icon_mapping.items():
        # Pattern: <i class="fa-regular fa-xxx text-xxx"></i>
        pattern = f'<i class="fa-regular {fa_icon} (text-[^"]+)"></i>'
        replacement = f'<i data-lucide="{lucide_icon}" class="\\1"></i>'
        
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            icon_count += count
            print(f"  ✓ {fa_icon} → {lucide_icon} ({count}x)")
    
    # 3. Xử lý Zalo icon (img tag) - giữ nguyên
    print(f"  ℹ Zalo icon (img tag) - giữ nguyên")
    
    # 4. Thêm script khởi tạo Lucide ở cuối body
    content = content.replace(
        '</body>',
        '''    <script>
        // Khởi tạo Lucide Icons
        lucide.createIcons();
    </script>
</body>'''
    )
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Đã chuyển đổi {icon_count} icon sang Lucide")
    print(f"✅ Đã thêm Lucide CDN và script khởi tạo")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất chuyển đổi sang Lucide Icons!")
