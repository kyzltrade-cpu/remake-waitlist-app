import os
import re
from datetime import datetime

# 1. Update sitemap.xml
sitemap_path = '/tmp/remake-waitlist-app-seo/sitemap.xml'
with open(sitemap_path, 'r') as f:
    sitemap_content = f.read()

new_sitemap_entry = f"""  <url>
    <loc>https://remake.beauty/products/wheat-germ-oil-comedogenic-acne-safe.html</loc>
    <lastmod>2026-11-03</lastmod>
    <priority>0.8</priority>
  </url>
</urlset>"""

sitemap_content = sitemap_content.replace('</urlset>', new_sitemap_entry)

with open(sitemap_path, 'w') as f:
    f.write(sitemap_content)


# 2. Update index.html
index_path = '/tmp/remake-waitlist-app-seo/index.html'
with open(index_path, 'r') as f:
    index_content = f.read()

# We need to find the footer section with SEO links and append our new link.
# Usually there is a block like: <div class="grid grid-cols-2 md:grid-cols-4 gap-8"> or similar in the footer.
# Let's search for "Ingredient Audits" or just inject it before a specific closing tag in the footer.
# I will use regex to find the ingredient audits column.
