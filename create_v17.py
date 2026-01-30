import re

def create_v17():
    # Read v16
    with open('index_v16.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title
    content = content.replace('Dashboard V16 - Appvn', 'Dashboard V17 - Appvn')
    
    # 2. Update Version Switcher - Add V17
    v16_pattern = r'(href="index_v16.html".*?</a>)'
    
    v17_entry = """
                        <a href="index_v17.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded-lg bg-white border border-slate-200 flex items-center justify-center font-bold text-xs shadow-sm">
                                <span class="bg-gradient-to-br from-blue-600 to-blue-400 bg-clip-text text-transparent">V17</span>
                            </div>
                            <div class="text-sm font-medium text-slate-700">V16 Layout + V8 Icon</div>
                        </a>"""
    
    # Inactive V16
    content = content.replace('transition-colors bg-slate-50">', 'transition-colors">')
    
    # Append V17
    content = re.sub(v16_pattern, r'\1' + v17_entry, content, flags=re.DOTALL)
    
    # Update Prev/Next
    content = content.replace('href="index_v15.html"', 'href="index_v16.html"')

    # 3. Apply V8 Icon Style
    # V16 structure:
    # <div class="w-[68px] h-[68px] rounded-2xl bg-white border border-slate-100 shadow-[...] flex items-center justify-center text-COLOR-500 flex-shrink-0 z-10 group-hover:bg-COLOR-500 group-hover:text-white transition-colors duration-300">
    #   <i class="fa-solid fa-ICON text-3xl"></i>
    # </div>
    
    # V8 style target:
    # - Container: Keep V16 container (White box) but REMOVE hover fill effect?
    #   User said "giống html 16 nhưng sử dụng icon của html 8". 
    #   V8 icon style is gradient text. 
    #   If we keep hover fill (solid bg), the gradient text inside becomes white.
    #   V16 behavior: hover -> bg becomes solid color, text becomes white.
    #   If V17 uses V8 style (gradient text), on hover:
    #   Option A: Keep hover fill. Icon turns white. (Good contrast).
    #   Option B: No hover fill. Icon stays gradient or lifts?
    #   V8 has simple lift, no bg color change on hover.
    #   Let's stick to V16 layout + V8 *Icon Style*. 
    #   Usually "use icon of V8" means the look of the icon itself.
    #   I will Apply Gradient Text to the icon.
    #   AND I will REMOVE the hover-fill-background effect to match V8's cleaner look (where only icon is colored).
    #   So: White Box, Gradient Icon. Hover: Lift only (no bg change).
    
    # Regex to transform the container and icon.
    
    def icon_processor(match):
        full_div = match.group(0) # The container div
        
        # Extract color
        # text-COLOR-500
        color_match = re.search(r'text-(\w+)-500', full_div)
        color = 'blue'
        if color_match:
            color = color_match.group(1)
            
        # New Container Clean classes (No group-hover bg change)
        # Keep size, shape, shadow.
        container_classes = [
            f"w-[68px] h-[68px]",
            "rounded-2xl",
            "bg-white",
            "border border-slate-100", # maybe lighter border?
            "shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)]",
            "flex items-center justify-center",
            "flex-shrink-0 z-10",
            "transition-all duration-300",
            # "group-hover:scale-105" # maybe scale icon?
        ]
        
        # New Icon classes
        # Gradient text, enlarged.
        # text-4xl (increased from 3xl)
        icon_classes = [
            f"bg-gradient-to-br from-{color}-600 to-{color}-400",
            "bg-clip-text",
            "text-transparent",
            "text-4xl", # Increased size
            # "drop-shadow-sm" # Maybe add subtle drop shadow to icon itself? V8 didn't have it but it looks nice. Let's stick to V8 (clean).
        ]
        
        # Return new start tag for div. 
        # But wait, I need to modify the <i> inside too. 
        # My regex in create_v16 only targeted the opening div tag.
        # Here I need to target the whole block or just start tag and assume I script the inner part?
        # In v16, the inner <i> had `text-3xl`.
        
        return f'<div class="{" ".join(container_classes)}">'
        
    # We need to replace the DIV opening tag.
    pattern_div = re.compile(r'<div class="w-\[68px\].*?text-\w+-500.*?>')
    content = pattern_div.sub(icon_processor, content)
    
    # Now replace the <i> tag style.
    # Current i: <i class="fa-solid fa-xyz text-3xl"></i>
    # We want to add the gradient classes to <i>.
    # BUT the color is dynamic.
    # The container no longer has `text-COLOR-500`. So <i> won't inherit.
    # So we must apply classes to <i> based on the context... which is hard if we do it separately.
    
    # Better strategy: Parse the whole block (A tag to /A tag) and rewrite.
    
    # Find all module links.
    link_pattern = re.compile(r'<a href="modules/([^"]+)".*?</a>', re.DOTALL)
    
    def link_replacer(match):
        full_link = match.group(0)
        module_name = match.group(1)
        
        # Extract existing color from the old div class text-COLOR-500
        color_match = re.search(r'text-(\w+)-500', full_link)
        color = 'blue'
        if color_match:
            color = color_match.group(1)
            
        # Extract Icon Class
        icon_match = re.search(r'<i class="([^"]+)"', full_link)
        icon_class = "fa-solid fa-cube"
        if icon_match:
            # Remove text-3xl and other sizing
            raw_icon = icon_match.group(1)
            icon_parts = [p for p in raw_icon.split() if not p.startswith('text-')]
            icon_class = " ".join(icon_parts)
            
        # Rebuild the Link Block
        # Layout: V16 (Launchpad)
        # Icon Style: V8 (Gradient Text)
        
        # Container
        div_html = f'''<div class="w-[68px] h-[68px] rounded-2xl bg-white border border-slate-100 shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)] flex items-center justify-center flex-shrink-0 z-10 transition-all duration-300 group-hover:shadow-[0_12px_24px_-4px_rgba(0,0,0,0.2)]">
                    <i class="{icon_class} text-4xl bg-gradient-to-br from-{color}-600 to-{color}-400 bg-clip-text text-transparent transform group-hover:scale-110 transition-transform duration-300"></i>
                </div>'''
                
        # Link content (copy text part logic from V16 or just rebuild)
        # We can capture the text.
        text_match = re.search(r'<h3 class=".*?">\s*(.*?)\s*</h3>', full_link, re.DOTALL)
        text = "Module"
        if text_match:
            text = text_match.group(1)
            
        new_link = f'''<a href="modules/{module_name}" class="flex flex-col items-center justify-center gap-4 transition-transform duration-300 hover:-translate-y-2 group">
                {div_html}
                <div class="min-w-0">
                    <h3 class="font-semibold text-slate-800 text-sm text-center">
                        {text}</h3>
                </div>
            </a>'''
            
        return new_link

    content = link_pattern.sub(link_replacer, content)

    with open('index_v17.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    create_v17()
