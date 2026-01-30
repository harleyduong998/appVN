import re

def transfer_cards():
    v10_path = 'd:\\AIDesign\\AppVN\\index_v10.html'
    v18_path = 'd:\\AIDesign\\AppVN\\index_v18.html'
    
    # 1. Read V10 to extract the grid content
    with open(v10_path, 'r', encoding='utf-8') as f:
        v10_content = f.read()
        
    # Find the grid in V10
    # <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4">
    # ...
    # </div> (before </main>)
    
    grid_start_tag = '<div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4">'
    grid_idx = v10_content.find(grid_start_tag)
    
    if grid_idx == -1:
        print("Could not find grid in index_v10.html")
        return
        
    # Find the matching closing div. 
    # Since V10 structure is: Grid -> </main>, we can look for the div ending before </main>
    main_end_idx = v10_content.find('</main>')
    grid_end_idx = v10_content.rfind('</div>', 0, main_end_idx)
    
    v10_grid_html = v10_content[grid_idx:grid_end_idx+6] # include </div>
    
    # 2. Read V18 to find where to replace
    with open(v18_path, 'r', encoding='utf-8') as f:
        v18_content = f.read()
        
    # V18 grid start: <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
    v18_grid_start_tag = '<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">'
    
    v18_grid_idx = v18_content.find(v18_grid_start_tag)
    if v18_grid_idx == -1:
         print("Could not find grid in index_v18.html")
         # Maybe regex match if spacing differs?
         return
         
    v18_main_end_idx = v18_content.find('</main>')
    v18_grid_end_idx = v18_content.rfind('</div>', 0, v18_main_end_idx)
    
    # Replace
    new_v18_content = v18_content[:v18_grid_idx] + v10_grid_html + v18_content[v18_grid_end_idx+6:]
    
    with open(v18_path, 'w', encoding='utf-8') as f:
        f.write(new_v18_content)
        
    print("Transferred V10 grid to V18.")

if __name__ == "__main__":
    transfer_cards()
