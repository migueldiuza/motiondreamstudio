
import glob
import re

file_path = 'c:/Users/mandi/Downloads/studiova-bootstrap-template-v1/src/html/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# 1. Styles Injection
# Inject the custom button style into the head
custom_css = """
  <style>
    .btn-hero-custom {
      background-color: #ffffff !important;
      color: #1F2A2E !important; /* Dark color from variables */
      border: 1px solid #ffffff !important;
      transition: all 0.3s ease;
      display: inline-flex;
      align-items: center;
      gap: 10px;
    }
    .btn-hero-custom .btn-text {
      color: #1F2A2E !important;
    }
    .btn-hero-custom:hover {
      background-color: #1F2A2E !important; /* Dark bg */
      color: #FF0000 !important; /* Red text */
      border-color: #FF0000 !important;
    }
    .btn-hero-custom:hover .btn-text {
      color: #FF0000 !important;
    }
    /* Icon default state (already bg-white text-dark in HTML) */
    /* On hover, maybe make icon dark or keep white? */
    /* User: "icon that other buttons have with the animation... changes place" */
    /* The animation is usually on the button or icon class. I'll rely on existing classes for animation. */
  </style>
</head>
"""
if '.btn-hero-custom' not in content:
    content = content.replace('</head>', custom_css)

# 2. Resize Logo
# Target: <img src="../assets/images/svgs/primary-leaf.svg" alt="" width="30" height="30"
# Replace with 90x90 to be noticeably bigger
content = re.sub(r'(src="../assets/images/svgs/primary-leaf\.svg" alt="" width=")30(" height=")30(")', r'\190\290\3', content)

# 3. Reduce Title Size
# Target: <h1 class="mb-0 fs-16 text-white lh-1">Motion Dreams</h1>
# Replace fs-16 with fs-14 (60px) or fs-15 (72px). Let's try fs-15 for "a bit smaller" first (128 -> 72 is huge, but maybe 128 was too big).
# Let's try fs-1 or display-1? 
# styles.css says fs-16 is 128px. fs-15 is 72px.
# "Un poco mas pequeña" -> If it was 128, 72 is HALF. That's a lot smaller.
# Maybe I should use style="font-size: 6rem;" (approx 96px) to be intermediate?
# I'll stick to a utility class if possible. fs-14 is 60px.
# Let's try changing fs-16 to fs-14 for a significant reduction if the user thinks 16 is too big.
# Or maybe the user meant "un poco" so 90px? 
# I'll modify the class to `fs-15` first. If it's too small I can adjust.
content = content.replace('h1 class="mb-0 fs-16 text-white lh-1"', 'h1 class="mb-0 fs-15 text-white lh-1"')

# 4. Update Buttons
# Target the specific block
# We need to replace:
# <a href="#projects" class="btn btn-primary">
#   <span class="btn-text text-white">Ver proyectos</span>
# </a>
# <a href="#contact" class="btn btn-outline-light">
#   <span class="btn-text">Cotizar ahora</span>
# </a>

# New Structure (using .btn-hero-custom and adding icon)
# Note: The icon classes match the "Recent Work" button example.
new_buttons_html = """              <a href="#projects" class="btn btn-hero-custom">
                <span class="btn-text">Ver proyectos</span>
                <iconify-icon icon="lucide:arrow-up-right" class="btn-icon bg-white text-dark round-52 rounded-circle hstack justify-content-center fs-7 shadow-sm"></iconify-icon>
              </a>
              <a href="#contact" class="btn btn-hero-custom">
                <span class="btn-text">Cotizar ahora</span>
                <iconify-icon icon="lucide:arrow-up-right" class="btn-icon bg-white text-dark round-52 rounded-circle hstack justify-content-center fs-7 shadow-sm"></iconify-icon>
              </a>"""

# Use Regex to match the block loosely
pattern_btns = r'<div class="d-flex align-items-center gap-3 mt-3">\s*<a href="#projects" class="btn btn-primary">\s*<span class="btn-text text-white">Ver proyectos</span>\s*</a>\s*<a href="#contact" class="btn btn-outline-light">\s*<span class="btn-text">Cotizar ahora</span>\s*</a>\s*</div>'

# Replacement (keeping the wrapper div)
replacement_btns = f'<div class="d-flex align-items-center gap-3 mt-3">\n{new_buttons_html}\n            </div>'

content = re.sub(pattern_btns, replacement_btns, content, flags=re.DOTALL)

if content != original_content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html with hero adjustments.")
else:
    print("No changes made to index.html (patterns might not match).")
