import re

def fix_v17_zalo():
    file_path = 'index_v17.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Zalo SVG Element
    # w-10 h-10 to match text-4xl approx size
    zalo_icon = '<img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Icon_of_Zalo.svg" alt="Zalo" class="w-10 h-10 object-contain hover:scale-110 transition-transform duration-300">'

    # 1. Mini App Builder
    # Find the block for miniapp.html and replace <i ... fa-cube ...> with img
    # Identify by href
    
    def replace_cube_with_zalo(match):
        block = match.group(0)
        # Replace the <i> tag with <img>
        # The <i> tag has: <i class="fa-solid fa-cube ...></i>
        return re.sub(r'<i class="fa-solid fa-cube[^>]*></i>', zalo_icon, block)

    # Mini App
    pattern_miniapp = re.compile(r'<a href="modules/miniapp.html".*?</a>', re.DOTALL)
    content = pattern_miniapp.sub(replace_cube_with_zalo, content)

    # Zalo OA
    pattern_zalo = re.compile(r'<a href="modules/zalo-oa.html".*?</a>', re.DOTALL)
    content = pattern_zalo.sub(replace_cube_with_zalo, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    fix_v17_zalo()
