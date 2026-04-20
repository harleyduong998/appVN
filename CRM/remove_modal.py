import sys
import os

filepath = r'd:\AIDesign\lixi\stuff2\CRM\invoice.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace x-data from body
content = content.replace('<body class="min-h-screen flex flex-col" x-data="{ isAddInvoiceModalOpen: false }">', '<body class="min-h-screen flex flex-col">')

# Modify the button
content = content.replace('<button @click="isAddInvoiceModalOpen = true" class="px-4 py-2 bg-blue-600 border border-blue-600 rounded-lg text-[13px] font-bold text-white hover:bg-blue-700 hover:border-blue-700 transition-colors shadow-sm flex items-center gap-2">', '<button class="px-4 py-2 bg-blue-600 border border-blue-600 rounded-lg text-[13px] font-bold text-white hover:bg-blue-700 hover:border-blue-700 transition-colors shadow-sm flex items-center gap-2">')

# Remove modal blocks
start_marker = '    <!-- Add Invoice Modal -->'
end_marker = '</body>'
start_idx = content.find(start_marker)
if start_idx != -1:
    end_idx = content.find(end_marker, start_idx)
    if end_idx != -1:
        # We cut everything between start_idx and end_idx
        content = content[:start_idx] + content[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
