import re

# Định nghĩa gradient cho từng màu
gradient_mapping = {
    'bg-blue-500': 'bg-gradient-to-br from-blue-500 to-blue-600',
    'bg-amber-500': 'bg-gradient-to-br from-amber-500 to-orange-500',
    'bg-emerald-500': 'bg-gradient-to-br from-emerald-500 to-teal-500',
    'bg-gray-500': 'bg-gradient-to-br from-gray-500 to-slate-600',
    'bg-indigo-500': 'bg-gradient-to-br from-indigo-500 to-purple-500',
    'bg-rose-500': 'bg-gradient-to-br from-rose-500 to-pink-500',
    'bg-purple-500': 'bg-gradient-to-br from-purple-500 to-fuchsia-500',
    'bg-red-500': 'bg-gradient-to-br from-red-500 to-rose-600',
    'bg-red-600': 'bg-gradient-to-br from-red-600 to-rose-700',
    'bg-yellow-500': 'bg-gradient-to-br from-yellow-500 to-amber-500',
    'bg-orange-500': 'bg-gradient-to-br from-orange-500 to-red-500',
    'bg-violet-500': 'bg-gradient-to-br from-violet-500 to-purple-600',
    'bg-pink-500': 'bg-gradient-to-br from-pink-500 to-rose-500',
    'bg-green-600': 'bg-gradient-to-br from-green-600 to-emerald-600',
    'bg-yellow-600': 'bg-gradient-to-br from-yellow-600 to-orange-500',
    'bg-blue-600': 'bg-gradient-to-br from-blue-600 to-indigo-600',
    'bg-orange-600': 'bg-gradient-to-br from-orange-600 to-red-600',
    'bg-teal-500': 'bg-gradient-to-br from-teal-500 to-cyan-600',
    'bg-indigo-600': 'bg-gradient-to-br from-indigo-600 to-purple-600',
    'bg-emerald-600': 'bg-gradient-to-br from-emerald-600 to-teal-600',
    'bg-cyan-600': 'bg-gradient-to-br from-cyan-600 to-blue-600',
    'bg-amber-600': 'bg-gradient-to-br from-amber-600 to-orange-600',
    'bg-rose-600': 'bg-gradient-to-br from-rose-600 to-pink-600',
    'bg-fuchsia-600': 'bg-gradient-to-br from-fuchsia-600 to-purple-600',
    'bg-gray-600': 'bg-gradient-to-br from-gray-600 to-slate-700',
    'bg-stone-600': 'bg-gradient-to-br from-stone-600 to-gray-700',
    'bg-slate-600': 'bg-gradient-to-br from-slate-600 to-gray-700',
    'bg-sky-600': 'bg-gradient-to-br from-sky-600 to-blue-600',
}

filename = 'index_v11.html'

print(f"🎨 Đang thêm gradient cho icon boxes...\n")

try:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    gradient_count = 0
    
    # Thay thế các bg-color trong group-hover
    for solid_color, gradient_color in gradient_mapping.items():
        # Pattern: group-hover:bg-xxx-500 hoặc bg-xxx-500 trong icon box
        pattern = f'group-hover:{solid_color}'
        if pattern in content:
            content = content.replace(pattern, f'group-hover:{gradient_color}')
            gradient_count += content.count(f'group-hover:{gradient_color}')
            print(f"  ✓ {solid_color} → gradient")
    
    # Ghi lại file
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"\n✅ Đã thêm gradient cho icon boxes")
    print(f"✅ File {filename} đã được cập nhật!")
    
except FileNotFoundError:
    print(f"❌ {filename} - File không tồn tại")
except Exception as e:
    print(f"❌ Lỗi: {str(e)}")

print("\n🎉 Hoàn tất thêm gradient!")
