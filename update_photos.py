import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update "Sobre a doutora"
about_repl = '''        <div class="about-photos fade-up" style="display: flex; align-items: center; justify-content: center;">
          <div class="about-photo-main" style="height: auto; width: 100%;">
            <img src="img/foto_doutora_instrumentos.jpg" alt="Dra. Ewerjane Ribeiro" style="width: 100%; border-radius: var(--radius-lg); object-fit: cover;" />
          </div>
        </div>'''
content = re.sub(r'<div class="about-photos fade-up">.*?</div>\s*(?=<div class="about-content fade-up">)', about_repl + '\n        ', content, flags=re.DOTALL)

lines = content.split('\n')
in_action = False
action_photo_count = 0
for i in range(len(lines)):
    if '<div class="action-photos fade-up">' in lines[i]:
        in_action = True
    if in_action and '<img src=' in lines[i]:
        action_photo_count += 1
        if action_photo_count == 3:
            lines[i] = '            <img src="img/foto_menino_dente.jpg" alt="Menino com dente na mão" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;" />'
        elif action_photo_count == 4:
            lines[i] = '            <img src="img/foto_paciente_sorrindo.jpg" alt="Dra Ewerjane e paciente" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;" />'

content = '\n'.join(lines)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Imagens atualizadas com placeholders.")
