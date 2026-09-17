# Coleção DeepSeek

Cinco templates de currículo gerados numa conversa do DeepSeek a partir do [`master-prompt.md`](../master-prompt.md). Todos standalone (HTML + CSS), pensados para ATS, leitura humana e impressão A4.

## Templates

| # | Template | Layout | ATS | Destaque |
|---|---|---|---|---|
| 01 | [ATS / Corporate](template-01-ats/) | 1 coluna | excelente | sem ruído, parsing máximo |
| 02 | [Modern Professional](template-02-modern/) | sidebar + main | bom | equilíbrio estético/ATS |
| 03 | [Technical / Engineering](template-03-technical/) | 1 coluna densa | muito bom | timeline + chips mono |
| 04 | [Executive / Premium](template-04-executive/) | 1 coluna | bom | serifado, muito respiro |
| 05 | [Creative Tech](template-05-creative/) | header colorido | médio | grid + cards |

Galeria: [`index.html`](index.html).

## Conteúdo

Cada pasta tem `index.html`, `styles.css` e `index.json` (manifesto). O gerador original está preservado em [`gerar.py`](gerar.py) — ele reescreve os cinco templates num `templates-curriculo.zip` com um `index.html` seletor.

## Origem

Conversa compartilhada do DeepSeek (o `master-prompt.md` era o anexo `.txt` de 12KB daquela conversa). Os arquivos foram extraídos da conversa e normalizados para o padrão global desta pasta.
