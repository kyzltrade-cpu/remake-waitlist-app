import os

# Update sitemap.xml
sitemap_path = "/tmp/remake-waitlist-app-seo/sitemap.xml"
with open(sitemap_path, "r") as f:
    sitemap = f.read()

new_sitemap_entry = """  <url>
    <loc>https://remake.beauty/products/yuka-app-vs-remake-app.html</loc>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap = sitemap.replace("</urlset>", new_sitemap_entry)

with open(sitemap_path, "w") as f:
    f.write(sitemap)
print("Sitemap updated.")

# Update index.html
index_path = "/tmp/remake-waitlist-app-seo/index.html"
with open(index_path, "r") as f:
    index_html = f.read()

target_li = '<li><a href="/products/shea-butter-comedogenic-acne.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Shea Butter Audit</a></li>'
new_li = '<li><a href="/products/shea-butter-comedogenic-acne.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Shea Butter Audit</a></li>\n          <li><a href="/products/yuka-app-vs-remake-app.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Yuka App vs Remake</a></li>'

index_html = index_html.replace(target_li, new_li)

with open(index_path, "w") as f:
    f.write(index_html)
print("index.html updated.")

