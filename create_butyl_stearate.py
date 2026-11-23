import os
import re

slug = "butyl-stearate-comedogenic-acne.html"

# Update index.html
with open('index.html', 'r') as f:
    index_html = f.read()

link_html = f'<div><a href="./products/{slug}" class="text-xs text-[#7C726E] hover:text-[#D98A96] transition-colors">Butyl Stearate (Acne Safe?)</a></div>'
index_html = index_html.replace(
    '<div class="flex flex-wrap gap-x-6 gap-y-3">',
    f'<div class="flex flex-wrap gap-x-6 gap-y-3">\n          {link_html}'
)

with open('index.html', 'w') as f:
    f.write(index_html)
