
import os

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: index.html not found.")
        return

    # We want to replace the Logo div block.
    # Structure:
    # <div class="flex items-center gap-3">
    #     <div ...> <img src="logo.png" ...> </div>
    #     <span ...>App.vn</span>
    # </div>
    
    # Let's find this block.
    # Start: <div class="flex items-center gap-3">
    # End: </div> after the span.
    
    start_marker = '<div class="flex items-center gap-3">'
    start_idx = content.find(start_marker)
    
    if start_idx == -1:
        print("Error: Logo container start not found.")
        return
        
    # We want to find the end of this div.
    # It contains a nested div (icon) and a span.
    # So we need to skip one </div> (for the icon) and find the next </div>.
    
    # Or we can just look for the span text and find the closing tag after it.
    span_marker = '<span class="text-xl font-bold tracking-tight">App.vn</span>'
    span_idx = content.find(span_marker, start_idx)
    
    if span_idx == -1:
        print("Error: Logo text span not found.")
        return
        
    end_idx = content.find('</div>', span_idx) + 6
    
    # New content: Just the image, clickable.
    # Height h-10 (approx 40px) to match the previous icon box size looks good.
    # Added some negative margin if needed but standard is fine.
    
    new_logo_html = """<div onclick="window.location.href='index.html'" class="cursor-pointer">
                <img src="logo_new.png" alt="App.vn" class="h-9 object-contain">
            </div>"""
            
    # Replace
    new_content = content[:start_idx] + new_logo_html + content[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully replaced logo structure.")

if __name__ == "__main__":
    main()
