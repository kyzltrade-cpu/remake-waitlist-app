import os

sitemap_path = "/tmp/remake-waitlist-app-seo/sitemap.xml"
with open(sitemap_path, "r") as f:
    sitemap = f.read()

new_url = """  <url>
    <loc>https://remake.beauty/products/cetyl-alcohol-comedogenic-acne.html</loc>
    <lastmod>2026-11-18</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>
</urlset>"""

if "</urlset>" in sitemap:
    sitemap = sitemap.replace("</urlset>", new_url)
    with open(sitemap_path, "w") as f:
        f.write(sitemap)
    print("Updated sitemap.xml")
else:
    print("Error: </urlset> not found")
