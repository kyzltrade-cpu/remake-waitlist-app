import os
import re
from datetime import datetime

# 1. Update index.html
index_path = "/tmp/remake-waitlist-app-seo/index.html"
with open(index_path, "r") as f:
    index_html = f.read()

new_link = '<div><a href="./products/isopropyl-isostearate-comedogenic.html" class="text-xs text-[#7C726E] hover:text-[#D98A96] transition-colors">Isopropyl Isostearate (Acne Safe?)</a></div>'
index_html = index_html.replace('</div>\n      </div>\n    </section>\n\n</body>', f'  {new_link}\n        </div>\n      </div>\n    </section>\n\n</body>')

with open(index_path, "w") as f:
    f.write(index_html)

# 2. Update sitemap.xml
sitemap_path = "/tmp/remake-waitlist-app-seo/sitemap.xml"
with open(sitemap_path, "r") as f:
    sitemap_xml = f.read()

today = datetime.now().strftime("%Y-%m-%d")
new_url = f'''  <url>
    <loc>https://remake.beauty/products/isopropyl-isostearate-comedogenic.html</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>'''

sitemap_xml = sitemap_xml.replace('</urlset>', new_url)

with open(sitemap_path, "w") as f:
    f.write(sitemap_xml)

print("Updated index.html and sitemap.xml")
