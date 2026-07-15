import re

with open('index.html', 'r') as f:
    content = f.read()

# Web3Forms Submit Handling (Extremely Robust)
w3f = re.compile(r'// Web3Forms Submit Handling.*?btnText\.innerHTML = originalHTML;\n\s*}\n\s*}\);\n\s*};\n', re.DOTALL)
content = w3f.sub('', content)

with open('index.html', 'w') as f:
    f.write(content)
