
import glob
import re

file_path = 'c:/Users/mandi/Downloads/studiova-bootstrap-template-v1/src/html/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

original_content = content

# 1. Styles Injection
custom_css = """
  <style>
    .btn-hero-custom {
      background-color: #ffffff !important;
      color: #1F2A2E !important;
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
      background-color: #1F2A2E !important;
      color: #FF0000 !important;
      border-color: #FF0000 !important;
    }
    .btn-hero-custom:hover .btn-text {
      color: #FF0000 !important;
    }
  </style>
</head>
"""
if '.btn-hero-custom' not in content:
    content = content.replace('</head>', custom_css)

# 2. Resize Logo
# USE SAFE GROUP REF \g<1>
content = re.sub(r'(src="../assets/images/svgs/primary-leaf\.svg" alt="" width=")30(" height=")30(")', r'\g<1>90\g<2>90\g<3>', content)

# 3. Reduce Title Size
content = content.replace('h1 class="mb-0 fs-16 text-white lh-1"', 'h1 class="mb-0 fs-15 text-white lh-1"')

# 4. Update Buttons
new_buttons_html = """              <a href="#projects" class="btn btn-hero-custom">
                <span class="btn-text">Ver proyectos</span>
                <iconify-icon icon="lucide:arrow-up-right" class="btn-icon bg-white text-dark round-52 rounded-circle hstack justify-content-center fs-7 shadow-sm"></iconify-icon>
              </a>
              <a href="#contact" class="btn btn-hero-custom">
                <span class="btn-text">Cotizar ahora</span>
                <iconify-icon icon="lucide:arrow-up-right" class="btn-icon bg-white text-dark round-52 rounded-circle hstack justify-content-center fs-7 shadow-sm"></iconify-icon>
              </a>"""

pattern_btns = r'<div class="d-flex align-items-center gap-3 mt-3">\s*<a href="#projects" class="btn btn-primary">\s*<span class="btn-text text-white">Ver proyectos</span>\s*</a>\s*<a href="#contact" class="btn btn-outline-light">\s*<span class="btn-text">Cotizar ahora</span>\s*</a>\s*</div>'
replacement_btns = f'<div class="d-flex align-items-center gap-3 mt-3">\n{new_buttons_html}\n            </div>'

content = re.sub(pattern_btns, replacement_btns, content, flags=re.DOTALL)

if content != original_content:
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated index.html with hero adjustments.")
else:
    # Fallback debug
    if 'width="30"' in content and 'primary-leaf.svg' in content:
        print("Debug: Logo pattern failed match.")
    if 'fs-16' in content:
        print("Debug: Title replacement failed (maybe already changed?)")
    print("No changes (or patterns failed).")
