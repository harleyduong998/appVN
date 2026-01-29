import re

filename = 'index_v11.html'

# SVG Gradient Definitions
svg_gradients = '''    <!-- SVG Gradient Definitions -->
    <svg width="0" height="0" style="position: absolute;">
        <defs>
            <linearGradient id="gradient-blue" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#3b82f6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#6366f1;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-amber" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#f59e0b;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f97316;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-emerald" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#10b981;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#14b8a6;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-gray" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#6b7280;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#475569;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-indigo" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#6366f1;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#a855f7;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-rose" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#f43f5e;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ec4899;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-purple" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#a855f7;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#d946ef;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-red" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#ef4444;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f43f5e;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-yellow" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#eab308;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f59e0b;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-orange" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#f97316;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#ef4444;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-violet" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#8b5cf6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#a855f7;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-pink" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#ec4899;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#f43f5e;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-green" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#16a34a;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#10b981;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-teal" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#14b8a6;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#06b6d4;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-cyan" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#06b6d4;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-fuchsia" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#d946ef;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#a855f7;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-sky" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#0ea5e9;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#3b82f6;stop-opacity:1" />
            </linearGradient>
            <linearGradient id="gradient-slate" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#475569;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#64748b;stop-opacity:1" />
            </linearGradient>
        </defs>
    </svg>

'''

# Color to gradient class mapping
color_to_gradient = {
    'text-blue-500': 'icon-gradient-blue',
    'text-amber-500': 'icon-gradient-amber',
    'text-emerald-500': 'icon-gradient-emerald',
    'text-gray-500': 'icon-gradient-gray',
    'text-indigo-500': 'icon-gradient-indigo',
    'text-rose-500': 'icon-gradient-rose',
    'text-purple-500': 'icon-gradient-purple',
    'text-red-500': 'icon-gradient-red',
    'text-red-600': 'icon-gradient-red',
    'text-yellow-500': 'icon-gradient-yellow',
    'text-yellow-600': 'icon-gradient-yellow',
    'text-orange-500': 'icon-gradient-orange',
    'text-orange-600': 'icon-gradient-orange',
    'text-violet-500': 'icon-gradient-violet',
    'text-pink-500': 'icon-gradient-pink',
    'text-green-600': 'icon-gradient-green',
    'text-blue-600': 'icon-gradient-blue',
    'text-teal-500': 'icon-gradient-teal',
    'text-teal-600': 'icon-gradient-teal',
    'text-indigo-600': 'icon-gradient-indigo',
    'text-emerald-600': 'icon-gradient-emerald',
    'text-cyan-600': 'icon-gradient-cyan',
    'text-amber-600': 'icon-gradient-amber',
    'text-rose-600': 'icon-gradient-rose',
    'text-fuchsia-600': 'icon-gradient-fuchsia',
    'text-gray-600': 'icon-gradient-gray',
    'text-stone-600': 'icon-gradient-slate',
    'text-slate-600': 'icon-gradient-slate',
    'text-sky-600': 'icon-gradient-sky',
}

print(f"🎨 Đang thêm SVG gradients và gradient classes...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Thêm SVG gradients sau <body>
    content = content.replace('<body class="min-h-screen', svg_gradients + '<body class="min-h-screen')
    print("✅ Đã thêm SVG gradient definitions")
    
    # 2. Thêm gradient class cho các icon
    icon_count = 0
    for text_color, gradient_class in color_to_gradient.items():
        # Pattern: <i data-lucide="xxx" class="text-xxx"></i>
        pattern = f'<i data-lucide="([^"]+)" class="{text_color}"></i>'
        replacement = f'<i data-lucide="\\1" class="{gradient_class}"></i>'
        
        new_content, count = re.subn(pattern, replacement, content)
        if count > 0:
            content = new_content
            icon_count += count
            print(f"  ✓ {text_color} → {gradient_class} ({count}x)")
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Đã thêm gradient class cho {icon_count} icon")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất thêm gradient cho icon stroke!")
