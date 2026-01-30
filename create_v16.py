import re

def create_v16():
    # Read v15
    with open('index_v15.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Title
    content = content.replace('Dashboard V15 - Appvn', 'Dashboard V16 - Appvn')
    
    # 2. Update Version Switcher - Add V16
    # Find V15 entry and append V16
    v15_pattern = r'(href="index_v15.html".*?</a>)'
    
    v16_entry = """
                        <a href="index_v16.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded-lg bg-white border border-slate-200 text-blue-600 flex items-center justify-center font-bold text-xs shadow-sm">
                                V16</div>
                            <div class="text-sm font-medium text-slate-700">V15 Layout + V10 Icon</div>
                        </a>"""
    
    # Remove bg-slate-50 from V15 link first (make it inactive)
    content = content.replace('bg-slate-50">', '">') 
    # Wait, the v16_entry has bg-slate-50. 
    # The replacement above might effect lines I don't want.
    # V15 line: ... transition-colors bg-slate-50">
    # Let's be specific.
    content = content.replace('transition-colors bg-slate-50">', 'transition-colors">')
    
    # Now append V16
    content = re.sub(v15_pattern, r'\1' + v16_entry, content, flags=re.DOTALL)
    
    # Update active link logic just in case
    # content = content.replace('href="index_v16.html"', 'href="index_v16.html" class="... bg-slate-50"') 
    # The inserted block already has it.
    
    # Update Prev/Next
    content = content.replace('href="index_v14.html"', 'href="index_v15.html"')
    # Next is index.html, keep it circular or empty? Let's keep index.html for now.

    # 3. Replace Icon Styles
    # Struct in v15: 
    # <div class="w-[68px] h-[68px] rounded-2xl shadow-sm bg-gradient-to-br from-COLOR-400 to-COLOR-600 ring-1 ring-white/20 ring-inset shadow-[inset...] ... text-white ...">
    #   <i class="... text-3xl"></i>
    # </div>
    
    # Target in v16 (based on v10):
    # <div class="w-[68px] h-[68px] rounded-2xl bg-white border border-slate-100 shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)] flex items-center justify-center text-COLOR-500 flex-shrink-0 z-10 group-hover:bg-COLOR-500 group-hover:text-white transition-colors duration-300">
    #   <i class="... text-3xl"></i>
    # </div>
    
    # We need to extract the color from `from-COLOR-400`.
    
    def icon_replacer(match):
        full_div = match.group(0)
        
        # Extract color
        color_match = re.search(r'from-(\w+)-400', full_div)
        color = 'blue' # default
        if color_match:
            color = color_match.group(1)
        
        # If color is 'gray', v10 used 'gray'. 
        # If color is 'slate', v10 used 'slate'.
        # We use the extracted color.
        
        # Build new class string
        # Keep size: w-[68px] h-[68px] (from v15 layout)
        # Keep radius: rounded-2xl (from v15)
        
        new_classes = [
            f"w-[68px] h-[68px]",
            "rounded-2xl",
            "bg-white",
            "border border-slate-100",
            "shadow-[0_8px_20px_-4px_rgba(0,0,0,0.15)]",
            "flex items-center justify-center",
            f"text-{color}-500",
            "flex-shrink-0 z-10",
            f"group-hover:bg-{color}-500",
            "group-hover:text-white",
            "transition-colors duration-300"
        ]
        
        # Reconstruct div
        # The content inside <div>...</div> is the icon <i>. 
        # Regex captured the opening tag `div class="..."`.
        
        return f'<div class="{" ".join(new_classes)}">'

    # Regex to find the div. 
    # It has `w-[68px]` and `bg-gradient-to-br`.
    pattern = re.compile(r'<div class="w-\[68px\].*?bg-gradient-to-br.*?>')
    
    content = pattern.sub(icon_replacer, content)
    
    # Also need to ensure the icon inside loses `text-white` if it had it explicitly?
    # In v15, the parent had `text-white`. The icon `<i>` usually inherits or has specific class?
    # In v15, `text-white` was on the parent div. The <i> usually has `text-3xl`.
    # In v10, the icon `<i>` has `text-2xl`. In v15 `text-3xl`.
    # Parent div in v15 has `text-white`.
    # My new class string has `text-{color}-500`. 
    # The icon `<i>` inside shouldn't have `text-white` class on itself.
    # In v15 code: <i class="fa-solid ... text-3xl"></i>. No text-color on <i>.
    # So inheriting from parent `text-{color}-500` should work.
    
    # Write v16
    with open('index_v16.html', 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    create_v16()
