# v0 — showcase interativo

Protótipo **interativo** de currículos (Next.js 16 + React 19 + Tailwind 4 + shadcn/Base UI). É a versão "app" da coleção: uma vitrine com abas para alternar entre os cinco estilos (Aline/ATS, Nexo/Modern, Stack/Technical, Miro/Executive, Orbit/Creative), prévia ao vivo em A4 e botão de exportar/print.

> Diferente de `deepseek/` e `openia/`, **não segue o padrão estático** (HTML+CSS+`index.json`). Fica aqui como referência de exploração e possível destino da camada interativa do repositório.

## Rodar

```bash
pnpm install
pnpm dev
```

Abra http://localhost:3000.

## Estrutura

- `app/page.tsx` — página/entrypoint.
- `components/resume-showcase.tsx` — componente principal: catálogo + os 5 layouts em React.
- `app/globals.css` — estilos (Tailwind 4).

## Relação com as outras coleções

Os cinco estilos correspondem em espírito aos templates A–E de [`../deepseek/`](../deepseek/) e 01–05 de [`../openia/`](../openia/), mas reescritos como componentes React com dados mock em TypeScript.
