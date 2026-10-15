import re

# Update index.html
with open('index.html', 'r') as f:
    content = f.read()

new_link = '<div><a href="./products/lanolin-comedogenic-acne.html" class="text-xs text-[#7C726E] hover:text-[#D98A96] transition-colors">Lanolin (Acne Safe?)</a></div>'

# find the last </div> in the flex container
if 'gap-x-6 gap-y-3">' in content:
    idx = content.find('gap-x-6 gap-y-3">')
    # find where this div closes, or just insert it right after the class opening
    insert_pos = idx + len('gap-x-6 gap-y-3">')
    new_content = content[:insert_pos] + f"\n          {new_link}" + content[insert_pos:]
    with open('index.html', 'w') as f:
        f.write(new_content)
    print("index.html updated")

# Update sitemap.xml
with open('sitemap.xml', 'r') as f:
    sitemap = f.read()

new_sitemap_entry = """  <url>
    <loc>https://remake.beauty/products/lanolin-comedogenic-acne.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap = sitemap.replace('</urlset>', new_sitemap_entry)

with open('sitemap.xml', 'w') as f:
    f.write(sitemap)
print("sitemap.xml updated")

