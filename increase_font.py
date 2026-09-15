import re

with open('src/pages/index.astro', 'r') as f:
    content = f.read()

def replace_rem(match):
    val = float(match.group(1))
    new_val = val + 0.125
    # Format to remove trailing zeros and dot if integer
    return f"font-size: {new_val:g}rem;"

def replace_px(match):
    val = float(match.group(1))
    new_val = val + 2
    return f"font-size: {new_val:g}px;"

content = re.sub(r'font-size:\s*([0-9.]+)rem;', replace_rem, content)
content = re.sub(r'font-size:\s*([0-9.]+)px;', replace_px, content)

with open('src/pages/index.astro', 'w') as f:
    f.write(content)

print("Updated font sizes in index.astro")
