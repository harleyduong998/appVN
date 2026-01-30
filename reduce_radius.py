import re

def reduce_radius():
    file_path = 'index_v15.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the current radius class
    # Current: rounded-[22px]
    # Target: rounded-2xl (16px) or rounded-xl (12px)
    # The user said "giảm radius icon xuống" (reduce radius). 
    # Current is quite round (squcircle).
    # Let's reduce significantly to notice the change.
    
    # Replace `rounded-[22px]` with `rounded-2xl`
    content = content.replace('rounded-[22px]', 'rounded-2xl')

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    reduce_radius()
