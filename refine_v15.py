import re

def refine_v15():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Grid Container
    # Find the main grid container
    # Original: grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4
    # Target: grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-7 2xl:grid-cols-8 gap-x-8 gap-y-12 items-start justify-center
    
    grid_pattern = r'class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4"'
    new_grid_class = 'class="grid grid-cols-3 sm:grid-cols-4 md:grid-cols-5 lg:grid-cols-6 xl:grid-cols-7 2xl:grid-cols-8 gap-x-12 gap-y-12 justify-center"' 
    
    content = re.sub(grid_pattern, new_grid_class, content)

    # 2. Update Icon Container Size & Radius
    # Original: w-12 h-12 rounded-xl
    # Target: w-[68px] h-[68px] rounded-2xl shadow-sm (adding shadow back for icon depth, but keeping card flat)
    # Actually, let's keep it flat if user insisted, but MacOS usually has depth. Let's stick to size and radius first.
    # w-[68px] h-[68px] rounded-2xl
    
    icon_container_pattern = r'w-12 h-12 rounded-xl'
    new_icon_container_class = 'w-[68px] h-[68px] rounded-[22px] shadow-sm' # 22px is roughly correct for 68px squircle
    
    content = content.replace('w-12 h-12 rounded-xl', new_icon_container_class)

    # 3. Update Icon Font Size
    # The icon is inside the container. 
    # Pattern: <i class="fa... text-xl"></i>
    # Target: text-3xl
    content = content.replace('text-xl', 'text-3xl')
    
    # Wait, 'text-xl' might be used elsewhere (header, title?). 
    # Header: text-xl (App.vn), text-xl (Bell).
    # I should be specific.
    # The icons are inside the grid items.
    # Let's use regex to target icons inside the grid items specifically, or just replace 'text-xl' if it's safe.
    # In index_v15, the header uses 'text-xl' for logo and bell.
    # I don't want to change those.
    # The grid items have: <div ...><i class="... text-xl"></i></div>
    # I can target `text-xl` that is preceded by `fa-` or inside the specific div structure.
    # A safer way: replace `text-xl` only if it follows `fa-` and is part of the icon.
    # Most icons in the grid are `fa-solid ... text-xl` or `fa-regular ... text-xl`.
    # Let's replace `text-xl` with `text-3xl` ONLY inside the grid section.
    # The grid section starts after `<!-- Modules Grid ... -->`.
    
    parts = content.split('<!-- Modules Grid - COMPACT LAYOUT (5-6 cols) -->')
    if len(parts) > 1:
        header_part = parts[0]
        grid_part = parts[1]
        
        # Replace text-xl in grid_part
        grid_part = grid_part.replace('text-xl', 'text-3xl')
        
        # 4. Update Text Spacing
        # The text is in `<h3>`.
        # Class: font-semibold text-slate-800 text-sm text-center
        # I want to add `mt-2` or change `gap-2` in parent.
        # Parent is `flex flex-col ... gap-2`.
        # Let's change parent gap to `gap-3` or `gap-4`.
        grid_part = grid_part.replace('gap-2', 'gap-4')
        
        # Reasemble
        content = header_part + '<!-- Modules Grid - COMPACT LAYOUT (5-6 cols) -->' + grid_part
    
    # 5. Fix Title
    content = content.replace('<title>Dashboard V9 - Appvn</title>', '<title>Dashboard V15 - Appvn</title>')
    content = content.replace('V9', 'V15') # This might replace V9 in dropdown too, which is what we want for the *active* state text, but might break the link to actual V9 if not careful. 
    # The link to V9 is `href="index_v9.html" ... V9 ...`. 
    # If I replace 'V9', it becomes 'V15' in the link text too.
    # Let's leave V9 alone in the general replace and fix the active one manually or let it be.
    # I'll just fix the Title.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    refine_v15()
