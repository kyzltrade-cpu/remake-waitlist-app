import re

with open('index.html', 'r') as f:
    content = f.read()

# Web3forms submit handling removal
w3f = re.compile(r'function handleFormSubmit\(form\) \{.*?\n      }\);?\n\s*\}\n', re.DOTALL)
content = w3f.sub('', content)

# querySelector for waitlist
content = re.sub(r'document\.querySelectorAll\(\'\.waitlist-form.*?handleFormSubmit\);', '', content)

# variables
content = re.sub(r'const scanToWaitlist = document\.getElementById\(\'scanToWaitlist\'\);', '', content)

# Waitlist Modal Controls
modals = re.compile(r'// Waitlist Modal Controls.*?openWaitlistModal\(\);\s*\}\);', re.DOTALL)
content = modals.sub('', content)

# close modal on Escape
content = re.sub(r'closeWaitlistModalFn\(\);', '', content)

with open('index.html', 'w') as f:
    f.write(content)
