
import re

def main():
    file_path = 'index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return

    # We want to replace `mr-5` with `mr-2` and `gap-3` with `gap-2` specifically within the module cards (or simpler, globally if safe).
    # The `mr-5` on the icon div is quite specific: `class="... z-10 mr-5 group-hover:bg-..."`
    # The `gap-3` is on the anchor: `class="... justify-start gap-3 h-[85px] ..."`
    
    # Let's use robust regex to target these class strings.
    
    # 1. Replace mr-5 with mr-2 inside the icon div class context
    # Context: flex items-center justify-center ... z-10 mr-5 group-hover ...
    # We can just replace "z-10 mr-5" with "z-10 mr-2" to be fairly safe and specific.
    
    new_content = content.replace("z-10 mr-5", "z-10 mr-2")
    
    # 2. Replace gap-3 with gap-2 inside the anchor class context
    # Context: justify-start gap-3 h-[85px]
    new_content = new_content.replace("justify-start gap-3 h-[85px]", "justify-start gap-2 h-[85px]")
    
    if new_content == content:
        print("No changes made. Check search strings.")
    else:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully reduced gaps in module buttons.")

if __name__ == "__main__":
    main()
