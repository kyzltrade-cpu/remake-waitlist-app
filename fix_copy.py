import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace all variations
content = content.replace("Download App", "Get REMAKE")
content = content.replace("Download on the App Store", "Get REMAKE")

with open('index.html', 'w') as f:
    f.write(content)
