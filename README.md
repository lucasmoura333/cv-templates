# Templates de Currículo

Embrião do repositório de criação de templates de currículo profissional. Segue o **mesmo padrão** de [`proposal-templates`](../../../gdpro-agent/proposal-templates/README.md): raiz com galeria, cada template numa pasta autocontida e um contrato de dados estável.

O documento-fonte do sistema é [`master-prompt.md`](master-prompt.md).

## Estrutura

```
templates/
├── README.md                 # este arquivo (padrão global)
├── index.html                # catálogo global (todas as coleções)
├── master-prompt.md          # prompt-mestre que rege a criação dos templates
├── <coleção>/                # deepseek | openia (…)
│   ├── README.md
│   ├── index.html            # galeria da coleção
│   └── template-NN-slug/
│       ├── index.html        # template (HTML, sem CSS inline)
│       ├── styles.css        # estilos do template
│       ├── index.json        # manifesto (metadados + contrato)
│       └── preview.pdf       # opcional (render A4)
└── v0/                       # app Next.js interativo (fora do padrão estático)
```

## Padrão de um template

1. **Autocontido** — abre `index.html` direto no navegador; único CSS externo é `styles.css` ao lado.
2. **A4** — todo `styles.css` define `@page { size: A4 }` e regras de `break-inside: avoid` para títulos/bullets/seções não quebrarem.
3. **Impressão** — `Ctrl+P` → A4 → margens **Nenhuma** → escala **100%** → marcar **gráficos de segundo plano**.
4. **Sem build** — HTML + CSS puros. Coleções interativas (ex.: `v0`) ficam fora deste contrato.
5. **Manifesto** — `index.json` descreve o template (ver abaixo).

## Manifesto (`index.json`)

```jsonc
{
  "template_id": "deepseek/template-01-ats",
  "collection": "deepseek",
  "version": 1,
  "name": "ATS / Corporate",
  "description": "…",
  "tags": ["ats", "1-coluna", "corporativo"],
  "page": { "size": "A4", "margin": "0" },
  "fonts": ["Inter"],
  "accent": "#1a3a5c",
  "features": { "columns": 1, "ats_safe": true, "page_break_rules": true, "standalone": true },
  "files": { "html": "index.html", "css": "styles.css", "preview": null },
  "data_contract": { "attributes": { "field": "data-field", "repeat": "data-repeat", "editable": "data-editable" }, "…": "…" }
}
```

## Contrato de dados

Mesmo espírito dos `data-field` / `data-repeat` / `data-editable` das propostas: o conteúdo é substituível sem tocar no layout.

| Atributo | Uso |
|---|---|
| `data-field="cv.name"` | valor escalar substituível |
| `data-repeat="experience"` | bloco repetível (um por item) |
| `data-editable="true"` | região editável em runtime |

Campos canônicos: `cv.name`, `cv.role`, `cv.location`, `cv.email`, `cv.phone`, `cv.github`, `cv.linkedin`, `cv.summary`, e as listas `experience`, `projects`, `education`, `languages`, `skills`.

> Estágio atual: contrato **documentado**; a marcação `data-*` será aplicada incrementalmente nos templates. O `deepseek/template-01-ats` é a referência de implementação.

## Coleções

| Coleção | Templates | Formato | Origem |
|---|---|---|---|
| [`deepseek/`](deepseek/) | 5 (ATS, Modern, Technical, Executive, Creative) | HTML/CSS estático | conversa DeepSeek + `gerar.py` |
| [`openia/`](openia/) | 5 (ATS Corporate, Modern Editorial, Technical Dense, Executive Premium, Creative Tech) | HTML/CSS estático | conjunto OpenIA |
| [`v0/`](v0/) | showcase interativo | Next.js + React + Tailwind | protótipo experimental |

## Impressão

Cada template já define `@page { size: A4; margin: 0 }` e regras que evitam quebras ruins (títulos órfãos, bullets partidos, seções cortadas). Para PDF: abra o `index.html` do template e use **Imprimir → Salvar como PDF**, papel A4, margens **Nenhuma**, escala **100%**, gráficos de segundo plano **ativados**.

## Como adicionar um template

1. Crie `templates/<coleção>/template-NN-slug/`.
2. Adicione `index.html` + `styles.css` (CSS fora do HTML) e, se quiser, `preview.pdf`.
3. Adicione `index.json` seguindo o manifesto acima.
4. Rode/abra a galeria da coleção — ela referencia os templates por pasta.

## Origem e atribuição

Este material foi **gerado com apoio de IA (DeepSeek)** a partir do [`master-prompt.md`](master-prompt.md) e depois normalizado manualmente para o padrão descrito acima. Os prompts-mestres e os layouts resultantes estão versionados aqui para preservar a rastreabilidade de como cada template foi produzido.

Repositório **privado**, compartilhado apenas com recrutadores. Todo o conteúdo dos templates é **fictício/mock** (nomes, empresas, métricas e links de exemplo) e deve ser substituído pelos dados reais antes de qualquer uso.

## Licença

Uso livre. Todo o conteúdo dos templates é **fictício/mock** e deve ser substituído pelos dados reais.
