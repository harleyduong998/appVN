"""
Complete conversion script for all modules to v10 style
"""
import re

# Read the file
with open('index_v10_full.html', 'r', encoding='utf-8') as f:
    content = f.read()

# All modules with their v10 configurations
# Format: (search_text, href, icon, color, title)
modules = [
    # Already converted: Sales (1), Product (2), Customer (3), Warehouse (4), Report (5), CRM (6)
    
    # Need to convert:
    ('Automation', 'automation.html', 'fa-robot', 'purple-500', 'Automation'),
    ('Ưu đãi', 'promotions.html', 'fa-tags', 'red-500', 'Ưu đãi'),
    ('Flash Sale', 'flashsale.html', 'fa-bolt', 'red-600', 'Flash Sale'),
    ('Loyalty', 'loyalty.html', 'fa-crown', 'yellow-500', 'Loyalty'),
    ('Combo', 'combo.html', 'fa-layer-group', 'orange-500', 'Combo'),
    ('RFM', 'rfm.html', 'fa-chart-area', 'violet-500', 'RFM'),
    ('WorkChat', 'workchat.html', 'fa-comments', 'pink-500', 'WorkChatV2'),
    ('Tổng đài', 'callcenter.html', 'fa-headset', 'green-600', 'Tổng đài'),
    ('Feedback', 'feedback.html', 'fa-comment-dots', 'yellow-600', 'Feedback'),
    ('Booking', 'booking.html', 'fa-calendar-check', 'blue-600', 'Booking'),
    ('Sự kiện', 'events.html', 'fa-calendar-days', 'orange-600', 'Sự kiện'),
    ('Bảo hành', 'warranty.html', 'fa-shield-halved', 'teal-500', 'Bảo hành'),
    ('Hóa đơn điện tử', 'einvoice.html', 'fa-file-invoice', 'blue-500', 'Hóa đơn'),
    ('Công nợ', 'debt.html', 'fa-file-invoice-dollar', 'indigo-600', 'Công nợ'),
    ('Thanh toán', 'payment.html', 'fa-credit-card', 'emerald-600', 'Thanh toán'),
    ('Thẻ trả trước', 'prepaid.html', 'fa-money-check-dollar', 'emerald-600', 'Thẻ trả trước'),
    ('Zalo', 'miniapp.html', 'ZALO_ICON', 'blue-600', 'Mini App'),
    ('Webview', 'webview.html', 'fa-globe', 'purple-600', 'Webview'),
    ('Cộng tác viên', 'collaborator.html', 'fa-handshake', 'cyan-600', 'Cộng tác viên'),
    ('Tích hợp', 'integration.html', 'fa-plug', 'cyan-600', 'Tích hợp'),
    ('Vận chuyển', 'shipping.html', 'fa-truck', 'amber-600', 'Vận chuyển'),
    ('Thiết kế ảnh', 'imagedesign.html', 'fa-palette', 'rose-600', 'Thiết kế ảnh'),
    ('Email', 'emaildesign.html', 'fa-envelope-open-text', 'fuchsia-600', 'Thiết kế Email'),
    ('Mẫu in', 'templates.html', 'fa-print', 'gray-600', 'Mẫu in'),
    ('Lưu trữ', 'storage.html', 'fa-hard-drive', 'stone-600', 'Lưu trữ'),
    ('Cài đặt', 'settings.html', 'fa-gear', 'slate-600', 'Cài đặt'),
    ('Bất động sản', 'realestate.html', 'fa-building', 'sky-600', 'Bất động sản'),
]

def create_v10_card(href, icon, color, title):
    """Generate v10 style card HTML"""
    # Determine hover color
    if '-500' in color:
        hover_color = color.replace('-500', '-700')
    elif '-600' in color:
        hover_color = color.replace('-600', '-700')
    else:
        hover_color = color
    
    # Handle Zalo special icon
    if icon == 'ZALO_ICON':
        icon_html = '<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Icon_of_Zalo.svg" alt="Zalo" class="w-6 h-6">'
    else:
        icon_html = f'<i class="fa-solid {icon} text-2xl"></i>'
    
    return f'''            <!-- {title} -->
            <a href="modules/{href}"
                class="bg-white rounded-xl p-4 shadow-sm border border-slate-200/30 card-hover group flex items-center justify-start gap-3 h-[85px] hover:border-{color} relative overflow-hidden transition-all">
                <div
                    class="w-14 h-14 rounded-2xl bg-white border border-slate-100 shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)] flex items-center justify-center text-{color} flex-shrink-0 z-10 group-hover:bg-{color} group-hover:text-white transition-colors duration-300">
                    {icon_html}
                </div>
                <div class="flex-1 min-w-0">
                    <h3 class="font-bold text-slate-800 text-sm truncate group-hover:text-{hover_color} transition-colors">
                        {title}</h3>
                </div>
            </a>'''

# Find and replace each module
# We'll use a simple pattern to find old-style modules and replace them
# Pattern: Find modules with "rounded-2xl p-6" (old style) and replace with v10 style

# Let's do a more targeted approach - find modules by their href
for search_name, href, icon, color, title in modules:
    # Find the module block
    # Pattern: <a href="modules/{href}" ... </a>
    pattern = rf'(<a href="modules/{re.escape(href)}"[^>]*>)(.*?)(</a>)'
    
    def replace_module(match):
        # Check if it's already v10 style (has h-[85px])
        if 'h-[85px]' in match.group(0):
            return match.group(0)  # Already converted
        
        # Replace with v10 style
        return create_v10_card(href, icon, color, title)
    
    content = re.sub(pattern, replace_module, content, flags=re.DOTALL)

# Write the updated content
with open('index_v10_full.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Conversion complete!")
print(f"Converted {len(modules)} modules to v10 style")
print("File saved as: index_v10_full.html")
