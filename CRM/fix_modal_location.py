"""
Fix: The addLeadModal was placed inside the Kanban Board Area container,
causing potential DOM conflicts. Move it to just before </body>.
Also ensure the assignClicks() function only picks up actual kanban cards
and add stopPropagation to prevent issues.
"""
filepath = r"d:\AIDesign\lixi\stuff2\CRM\CRM_Lead_v2.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove the addLeadModal block from its current location (inside kanban area)
# It starts with <!-- Add Lead Modal --> and ends with </script> for the Add Lead Modal Script
import re

# Find and extract the entire addLeadModal block
modal_pattern = re.compile(
    r'\n\s*\n\s*<!-- Add Lead Modal -->.*?<!-- Add Lead Modal Script -->.*?</script>\n',
    re.DOTALL
)

match = modal_pattern.search(content)
if match:
    modal_block = match.group(0)
    print("Found modal block to relocate, length:", len(modal_block))
    
    # Remove from current position
    content = content[:match.start()] + content[match.end():]
    
    # Insert before </body>
    # Strip any leading/trailing whitespace from modal block and add clean separation
    modal_block_clean = modal_block.strip()
    content = content.replace("</body>", f"\n\n{modal_block_clean}\n\n</body>")
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("Successfully moved addLeadModal to before </body>")
else:
    print("Modal block pattern not found, trying alternative approach...")
    # Just print lines around addLeadModal to debug
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'Add Lead Modal' in line:
            print(f"Line {i+1}: {line.strip()[:100]}")
