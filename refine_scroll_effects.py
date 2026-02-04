
import re

def main():
    file_path = 'index.html'
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print("index.html not found")
        return

    # 1. Increase Toolbar Margin
    # Find the toolbar div and change mb-6 to mb-10 (or even mb-12 for more space)
    # Toolbar ID: id="sticky-toolbar"
    
    # Regex to find the class inside the toolbar div
    toolbar_pattern = r'(id="sticky-toolbar"[^>]*class="[^"]*)mb-6'
    if re.search(toolbar_pattern, content):
        content = re.sub(toolbar_pattern, r'\1mb-10', content)
        print("Updated toolbar margin to mb-10")
    else:
        print("Could not find toolbar margin class")

    # 2. Refine Scroll Script
    # Replace the existing script block with a smoother one.
    # We'll use CSS classes for transition instead of direct JS manipulation of height '0' to 'auto' which is jerky.
    # Actually, strictly animating height from auto to 0 is hard in CSS without max-height.
    # So we will use max-height strategy in JS or CSS.
    
    # Let's add a CSS style block for the welcome-section to handle the transition smoothly.
    # We can inject a style block or just rely on Tailwind classes if possible.
    # The Welcome section already has `transition-opacity duration-300`.
    # We should add `transition-all duration-500 ease-in-out` and `max-h-40` (approx height) -> `max-h-0`.
    
    # First, let's replace the script.
    
    old_script_start = "window.addEventListener('scroll', function() {"
    old_script_end = "});"
    
    # Robust replacement of the specific scroll script we added.
    # We can just match the whole block we added last time mentally.
    
    new_script = """
        window.addEventListener('scroll', function() {
            const welcomeSection = document.getElementById('welcome-section');
            const toolbar = document.getElementById('sticky-toolbar');
            
            if (welcomeSection) {
                const scrollY = window.scrollY;
                const threshold = 50; // threshold to trigger collapse
                
                // We want a smooth opacity fade first
                // Opacity: 1 at 0px, 0 at 100px.
                const opacity = Math.max(0, 1 - (scrollY / 100));
                welcomeSection.style.opacity = opacity;
                
                // Smooth collapse using max-height and margin
                // Instead of abrupt visibility hidden, we toggle a class 'collapsed' 
                // But we need to define that class or set styles directly but smoothly.
                
                if (scrollY > threshold) {
                    // Collapse
                    if (!welcomeSection.classList.contains('collapsed')) {
                        welcomeSection.style.maxHeight = '0';
                        welcomeSection.style.marginBottom = '0';
                        welcomeSection.classList.add('collapsed');
                    }
                } else {
                    // Expand
                    if (welcomeSection.classList.contains('collapsed')) {
                        welcomeSection.style.maxHeight = '150px'; // Approximate height of welcome section
                        welcomeSection.style.marginBottom = '1rem';
                        welcomeSection.classList.remove('collapsed');
                    }
                }
            }
        });
    """
    
    # We need to ensure the Welcome Section has the right transition properties for this to work.
    # <div id="welcome-section" class="mb-4 animate-fade-in-up transition-opacity duration-300">
    # We need to change that class string to include transition-all.
    
    welcome_regex = r'(id="welcome-section"[^>]*class="[^"]*)transition-opacity duration-300'
    replacement_welcome = r'\1transition-all duration-500 ease-in-out overflow-hidden'
    
    if re.search(welcome_regex, content):
        content = re.sub(welcome_regex, replacement_welcome, content)
        print("Updated welcome section classes for smooth transition")
        
    # Now replace the script body.
    # Regex to capture the content inside the scroll event listener
    script_regex = r'window\.addEventListener\(\'scroll\', function\(\) \{[\s\S]*?\}\);'
    
    if re.search(script_regex, content):
        content = re.sub(script_regex, new_script.strip(), content)
        print("Updated scroll script")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    main()
