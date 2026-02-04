"""
Convert all modules in index.html to v10 compact style
"""
import re

# Read current file
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Module configurations from v10
modules_config = [
    ('Sản phẩm', 'product.html', 'fa-box-open', 'amber-500', 'Sản phẩm'),
    ('Khách hàng', 'customer.html', 'fa-user-group', 'emerald-500', 'Khách hàng'),
    ('Kho hàng', 'warehouse.html', 'fa-warehouse', 'gray-500', 'Kho hàng'),
    ('Báo cáo', 'report.html', 'fa-chart-simple', 'indigo-500', 'Báo cáo'),
    ('CRM', 'crm.html', 'fa-chart-pie', 'rose-500', 'CRM'),
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
    ('Zalo', 'miniapp.html', 'zalo-icon', 'blue-600', 'Mini App'),
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

def create_v10_module(href, icon, color, title):
    """Create v10 style module HTML"""
    # Handle special Zalo icon
    if icon == 'zalo-icon':
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
                    <h3 class="font-bold text-slate-800 text-sm truncate group-hover:text-{color.replace('500', '700').replace('600', '700')} transition-colors">
                        {title}</h3>
                </div>
            </a>
'''

print("V10 module converter ready")
print(f"Will convert {len(modules_config)} modules")
print("\nSample output:")
print(create_v10_module('product.html', 'fa-box-open', 'amber-500', 'Sản phẩm'))
