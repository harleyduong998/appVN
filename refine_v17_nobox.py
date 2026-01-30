import re

def refine_v17_nobox():
    file_path = 'index_v17.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Strategy:
    # 1. Regex find the wrapper div (identified by the long class string or parts of it).
    # 2. Capture the inner content (the <i> tag).
    # 3. Replace the wrapper with the inner content, modified (text-4xl -> text-6xl).
    # 4. Handle Zalo/MiniApp special cases (replace <i> with <img>).

    # The wrapper class starts with w-[68px]
    # <div class="w-[68px] h-[68px] ... shadow-[...] ...">
    #    <i class="..."></i>
    # </div>
    
    # We want to replace this whole block with just the modifications.
    
    # Problem: Regex matching matching nested divs is hard, but here the wrapper is inside an <a> tag and contains an <i>.
    # It doesn't contain other divs.
    
    pattern_wrapper = re.compile(r'<div class="w-\[68px\].*?>(.*?)</div>', re.DOTALL)
    
    def wrapper_replacer(match):
        inner_content = match.group(1).strip()
        
        # Check if this is the Zalo or MiniApp block (which currently has fa-cube from previous step)
        # We can't check href easily here, but we can check if we want to replace based on context?
        # Actually, let's just do the resizing first, then fix Zalo/MiniApp by href search.
        
        # Resize: text-4xl -> text-6xl
        # text-6xl is 60px line height, font size 3.75rem (60px). Close to 68px.
        # Also remove `bg-white` `border` etc from inner if any (none expected).
        # Need to ensure the lift/scale effects are on the icon now?
        # The wrapper had `group-hover:shadow...`. The icon inside had `group-hover:scale-110`.
        # The parent <a> tag has `hover:-translate-y-2`.
        # So removing wrapper is fine.
        
        new_content = inner_content.replace('text-4xl', 'text-6xl drop-shadow-md') # Add drop shadow for better visibility? V8 had none, but V16 had shadow on box.
                                                                                # User said "V8 styling". V8 icon had bg-clip-text.
                                                                                # Let's keep it simple: text-6xl.
        
        return new_content

    content = pattern_wrapper.sub(wrapper_replacer, content)

    # Now Fix Zalo / Mini App
    # They currently have <i class="... fa-cube ... text-6xl ..."></i> due to the above replacement.
    # We need to find the A tag for miniapp and zalo-oa and replace the <i> with <img>.
    
    zalo_img = '<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Icon_of_Zalo.svg" alt="Zalo" class="w-[60px] h-[60px] object-contain group-hover:scale-110 transition-transform duration-300 drop-shadow-md">'
    
    # Mini App
    # Search for href="modules/miniapp.html" ... then find the <i> inside the A tag.
    pattern_miniapp = re.compile(r'(<a href="modules/miniapp.html"[^>]*>)\s*<i[^>]*></i>', re.DOTALL)
    content = pattern_miniapp.sub(r'\1' + zalo_img, content)

    # Zalo OA
    pattern_zalo = re.compile(r'(<a href="modules/zalo-oa.html"[^>]*>)\s*<i[^>]*></i>', re.DOTALL)
    content = pattern_zalo.sub(r'\1' + zalo_img, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    refine_v17_nobox()
