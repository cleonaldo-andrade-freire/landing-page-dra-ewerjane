import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

for match in re.finditer(r'<img src=\"(data:image[^\"]+)\" alt=\"([^\"]+)\"', content):
    b64 = match.group(1)
    alt = match.group(2)
    print(f'Alt: {alt} - Start: {b64[:40]}... End: {b64[-40:]} - Len: {len(b64)}')
