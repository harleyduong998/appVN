import re

def add_hover_lift():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the anchor class
    # Current: class="flex flex-col items-center justify-center gap-4 hover:opacity-80 transition-opacity"
    # Target: class="flex flex-col items-center justify-center gap-4 hover:opacity-100 transition-all duration-300 hover:-translate-y-2 group"
    
    # Note: opacity-80 on hover might be hiding the nice gradient. 
    # Let's remove hover:opacity-80 or make it subtle (hover:opacity-90).
    # And add the transform.
    
    old_class = 'class="flex flex-col items-center justify-center gap-4 hover:opacity-80 transition-opacity"'
    new_class = 'class="flex flex-col items-center justify-center gap-4 transition-transform duration-300 hover:-translate-y-2 group"'
    
    # Wait, the opacity transition was `transition-opacity`. If I remove it, the opacity change will be instant if I kept it.
    # But I removed `hover:opacity-80`. 
    # Let's keep a slight opacity change? Maybe brightness.
    # The user asked just for "lift". So let's focus on lift.
    # If the user previously had opacity change, maybe I should keep it or improve it.
    # Apple icons darken slightly or stay same.
    # Let's just do lift.
    
    if old_class in content:
        content = content.replace(old_class, new_class)
    else:
        # Fallback regex if spacing/attributes order differs
        pattern = r'class="flex flex-col items-center justify-center gap-4 hover:opacity-80 transition-opacity"'
        content = re.sub(pattern, new_class, content)
        
    # Also, we need to make sure the icon *inside* doesn't do weird things if we lift the parent.
    # Lifting the parent lifts everything (icon + text). This is usually what we want for "Apps".
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    add_hover_lift()
