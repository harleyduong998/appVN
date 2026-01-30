import re

def fix_v16_colors():
    file_path = 'index_v16.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Mapping based on V10
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
        'modules/miniapp.html': 'blue',
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
        'modules/zalo-oa.html': 'blue',
        'modules/web-design.html': 'indigo',
        'modules/datatables.html': 'slate'
    }

    # Strategy: Find the anchor with href="modules/..." and then update the inner div classes.
    # The structure:
    # <a href="KEY" ...>
    #    <div class="... text-OLD-500 ... group-hover:bg-OLD-500 ...">
    
    for href, color in color_map.items():
        # Regex to find the block for this href
        # We need to capture the Div content to replace colors.
        
        # Pattern:
        # href="KEY" (anything until) <div class="(CLASSES)"
        
        # We want to replace `text-\w+-500` with `text-{color}-500`
        # and `group-hover:bg-\w+-500` with `group-hover:bg-{color}-500`
        # inside the block following the href.
        
        # Since regex overlap is tricky, let's split by href or find specific blocks.
        # But global replace of `text-\w+-500` is dangerous.
        
        # Let's locate the specific A tag start.
        start_idx = content.find(f'href="{href}"')
        if start_idx == -1:
            continue
            
        # Find the end of this A tag
        end_idx = content.find('</a>', start_idx)
        if end_idx == -1:
            continue
            
        block = content[start_idx:end_idx]
        
        # Perform replacement in this block
        new_block = re.sub(r'text-\w+-500', f'text-{color}-500', block)
        new_block = re.sub(r'group-hover:bg-\w+-500', f'group-hover:bg-{color}-500', new_block)
        
        # Check if we messed up text-white (group-hover:text-white or just text-white).
        # regex `text-\w+-500` should not match `text-white`.
        
        # Update content slice
        content = content[:start_idx] + new_block + content[end_idx:]

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_v16_colors()
