
import re
import os

def main():
    file_path = 'index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return

    # 1. Parse all existing modules
    # Regex to capture each module block: <!-- Number. Name --> followed by <a> tag
    module_pattern = re.compile(r'(<!--\s*\d+\.\s*(.*?)-->\s*<a href="modules/.*?".*?</a>)', re.DOTALL)
    
    modules = []
    seen_keys = set()
    
    # scan entire file content for modules
    for match in module_pattern.finditer(content):
        full_block = match.group(1)
        name_comment = match.group(2).strip()
        key = name_comment.lower()
        
        # Deduplicate based on unique key + block content hash approx
        if key not in seen_keys:
            modules.append({
                'key': key,
                'block': full_block,
                'name': name_comment
            })
            seen_keys.add(key)
            
    print(f"Found {len(modules)} modules.")
    
    # 2. Define New Categories
    # Keys must match lowercased comment names approximately
    
    categories = [
        {
            "id": "sales",
            "name": "BÁN HÀNG",
            "icon": "fa-solid fa-cart-shopping",
            "items": ["quản lý bán hàng", "bán hàng", "hóa đơn", "hóa đơn điện tử", "công nợ", "thanh toán", "cổng thanh toán", "thẻ trả trước", "bất động sản", "booking"]
        },
        {
            "id": "contact",
            "name": "LIÊN HỆ",
            "icon": "fa-regular fa-address-book",
            "items": ["khách hàng", "workchatv2", "zalo oa", "tổng đài", "tổng đài - sms - zns", "feedback"]
        },
        {
            "id": "marketing",
            "name": "MARKETING",
            "icon": "fa-solid fa-bullhorn",
            "items": ["crm", "automation", "ưu đãi", "flash sale", "loyalty", "combo", "rfm", "sự kiện", "khóa học - sự kiện", "cộng tác viên"]
        },
         {
            "id": "inventory",
            "name": "HÀNG HÓA & TỒN KHO",
            "icon": "fa-solid fa-boxes-stacked",
            "items": ["sản phẩm", "kho hàng", "vận chuyển", "vận chuyển nội bộ", "bảo hành"]
        },
        {
            "id": "content",
            "name": "QUẢN LÝ NỘI DUNG",
            "icon": "fa-solid fa-pen-to-square",
            "items": ["lưu trữ", "webview", "quản lý nội dung"]
        },
        {
            "id": "design",
            "name": "CÔNG CỤ THIẾT KẾ",
            "icon": "fa-solid fa-paintbrush",
            "items": ["thiết kế ảnh", "thiết kế email", "thiết kế website", "mẫu in"]
        },
        {
            "id": "support",
            "name": "ỨNG DỤNG HỖ TRỢ",
            "icon": "fa-solid fa-screwdriver-wrench",
            "items": ["mini app", "mini app builder", "tích hợp", "cài đặt"]
        },
        {
            "id": "reports",
            "name": "BÁO CÁO - THỐNG KÊ",
            "icon": "fa-solid fa-chart-line",
            "items": ["báo cáo", "bảng dữ liệu"]
        }
    ]
    
    # 3. Assign modules
    categorized_html = ""
    assigned_keys = set()
    
    for cat in categories:
        cat_modules_html = []
        for item_key in cat["items"]:
            # Find module matching this key
            for m in modules:
                # Flexible matching
                if item_key == m['key'] or item_key in m['key'] or m['key'] in item_key:
                     if m['key'] not in assigned_keys:
                         cat_modules_html.append(m['block'])
                         assigned_keys.add(m['key'])
                         # Don't break immediately, in case multiple modules match generic key? 
                         # No, specific keys are better. 
                         # But let's assume one match per item_key iteration is safe enough or 
                         # we loop modules driven by modules to ensure all are found.
                         
        # Add section if not empty
        if cat_modules_html:
            section_html = f"""
            <!-- Category: {cat['name']} -->
            <div class="mb-4">
                <div class="flex items-center gap-2 mb-4 text-[#1B3DA1] font-['Montserrat'] font-extrabold uppercase text-lg tracking-wide border-b-2 border-indigo-100 pb-2 cursor-pointer select-none hover:bg-slate-50 transition-colors rounded-t-lg px-2 pt-2" onclick="toggleCategory('{cat['id']}')">
                    <span class="bg-indigo-50 p-1 rounded text-indigo-600">
                        <i class="{cat['icon']}"></i>
                    </span>
                    <span>{cat['name']}</span>
                    <i id="icon-{cat['id']}" class="fa-solid fa-chevron-down ml-3 text-slate-400 transition-transform duration-300"></i>
                </div>
                <!-- Collapsible Grid -->
                <div id="cat-{cat['id']}" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4 transition-all duration-300 origin-top">
                    {"".join(cat_modules_html)}
                </div>
            </div>
            """
            categorized_html += section_html

    # 4. Handle Uncategorized (Khác)
    uncategorized = []
    for m in modules:
        if m['key'] not in assigned_keys:
            uncategorized.append(m['block'])
            
    if uncategorized:
        section_html = f"""
        <!-- Category: KHÁC -->
        <div class="mb-4">
             <div class="flex items-center gap-2 mb-4 text-[#1B3DA1] font-['Montserrat'] font-extrabold uppercase text-lg tracking-wide border-b-2 border-indigo-100 pb-2 cursor-pointer select-none hover:bg-slate-50 transition-colors rounded-t-lg px-2 pt-2" onclick="toggleCategory('other')">
                <span class="bg-indigo-50 p-1 rounded text-indigo-600">
                    <i class="fa-solid fa-shapes"></i>
                </span>
                <span>KHÁC</span>
                <i id="icon-other" class="fa-solid fa-chevron-down ml-3 text-slate-400 transition-transform duration-300"></i>
             </div>
            <div id="cat-other" class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-5 xl:grid-cols-6 gap-4 transition-all duration-300 origin-top">
                {"".join(uncategorized)}
            </div>
        </div>
        """
        categorized_html += section_html

    # Add Script for Toggle
    categorized_html += """
    <script>
    function toggleCategory(id) {
        const grid = document.getElementById('cat-' + id);
        const icon = document.getElementById('icon-' + id);
        
        if (grid.classList.contains('hidden')) {
            grid.classList.remove('hidden');
            grid.classList.add('grid');
            setTimeout(() => {
                grid.style.opacity = '1';
                grid.style.maxHeight = '2000px'; 
            }, 10);
            icon.style.transform = 'rotate(0deg)';
        } else {
            grid.style.opacity = '0';
            grid.style.maxHeight = '0';
            setTimeout(() => {
                grid.classList.add('hidden');
                grid.classList.remove('grid');
            }, 300);
            icon.style.transform = 'rotate(-90deg)';
        }
    }
    </script>
    """

    # 5. Replacement
    # We want to replace the block that contains all categories.
    # It starts with <!-- Categorized Modules --> (if present) or <!-- Modules Grid --> (old)
    # or just the block between Search/Actions and Footer.
    
    # Robust start finding
    start_point = -1
    if "<!-- Categorized Modules -->" in content:
        start_point = content.find("<!-- Categorized Modules -->")
    elif "<!-- Modules Grid -->" in content:
        start_point = content.find("<!-- Modules Grid -->")
        
    # Robust end finding
    end_point = content.find("</main>")
    
    if start_point != -1 and end_point != -1:
        new_full_content = content[:start_point] + "<!-- Categorized Modules -->\n" + categorized_html + "\n        " + content[end_point:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
        print("Successfully re-categorized modules.")
    else:
        print("Could not find insertion points.")

if __name__ == "__main__":
    main()
