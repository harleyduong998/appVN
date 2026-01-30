import re

def fix_v17_colors():
    file_path = 'index_v17.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping based on V10 (same as v16 fix)
    # The target replacement pattern in V17 is:
    # <i class="... bg-gradient-to-br from-blue-600 to-blue-400 ...">
    # We want to replace blue-600/400 with COLOR-600/400.
    
    color_map = {
        'modules/sales.html': 'blue',
        'modules/product.html': 'amber',
        'modules/customer.html': 'emerald',
        'modules/warehouse.html': 'gray',
        'modules/report.html': 'indigo',
        'modules/crm.html': 'rose',
        'modules/automation.html': 'purple',
        'modules/promotions.html': 'red',
        'modules/flashsale.html': 'red',
        'modules/loyalty.html': 'yellow',
        'modules/combo.html': 'orange',
        'modules/rfm.html': 'violet',
        'modules/workchat.html': 'pink',
        'modules/callcenter.html': 'green',
        'modules/feedback.html': 'yellow',
        'modules/booking.html': 'blue',
        'modules/events.html': 'orange',
        'modules/warranty.html': 'teal',
        'modules/einvoice.html': 'blue',
        'modules/debt.html': 'indigo',
        'modules/payment.html': 'emerald',
        'modules/prepaid.html': 'emerald',
        'modules/miniapp.html': 'blue', # Image, handled separately/ignored
        'modules/webview.html': 'purple',
        'modules/agents.html': 'cyan',
        'modules/integration.html': 'cyan',
        'modules/shipping.html': 'amber',
        'modules/imagedesign.html': 'rose',
        'modules/emaildesign.html': 'fuchsia',
        'modules/templates.html': 'gray',
        'modules/storage.html': 'stone',
        'modules/settings.html': 'slate',
        'modules/realestate.html': 'sky',
        'modules/zalo-oa.html': 'blue', # Image
        'modules/web-design.html': 'indigo',
        'modules/datatables.html': 'slate'
    }

    # Iterate through map and find the specific link block
    
    for href, color in color_map.items():
        # Skip if default blue (optional optimization, but good to enforce everything)
        # if color == 'blue': continue 

        # Find the block: href="..." ... </a>
        # Then inside that block find the <i> tag with bg-gradient...
        
        # Regex for the block
        # <a href="KEY" ...> ... </a>
        # BE CAREFUL with regex matching across newlines.
        
        # We can search by string find to be safer with exact href match
        start_marker = f'href="{href}"'
        start_idx = content.find(start_marker)
        if start_idx == -1:
            continue
            
        # Find closing </a>
        end_idx = content.find('</a>', start_idx)
        if end_idx == -1:
            continue
            
        block = content[start_idx:end_idx]
        
        # Check if it has an <i> tag with gradient
        # Pattern: from-blue-600 to-blue-400
        # or just from-\w+-600
        
        if '<img' in block:
            # Skip image based blocks (Zalo, Miniapp)
            continue
            
        # Replace the colors
        # We look for from-\w+-600 to-\w+-400 (or similar numbers if they vary)
        # In refine_v17_nobox, we set them to from-blue-600 to-blue-400
        
        new_block = re.sub(r'from-\w+-\d+', f'from-{color}-600', block)
        new_block = re.sub(r'to-\w+-\d+', f'to-{color}-400', new_block)
        
        # Replace in content
        content = content[:start_idx] + new_block + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_v17_colors()
