
import re

def main():
    file_path = 'index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return

    # 1. Add ID to Welcome Section
    # Look for "Xin chào, Harley!"
    # The parent div is: <div class="mb-4 animate-fade-in-up">
    
    welcome_pattern = r'<div class="mb-4 animate-fade-in-up">\s*<h1 class="text-3xl font-bold text-slate-800 mb-2">Xin chào'
    if re.search(welcome_pattern, content):
        content = re.sub(
            r'<div class="mb-4 animate-fade-in-up">(\s*<h1 class="text-3xl font-bold text-slate-800 mb-2">Xin chào)', 
            r'<div id="welcome-section" class="mb-4 animate-fade-in-up transition-opacity duration-300">\1', 
            content
        )
    else:
        print("Could not find Welcome Section to add ID")

    # 2. Add ID and Sticky Class to Toolbar
    # The toolbar starts with: <div class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white
    # We want to add `sticky top-16 z-30 transition-all duration-300`
    # top-16 is 4rem = 64px. If header is 64px, this sits right below.
    
    toolbar_pattern = r'<div\s+class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white p-3 rounded-lg shadow-sm border border-indigo-100">'
    
    replacement_toolbar = r'<div id="sticky-toolbar" class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white p-3 rounded-lg shadow-sm border border-indigo-100 sticky top-[70px] z-40 transition-all duration-300">'
    
    if re.search(toolbar_pattern, content):
        content = re.sub(toolbar_pattern, replacement_toolbar, content)
    else:
        # Try looser match if whitespace differs
        toolbar_pattern_loose = r'<div\s+class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white p-3 rounded-lg shadow-sm border border-indigo-100">'
        content = re.sub(r'(<div\s+class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white p-3 rounded-lg shadow-sm border border-indigo-100")', 
                         r'<div id="sticky-toolbar" class="flex flex-col md:flex-row items-center justify-between gap-4 mb-6 bg-white p-3 rounded-lg shadow-sm border border-indigo-100 sticky top-[70px] z-40 transition-all duration-300"', 
                         content)

    # 3. Add Script for Scroll Effect
    # We want Class 1 (Welcome) to fade out.
    # We want Class 2 (Toolbar) to possibly change style or just be sticky.
    # The user said "Class 1 bị ẩn mờ đi" -> Opacity reduces as we scroll.
    
    script_content = """
    <script>
        window.addEventListener('scroll', function() {
            const welcomeSection = document.getElementById('welcome-section');
            const toolbar = document.getElementById('sticky-toolbar');
            
            if (welcomeSection) {
                const scrollY = window.scrollY;
                // Fade out welcome section over 100px of scroll
                const opacity = Math.max(0, 1 - (scrollY / 100));
                welcomeSection.style.opacity = opacity;
                
                // Optional: Hide completely to avoid clicking hidden elements
                if (opacity <= 0) {
                    welcomeSection.style.visibility = 'hidden';
                    welcomeSection.style.height = '0';
                    welcomeSection.style.margin = '0';
                    welcomeSection.style.overflow = 'hidden';
                } else {
                    welcomeSection.style.visibility = 'visible';
                    welcomeSection.style.height = 'auto';
                    welcomeSection.style.marginBottom = '1rem'; // restore mb-4 (approx)
                }
            }
            
            // Optional: Add shadow to toolbar when pinned
            /*
            if (toolbar) {
                if (window.scrollY > 50) {
                    toolbar.classList.add('shadow-md');
                    toolbar.classList.remove('shadow-sm');
                } else {
                    toolbar.classList.remove('shadow-md');
                    toolbar.classList.add('shadow-sm');
                }
            }
            */
        });
    </script>
    """
    
    # Insert script before </body>
    if "</body>" in content:
        content = content.replace("</body>", script_content + "\n</body>")
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Successfully implemented scroll effects.")

if __name__ == "__main__":
    main()
