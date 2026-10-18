import datetime
import re

# Update sitemap.xml
with open("sitemap.xml", "r") as f:
    sitemap = f.read()

new_url = """  <url>
    <loc>https://remake.beauty/products/isopropyl-palmitate-comedogenic-acne.html</loc>
    <lastmod>{date}</lastmod>
    <priority>0.8</priority>
  </url>
</urlset>""".format(date=datetime.datetime.now().strftime("%Y-%m-%d"))

sitemap = sitemap.replace("</urlset>", new_url)

with open("sitemap.xml", "w") as f:
    f.write(sitemap)


# Update index.html
with open("index.html", "r") as f:
    index_html = f.read()

new_link = '          <li><a href="/products/isopropyl-palmitate-comedogenic-acne.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Isopropyl Palmitate Audit</a></li>\n          <li><a href="/products/yuka-app-vs-remake-app.html"'

index_html = index_html.replace('          <li><a href="/products/yuka-app-vs-remake-app.html"', new_link)

with open("index.html", "w") as f:
    f.write(index_html)
