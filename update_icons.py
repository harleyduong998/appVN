import re

# Đọc file HTML
with open('index_v9.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Định nghĩa các màu cho từng module
color_map = {
    'fa-cart-shopping': 'blue-500',
    'fa-box-open': 'amber-500',
    'fa-user-group': 'emerald-500',
    'fa-warehouse': 'gray-500',
    'fa-chart-simple': 'indigo-500',
    'fa-chart-pie': 'rose-500',
    'fa-robot': 'purple-500',
    'fa-tags': 'red-500',
    'fa-bolt': 'red-600',
    'fa-crown': 'yellow-500',
    'fa-layer-group': 'orange-500',
    'fa-chart-area': 'violet-500',
    'fa-comments': 'pink-500',
    'fa-headset': 'green-600',
    'fa-comment-dots': 'yellow-600',
    'fa-calendar-check': 'blue-600',
    'fa-calendar-days': 'orange-600',
    'fa-shield-halved': 'teal-500',
    'fa-file-invoice': 'blue-500',
    'fa-file-invoice-dollar': 'indigo-600',
    'fa-credit-card': 'emerald-600',
    'fa-money-check-dollar': 'emerald-600',
    'fa-globe': 'purple-600',
    'fa-handshake': 'cyan-600',
    'fa-plug': 'cyan-600',
    'fa-truck': 'amber-600',
    'fa-palette': 'rose-600',
    'fa-envelope-open-text': 'fuchsia-600',
    'fa-print': 'gray-600',
    'fa-hard-drive': 'stone-600',
    'fa-gear': 'slate-600',
    'fa-building': 'sky-600',
    'fa-laptop-code': 'indigo-600',
    'fa-table': 'slate-600',
}

# Pattern để tìm các icon box div
pattern = r'<div\s+class="w-14 h-14 rounded-2xl bg-white border border-slate-100 shadow-\[0_8px_20px_-4px_rgba\(0,0,0,0\.15\)\] flex items-center justify-center text-(\w+-\d+) flex-shrink-0 z-10 mr-5 group-hover:bg-\1 group-hover:text-white transition-colors duration-300">'

# Thay thế pattern
def replace_icon_box(match):
    color = match.group(1)
    # Đảo ngược: nền màu, icon trắng, hover chỉ scale
    return f'<div class="w-14 h-14 rounded-2xl bg-{color} border border-{color} shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)] flex items-center justify-center text-white flex-shrink-0 z-10 mr-5 group-hover:scale-110 transition-transform duration-300">'

content = re.sub(pattern, replace_icon_box, content)

# Xử lý trường hợp đặc biệt cho Zalo (có img thay vì icon)
# Tìm và thay thế cho Mini App và Zalo OA
zalo_pattern = r'<div\s+class="w-14 h-14 rounded-2xl bg-white border border-slate-100 shadow-\[0_8px_20px_-4px_rgba\(0,0,0,0\.15\)\] flex items-center justify-center text-blue-600 flex-shrink-0 z-10 mr-5 group-hover:bg-blue-600 group-hover:text-white transition-colors duration-300">\s+<img'

zalo_replacement = '<div class="w-14 h-14 rounded-2xl bg-blue-600 border border-blue-600 shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)] flex items-center justify-center text-white flex-shrink-0 z-10 mr-5 group-hover:scale-110 transition-transform duration-300">\n                    <img'

content = re.sub(zalo_pattern, zalo_replacement, content)

# Ghi lại file
with open('index_v9.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Đã cập nhật thành công tất cả icon boxes!")
print("- Icon trắng trên nền màu")
print("- Hover chỉ scale lên (không đổi màu)")
