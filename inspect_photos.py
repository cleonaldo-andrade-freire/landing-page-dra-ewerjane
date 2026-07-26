import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    line_no_b64 = re.sub(r'data:image[^\"'']+', 'DATA_URI', line)
    if 510 <= i <= 525 or 570 <= i <= 600:
        print(f'{i+1}: {line_no_b64}', end='')
