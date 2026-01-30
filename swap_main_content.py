import re

def swap_main():
    file1 = 'index.html'
    file2 = 'index_v10.html'
    
    with open(file1, 'r', encoding='utf-8') as f:
        content1 = f.read()
        
    with open(file2, 'r', encoding='utf-8') as f:
        content2 = f.read()
        
    # Regex to capture <main ...> ... </main>
    # Utilizing dotall to match newlines
    main_pattern = re.compile(r'(<main[^>]*>.*?</main>)', re.DOTALL)
    
    match1 = main_pattern.search(content1)
    match2 = main_pattern.search(content2)
    
    if not match1 or not match2:
        print("Error: Could not find <main> tag in one or both files.")
        return
        
    main_content1 = match1.group(1)
    main_content2 = match2.group(1)
    
    print(f"Found main block in {file1}: {len(main_content1)} chars")
    print(f"Found main block in {file2}: {len(main_content2)} chars")
    
    # Swap
    new_content1 = content1.replace(main_content1, main_content2)
    new_content2 = content2.replace(main_content2, main_content1)
    
    with open(file1, 'w', encoding='utf-8') as f:
        f.write(new_content1)
        
    with open(file2, 'w', encoding='utf-8') as f:
        f.write(new_content2)
        
    print("Successfully swapped main content.")

if __name__ == "__main__":
    swap_main()
