import re

def refine_style_v15():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Reduce Gap
    # Current: gap-x-12 gap-y-12
    # Target: gap-x-8 gap-y-10 (Reduced but not cramped)
    content = content.replace('gap-x-12 gap-y-12', 'gap-x-8 gap-y-10')
    
    # 2. Add Gradient and Inner Shadow
    # Pattern: bg-[color]-[shade]
    # We need to find `bg-X-500` and replace with `bg-gradient-to-br from-X-400 to-X-600 shadow-inner`
    # However, some colors might be 600 or different shades.
    
    # Let's map specific colors found in the file:
    # blue-500, amber-500, emerald-500, gray-500, indigo-500, rose-500, purple-500, red-500, yellow-500, orange-500, violet-500, pink-500, green-600, yellow-600, blue-600, orange-600, teal-500, indigo-600, emerald-600, blue-600, purple-600, cyan-600, amber-600, rose-600, fuchsia-600, stone-600, slate-600, sky-600.
    
    # Regex to capture color and shade: bg-(\w+)-(\d+)
    # We only want to target the icon containers which have `w-[68px]`.
    
    # Strategy: Find the div with `w-[68px]` and replace its background class.
    
    def replacer(match):
        # match.group(0) is the entire div string if we capture it, but regex might be complex.
        # Simpler: regex for `bg-(\w+)-(\d+)` inside the specific container context? No, regex doesn't support "inside context" easily without variable length lookbehind.
        
        # Let's iterate over lines or chunks.
        # But `w-[68px]` and `bg-...` are on the same line in my previous script output?
        # Let's check the file content structure from previous view_file.
        # They are on the same line: <div class="w-[68px] ... bg-blue-500 ...">
        
        full_match = match.group(0)
        
        # Extract color and shade
        color_match = re.search(r'bg-(\w+)-(\d+)', full_match)
        if color_match:
            color = color_match.group(1)
            shade = int(color_match.group(2))
            
            # Construct gradient
            # logic: from-color-(shade-100) to-color-(shade+100)
            # if shade is 500 -> 400 to 600
            # if shade is 600 -> 500 to 700
            
            start_shade = max(50, shade - 100)
            end_shade = min(900, shade + 100)
            
            # Special cases for white/black? No, they are colors.
            
            gradient_class = f'bg-gradient-to-br from-{color}-{start_shade} to-{color}-{end_shade}'
            
            # Add subtle inner white ring/shadow for "depth"
            # ring-1 ring-white/20 ring-inset shadow-[inset_0_2px_4px_rgba(255,255,255,0.3)]
            style_class = f'{gradient_class} ring-1 ring-white/20 ring-inset shadow-[inset_0_4px_8px_rgba(255,255,255,0.25),0_4px_8px_rgba(0,0,0,0.1)]'
            
            # Replace the original bg class
            new_line = full_match.replace(f'bg-{color}-{shade}', style_class)
            
            # Remove border if present (e.g. border-blue-500) because gradient background makes border look weird usually, or we can keep it as subtle border.
            # User said "light internal shadow". 
            # I will remove `border` and `border-{color}-{shade}` to be cleaner with gradient.
            new_line = re.sub(r'border border-\w+-\d+', '', new_line)
            
            return new_line
        
        return full_match

    # Regex to find the container div
    # <div class="w-[68px] ...">
    # Note: refined_v15.py output might have extra spaces.
    pattern = re.compile(r'<div class="w-\[68px\].*?>')
    
    new_content = pattern.sub(replacer, content)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    refine_style_v15()
