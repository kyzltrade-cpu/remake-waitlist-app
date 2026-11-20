import re
from datetime import datetime

# 1. Update sitemap.xml
sitemap_path = "sitemap.xml"
with open(sitemap_path, "r") as f:
    sitemap_content = f.read()

new_sitemap_entry = f"""
  <url>
    <loc>https://remake.beauty/products/isostearyl-isostearate-comedogenic-acne.html</loc>
    <lastmod>{datetime.now().strftime("%Y-%m-%d")}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap_content = sitemap_content.replace("</urlset>", new_sitemap_entry.strip() + "\n</urlset>")
with open(sitemap_path, "w") as f:
    f.write(sitemap_content)
print("Updated sitemap.xml")

# 2. Update index.html
index_path = "index.html"
with open(index_path, "r") as f:
    index_content = f.read()

new_footer_link = '<li><a href="/products/isostearyl-isostearate-comedogenic-acne.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Isostearyl Isostearate Audit</a></li>\n          <li><a href="/products/ethylhexyl-palmitate-acne-safe.html"'

index_content = index_content.replace('<li><a href="/products/ethylhexyl-palmitate-acne-safe.html"', new_footer_link)

with open(index_path, "w") as f:
    f.write(index_content)
print("Updated index.html")
