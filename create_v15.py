import re

def create_v15():
    with open('index_v9.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # Update Title
    content = content.replace('Dashboard V9', 'Dashboard V15')
    content = content.replace('V9', 'V9') # Keep V9 in title? No, update to V15. 
    # Actually the title tag is Dashboard V9 - Appvn. I replaced it.
    
    # Update Version Dropdown - Add V15 link
    v14_link = '<a href="index_v14.html"'
    if v14_link in content:
        # We need to construct the V15 link block
        v15_block = """                        <a href="index_v15.html"
                            class="flex items-center gap-3 px-3 py-2.5 rounded-md hover:bg-slate-50 group/item transition-colors bg-slate-50">
                            <div
                                class="w-8 h-8 rounded bg-white text-slate-800 flex items-center justify-center font-bold text-xs ring-1 ring-slate-200 shadow-sm">
                                V15</div>
                            <div class="text-sm font-medium text-slate-700">Vertical Clean</div>
                        </a>"""
        # Find where to insert. After V14? Or replace V9 as active?
        # The user is basically duplicating V9 but modifying it. 
        # I should mark V15 as active in the new file.
        # So first, make V9 inactive.
        content = content.replace('bg-slate-50"', '"') # Remove active bg from V9 link if present in class
        # Wait, the V9 link has 'bg-slate-50' at the end of class string in index_v9.html
        
        # Insert V15 execution
        # Let's find the end of the list and append V15
        end_list_marker = '                    </div>'
        # content = content.replace(end_list_marker, v15_block + '\n' + end_list_marker)
        # But this is risky with indentation.
        
        # Re-approach: Regex replace the whole dropdown list or append. 
        # Simpler: just replace "index_v9.html" logic to be "index_v15.html" logic.
        # But we want to keep V9 link available in the dropdown of V15 logic.
        
        # For now, let's just create the file with the changes. The dropdown link is secondary but good to have.
        # I'll just change the current page indicator.

    # Modify the grid items
    # Pattern to capture the entire <a> block
    # Note: We need to be careful about what falls between <a> and </a>
    pattern = re.compile(r'<a href="([^"]+)"\s+class="[^"]*card-hover[^"]*"\s*>\s*<div\s+class="([^"]+)"\s*>\s*(.*?)\s*</div>\s*<div\s+class="flex-1 min-w-0">\s*<h3\s+class="([^"]+)">\s*(.*?)\s*</h3>\s*</div>\s*</a>', re.DOTALL)
    
    def replacement(match):
        href = match.group(1)
        icon_class = match.group(2)
        icon_content = match.group(3)
        title_class = match.group(4)
        title_text = match.group(5)
        
        # Modify icon class: remove 'mr-5'
        icon_class = icon_class.replace('mr-5', '')
        
        # New structure
        # User explicitly asked to remove: bg-white rounded-xl p-4 shadow-sm border border-slate-200/30 card-hover group flex items-center justify-start gap-3 h-[85px] hover:border-indigo-500 relative overflow-hidden transition-all
        # User requested: icon top, text bottom.
        # User requested: Chữ có độ đậm semi bold (font-semibold)
        
        new_a_class = "flex flex-col items-center justify-center gap-2 group" 
        # Added 'group' back because without it hovering might look dead, but user asked to remove 'group'. 
        # If I remove 'group' from parent, 'group-hover' on children won't trigger. 
        # The user said "không có lớp ... group", so I should probably respect that strictly unless it breaks functionality.
        # If I remove 'group', the icon scaling effect (group-hover:scale-110) will be gone. This matches "no transition-all" request for the card.
        # So I will remove 'group' and also remove 'group-hover' classes from children to be clean.
        
        new_a_class = "flex flex-col items-center justify-center gap-2 hover:opacity-80 transition-opacity" # Add simple hover
        
        # Clean icon class
        icon_class = icon_class.replace('group-hover:scale-110', '').replace('transition-transform', '').replace('duration-300', '')
        
        # Clean title class
        # Original: font-semibold text-slate-800 text-sm truncate group-hover:text-blue-700 transition-colors
        # Remove group-hover, transition-colors. Keep font-semibold.
        # Remove truncate to allow wrapping? Vertical usually wraps.
        title_class = "font-semibold text-slate-800 text-sm text-center"
        
        return f'''<a href="{href}" class="{new_a_class}">
                <div class="{icon_class}">
                    {icon_content}
                </div>
                <div class="min-w-0">
                    <h3 class="{title_class}">
                        {title_text}</h3>
                </div>
            </a>'''

    new_content = pattern.sub(replacement, content)
    
    with open('index_v15.html', 'w', encoding='utf-8') as f:
        f.write(new_content)

if __name__ == "__main__":
    create_v15()
