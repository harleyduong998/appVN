import re

def apply_categories():
    file_path = 'd:\\AIDesign\\AppVN\\index_v18.html'
    
    # Mapping href -> categories
    # Categories: recent, sales, contact, marketing, products, content, design, support, report, other
    mapping = {
        'modules/sales.html': 'recent sales',
        'modules/product.html': 'products',
        'modules/customer.html': 'recent contact',
        'modules/warehouse.html': 'recent products',
        'modules/report.html': 'recent report',
        'modules/crm.html': 'contact',
        'modules/automation.html': 'support',
        'modules/promotions.html': 'sales marketing',
        'modules/flashsale.html': 'sales marketing',
        'modules/loyalty.html': 'marketing',
        'modules/combo.html': 'sales',
        'modules/rfm.html': 'marketing',
        'modules/workchat.html': 'contact',
        'modules/callcenter.html': 'contact',
        'modules/feedback.html': 'contact',
        'modules/booking.html': 'content',
        'modules/events.html': 'content',
        'modules/warranty.html': 'products',
        'modules/einvoice.html': 'sales support',
        'modules/debt.html': 'sales',
        'modules/payment.html': 'sales',
        'modules/prepaid.html': 'sales',
        'modules/miniapp.html': 'content',
        'modules/webview.html': 'content',
        'modules/agents.html': 'contact',
        'modules/integration.html': 'support',
        'modules/shipping.html': 'products',
        'modules/imagedesign.html': 'design',
        'modules/emaildesign.html': 'design marketing',
        'modules/templates.html': 'design',
        'modules/storage.html': 'support',
        'modules/settings.html': 'support',
        'modules/realestate.html': 'other'
    }

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find <a href="..."> tags inside the grid
    # We want to add class="module-card" and data-categories="..."
    # We'll simple replace the href line with href + attributes if it's one of the known modules
    
    for href, categories in mapping.items():
        # V10 Structure:
        # <a href="modules/sales.html"
        #   class="bg-white rounded-xl ...">
        
        # Regex to find match: <a href="href" (whitespace) class="
        
        pattern = re.compile(r'(<a\s+href="' + re.escape(href) + r'"\s+class=")([^"]*)(")', re.DOTALL)
        
        # We also need to add 'module-card' back to the classes?
        # Yes, filtering logic uses .module-card class.
        
        def replacer(match):
            prefix = match.group(1) # <a href="..." \n class="
            classes = match.group(2)
            suffix = match.group(3)
            
            new_classes = classes
            if 'module-card' not in classes:
                new_classes = 'module-card ' + classes
                
            # We want to inject data-categories BEFORE the class attribute or just update the tag.
            # My logic in original file was a bit complex.
            # Simpler: just replace the href line to include data-categories.
            
            # Use basic string replace for the HREF part to add data-categories?
            pass
            return match.group(0)

        # Better approach:
        # Read file content.
        # For each href:
        # Check if already has data-categories (idempotent)
        # Regex Replace:
        # Find: <a href="HREF"
        # Replace: <a href="HREF" data-categories="CATEGORIES"
        
        # Also need to add class "module-card" to the class list.
        # Find: class="
        # Replace: class="module-card 
        # But only for THIS tag.
        
        # Combined Regex:
        # (<a\s+href="HREF")([^>]*)class="
        # This matches everything up to class.
        
        search_pattern = re.compile(r'(<a\s+href="' + re.escape(href) + r'")([^>]*)class="')
        
        if search_pattern.search(content):
             # Add data-categories
             content = content.replace(f'href="{href}"', f'href="{href}" data-categories="{categories}"')
             
             # Now find the class attribute for this modified tag
             # <a href="..." data-categories="..." ... class="...
             
             # We can just look for the string sequence we just created
             # And find the next class="
             
             marker = f'href="{href}" data-categories="{categories}"'
             # Regex to find class after this marker
             class_pattern = re.compile(r'(' + re.escape(marker) + r'[^>]*class=")([^"]*)')
             
             def class_adder(m):
                 if 'module-card' not in m.group(2):
                     return m.group(1) + 'module-card ' + m.group(2)
                 return m.group(0)
                 
             content = class_pattern.sub(class_adder, content)
            
    # Finally, ensure "Vừa truy cập" button is triggered or items shown.
    # The script in HTML defaults to nothing? No, logic says "if categories.includes(cat) -> show".
    # Initially all might be shown or hidden?
    # I should add 'recent' to the list of categories for the first 4 items, AND maybe trigger the click on load.
    # In index_v18.html Script:
    # document.addEventListener('DOMContentLoaded', () => { filterModules('recent', document.querySelector('.category-btn')); });
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Categories applied.")

if __name__ == "__main__":
    apply_categories()
