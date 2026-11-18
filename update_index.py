import os

index_path = "/tmp/remake-waitlist-app-seo/index.html"
with open(index_path, "r") as f:
    index = f.read()

target = '<li><a href="/products/ethylhexyl-palmitate-acne-safe.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Ethylhexyl Palmitate Audit</a></li>'
replacement = target + '\n          <li><a href="/products/cetyl-alcohol-comedogenic-acne.html" class="hover:underline hover:text-[#2A2421] transition decoration-[#E8A0AA]">Cetyl Alcohol Audit</a></li>'

if target in index:
    index = index.replace(target, replacement)
    with open(index_path, "w") as f:
        f.write(index)
    print("Updated index.html")
else:
    print("Target not found")