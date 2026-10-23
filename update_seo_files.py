import re
from datetime import datetime

slug = "ceteareth-20-comedogenic-acne-safe"
url = f"https://remake.beauty/products/{slug}.html"
today = datetime.now().strftime("%Y-%m-%d")

# 1. Update sitemap.xml
with open("/tmp/remake-waitlist-app-seo/sitemap.xml", "r") as f:
    sitemap = f.read()

new_sitemap_entry = f"""  <url>
    <loc>{url}</loc>
    <lastmod>{today}</lastmod>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap = sitemap.replace("</urlset>", new_sitemap_entry)

with open("/tmp/remake-waitlist-app-seo/sitemap.xml", "w") as f:
    f.write(sitemap)

# 2. Update index.html footer
link_html = f'<div><a href="./products/{slug}.html" class="text-xs text-[#7C726E] hover:text-[#D98A96] transition-colors">Ceteareth-20 (Acne Safe?)</a></div>'

with open("/tmp/remake-waitlist-app-seo/index.html", "r") as f:
    index_html = f.read()

# find the last internal link div and insert this before the closing tag of the flex container
pattern = r'(<div><a href="\./products/.*?</div>)'
matches = list(re.finditer(pattern, index_html))
if matches:
    last_match = matches[-1]
    insert_pos = last_match.end()
    index_html = index_html[:insert_pos] + link_html + index_html[insert_pos:]
    with open("/tmp/remake-waitlist-app-seo/index.html", "w") as f:
        f.write(index_html)
    print("Added to index.html")
else:
    print("Could not find insertion point in index.html")
