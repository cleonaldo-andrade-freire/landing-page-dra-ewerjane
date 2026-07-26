import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remover 'endodontia'
content = content.replace('Especialista em Endodontia', 'Cirurgiã-Dentista / Periodontista')

# 2. Ajustar SEO
new_title = "<title>Dentista 24h em Aracaju | Emergência Odontológica | Dra. Ewerjane Ribeiro</title>"
new_desc = '<meta name="description" content="Dentista 24h em Aracaju. Dor de dente, dente quebrado e urgências? Atendimento particular imediato todos os dias, incluindo sábados, domingos e feriados. Chame a Dra. Ewerjane Ribeiro!" />'
new_kw = '<meta name="keywords" content="dentista 24h Aracaju, emergência odontológica Aracaju, dor de dente Aracaju, dentista urgência Aracaju, plantão odontológico Aracaju, dentista domingo Aracaju, clinica odontologica 24h, Dra Ewerjane Ribeiro, periodontista Aracaju" />'

content = re.sub(r'<title>.*?</title>', new_title, content, flags=re.IGNORECASE)
content = re.sub(r'<meta\s+name="description"\s+content=".*?"\s*/>', new_desc, content, flags=re.IGNORECASE)
content = re.sub(r'<meta\s+name="keywords"\s+content=".*?"\s*/>', new_kw, content, flags=re.IGNORECASE)

# 3. Remover a seção de "Continue seu tratamento aqui" (servicos)
content = re.sub(r'\s*<!--\s*SERVICES\s*-->\s*<section id="servicos">.*?</section>\s*(?=<!--\s*TESTIMONIALS\s*-->|<section id="depoimentos")', '\n\n  ', content, flags=re.DOTALL | re.IGNORECASE)
content = re.sub(r'\s*<section id="servicos">.*?</section>\s*(?=<!--\s*TESTIMONIALS\s*-->|<section id="depoimentos")', '\n\n  ', content, flags=re.DOTALL | re.IGNORECASE)

# 4. Remover a foto repetida
pattern_photo = r'<div class="[^"]*photo[^"]*">\s*<img[^>]+alt="Paciente satisfeita"[^>]*>\s*</div>\s*'
matches = list(re.finditer(pattern_photo, content))
if len(matches) > 1:
    match_to_remove = matches[1]
    content = content[:match_to_remove.start()] + content[match_to_remove.end():]
elif len(matches) == 1:
    content = re.sub(pattern_photo, '', content, count=1)

# 5. Remover o rodapé
content = re.sub(r'\s*<!--\s*FOOTER\s*-->\s*<footer class="footer">.*?</footer>\s*', '\n\n', content, flags=re.DOTALL | re.IGNORECASE)
content = re.sub(r'\s*<footer class="footer">.*?</footer>\s*', '\n\n', content, flags=re.DOTALL | re.IGNORECASE)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Modificações concluídas com sucesso!")
