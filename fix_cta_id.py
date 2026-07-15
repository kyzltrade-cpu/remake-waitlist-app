import re

with open('index.html', 'r') as f:
    content = f.read()

# Fix hero button
content = content.replace(
    '<a href="#" class="btn-primary w-full sm:w-auto text-center px-8 py-3.5">',
    '<a href="#" class="btn-primary w-full sm:w-auto text-center">'
)

# Fix bottom CTA button
content = content.replace(
    '<a href="#" class="btn-primary w-full text-center px-8 py-4 bg-white text-[#2A2421] border-white hover:bg-pink-100 hover:text-[#2A2421]">',
    '<a href="#" class="btn-primary w-full text-center bg-white text-[#2A2421] border-white hover:bg-pink-100 hover:text-[#2A2421]">'
)

# Fix middle CTA button
content = content.replace(
    '<a href="#" class="btn-primary w-full text-center py-3 block">Download App</a>',
    '<a href="#" class="btn-primary w-full text-center block">Download App</a>'
)

# Add header-cta ID back
content = content.replace(
    '<a href="#" class="btn-primary px-3.5 py-1.5 text-[9px] md:px-5 md:py-2 md:text-[10.5px]">Download App</a>',
    '<a href="#" id="header-cta" class="btn-primary px-3.5 py-1.5 text-[9px] md:px-5 md:py-2 md:text-[10.5px]">Download App</a>'
)

with open('index.html', 'w') as f:
    f.write(content)
