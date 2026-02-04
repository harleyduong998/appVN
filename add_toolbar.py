
import os

def main():
    try:
        with open('index.html', 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("Error: index.html not found.")
        return

    # Find the insertion point: Top of <main>
    # <main class="flex-1 pt-24 pb-12 px-6 max-w-7xl mx-auto w-full">
    
    main_start_tag = '<main class="flex-1 pt-24 pb-12 px-6 max-w-7xl mx-auto w-full">'
    
    if main_start_tag not in content:
        # Try finding generic main if specific class match fails
        idx = content.find('<main')
        if idx != -1:
            end_bracket = content.find('>', idx)
            main_start_tag = content[idx:end_bracket+1]
        else:
            print("Error: <main> tag not found.")
            return

    # New Toolbar HTML
    new_toolbar = """
        <!-- Top Toolbar -->
        <div class="flex flex-col md:flex-row items-center justify-between gap-4 mb-2 bg-white p-3 rounded-lg shadow-sm border border-indigo-100">
            <!-- Search -->
            <div class="relative w-full md:w-80">
                <i class="fa-solid fa-magnifying-glass absolute left-3 top-1/2 -translate-y-1/2 text-slate-400 text-sm"></i>
                <input type="text" placeholder="Tìm kiếm ứng dụng" class="w-full pl-9 pr-4 py-2 bg-slate-50/50 border border-slate-200/80 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500/20 focus:border-blue-500 transition-all text-sm text-slate-600">
            </div>
            
            <!-- Actions -->
            <div class="flex items-center gap-2 w-full md:w-auto overflow-x-auto pb-1 md:pb-0 no-scrollbar">
                 <button class="flex items-center gap-1.5 px-3 py-2 bg-[#1B3DA1] text-white rounded-md text-sm font-medium hover:bg-blue-800 transition-colors shadow-sm whitespace-nowrap">
                    <i class="fa-solid fa-star text-xs"></i>
                    Ứng dụng của tôi
                </button>
                <button class="flex items-center gap-1.5 px-3 py-2 bg-white border border-slate-200 text-slate-600 rounded-md text-sm font-medium hover:bg-slate-50 hover:text-blue-600 transition-all whitespace-nowrap">
                    <i class="fa-solid fa-table-cells text-xs"></i>
                    Kho ứng dụng
                </button>
                <button class="flex items-center gap-1.5 px-3 py-2 bg-white border border-slate-200 text-slate-600 rounded-md text-sm font-medium hover:bg-slate-50 hover:text-blue-600 transition-all whitespace-nowrap">
                    <i class="fa-solid fa-box-open text-xs"></i>
                    Gói cước
                </button>
                 <button class="flex items-center gap-1.5 px-3 py-2 bg-white border border-slate-200 text-slate-600 rounded-md text-sm font-medium hover:bg-slate-50 hover:text-blue-600 transition-all whitespace-nowrap">
                    <i class="fa-solid fa-list text-xs"></i>
                    Hiển thị
                </button>
            </div>
        </div>
        """
        
    replacement = main_start_tag + "\n" + new_toolbar
    
    new_content = content.replace(main_start_tag, replacement)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully inserted toolbar above Welcome section.")

if __name__ == "__main__":
    main()
