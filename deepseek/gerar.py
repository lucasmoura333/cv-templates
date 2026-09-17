#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gera templates-curriculo.zip com 5 templates de currículo separados,
um index.html com seletor e um README.md.
Rodar: python gerar.py
"""
import pathlib, zipfile

ROOT = pathlib.Path("templates-curriculo")
ROOT.mkdir(exist_ok=True)
FILES = {}

# ============================================================
# TEMPLATE A — ATS / CORPORATE
# ============================================================
FILES["template-a-ats.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucas Andrade — ATS</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,"Source Sans 3",Arial,sans-serif;font-size:10.5pt;color:#1a1a1a;background:#f5f5f5;padding:20px 0;display:flex;justify-content:center;line-height:1.35}
.r{width:210mm;min-height:297mm;background:#fff;padding:18mm 20mm;box-shadow:0 2px 12px rgba(0,0,0,.12)}
h1{font-size:22pt;font-weight:700;letter-spacing:-.02em;line-height:1.15}
.role{font-size:12pt;color:#1a3a5c;font-weight:500;margin:2pt 0 4pt}
.contact{font-size:9pt;color:#444;margin-bottom:14pt;padding-bottom:8pt;border-bottom:1.5pt solid #1a3a5c;line-height:1.5}
.contact a{color:#444;text-decoration:none;border-bottom:.5pt solid #ccc}
h2{font-size:11pt;text-transform:uppercase;letter-spacing:.08em;color:#1a3a5c;border-bottom:.75pt solid #ccc;padding-bottom:2pt;margin:14pt 0 8pt;font-weight:700}
.j{margin-bottom:8pt}
.jh{display:flex;justify-content:space-between;gap:4pt;flex-wrap:wrap}
.co{font-weight:700;font-size:10.5pt}
.pe{font-size:9pt;color:#666;white-space:nowrap}
.ro{font-size:10pt;color:#1a3a5c;font-weight:500;margin:1pt 0}
.lo{font-size:9pt;color:#666;margin-bottom:4pt}
ul{list-style:disc;padding-left:16pt;font-size:10pt;line-height:1.5}
ul li{margin-bottom:2pt}
ul li::marker{color:#1a3a5c}
.sum{font-size:10pt;line-height:1.5}
.sk{font-size:10pt;margin-bottom:3pt;line-height:1.4}
.sk b{display:inline-block;min-width:130pt}
.sk span{color:#444}
.pj{margin-bottom:8pt}
.pjh{display:flex;justify-content:space-between;gap:4pt;flex-wrap:wrap}
.pjn{font-weight:700;font-size:10pt}
.pjl{font-size:9pt;color:#666}
.pjl a{color:#666;text-decoration:none}
.pjd{font-size:10pt;line-height:1.5;margin:2pt 0}
.pjt{font-size:9pt;color:#666;font-style:italic}
.edu{margin-bottom:8pt}
.eduh{display:flex;justify-content:space-between;gap:4pt;flex-wrap:wrap}
.educ{font-weight:700;font-size:10pt}
.edup{font-size:9pt;color:#666}
.edui{font-size:10pt;color:#444}
.cert{list-style:none;font-size:10pt;line-height:1.5}
.cert li{padding-left:12pt;position:relative;margin-bottom:2pt}
.cert li::before{content:"\2022";position:absolute;left:0;color:#1a3a5c;font-weight:700}
.langs{display:flex;flex-wrap:wrap;gap:8pt;font-size:10pt}
.langs b{font-weight:600}
@page{size:A4;margin:0}
@media print{body{background:none;padding:0;display:block}.r{width:100%;min-height:auto;box-shadow:none}a{color:inherit;text-decoration:none;border:none!important}h2{page-break-after:avoid}.j,.pj,.edu{page-break-inside:avoid}}
@media screen and (max-width:820px){body{padding:0}.r{width:100%;padding:20px}.jh,.pjh,.eduh{flex-direction:column;gap:2px}.sk b{display:block;min-width:auto}}
</style></head><body><main class="r">
<h1>Lucas Andrade</h1>
<p class="role">Full Stack Software Engineer</p>
<p class="contact">São Paulo, SP — Brasil &nbsp;|&nbsp; <a href="mailto:email@example.com">email@example.com</a> &nbsp;|&nbsp; <a href="https://github.com/example">github.com/example</a> &nbsp;|&nbsp; <a href="https://linkedin.com/in/example">linkedin.com/in/example</a></p>
<h2>Resumo Profissional</h2>
<p class="sum">Engenheiro de software full stack com 7+ anos de experiência construindo sistemas distribuídos e aplicações web de alta escala. Especializado em TypeScript, Node.js e React, com histórico comprovado na redução de latência, otimização de pipelines de dados e liderança técnica de equipes multidisciplinares. Foco em arquitetura limpa, observabilidade e entrega contínua.</p>
<h2>Experiência Profissional</h2>
<div class="j"><div class="jh"><span class="co">TechNova Solutions</span><span class="pe">Mar 2022 — Presente</span></div><p class="ro">Senior Full Stack Engineer</p><p class="lo">São Paulo, SP — Remoto</p><ul>
<li>Redesenhou o pipeline de processamento de documentos usando workers assíncronos e Redis, reduzindo o tempo médio em 42%.</li>
<li>Liderou a migração de monolito Laravel para microsserviços em Node.js + NestJS, melhorando a escalabilidade em 3×.</li>
<li>Implementou observabilidade com OpenTelemetry e Grafana, reduzindo o MTTR de 45 para 12 minutos.</li>
<li>Mentorou 4 engenheiros júniores em boas práticas de código, testes e design de APIs REST.</li>
</ul></div>
<div class="j"><div class="jh"><span class="co">DataFlow Systems</span><span class="pe">Jan 2020 — Fev 2022</span></div><p class="ro">Full Stack Developer</p><p class="lo">São Paulo, SP — Híbrido</p><ul>
<li>Desenvolveu dashboard analítico em React + Next.js consumindo APIs GraphQL, usado por 200+ clientes corporativos.</li>
<li>Otimizou consultas PostgreSQL com índices compostos, reduzindo tempo de resposta em 65%.</li>
<li>Automatizou pipelines de CI/CD com GitHub Actions e Docker, reduzindo o deploy de 25 para 6 minutos.</li>
</ul></div>
<div class="j"><div class="jh"><span class="co">StartupLab</span><span class="pe">Jun 2018 — Dez 2019</span></div><p class="ro">Backend Developer</p><p class="lo">Campinas, SP — Presencial</p><ul>
<li>Construiu APIs REST em Python (FastAPI) processando 50k+ transações diárias.</li>
<li>Implementou filas com RabbitMQ para relatórios assíncronos, eliminando timeouts em pico.</li>
<li>Escreveu testes com cobertura de 85%, reduzindo bugs em produção em 40%.</li>
</ul></div>
<h2>Competências Técnicas</h2>
<p class="sk"><b>Languages</b><span>TypeScript · JavaScript · Python · Java · SQL</span></p>
<p class="sk"><b>Backend</b><span>Node.js · NestJS · FastAPI · Laravel · REST APIs · GraphQL</span></p>
<p class="sk"><b>Frontend</b><span>React · Next.js · HTML · CSS · Tailwind CSS</span></p>
<p class="sk"><b>Data</b><span>PostgreSQL · MySQL · Redis · MongoDB · RabbitMQ</span></p>
<p class="sk"><b>Infrastructure</b><span>Docker · AWS · CI/CD · GitHub Actions · OpenTelemetry</span></p>
<h2>Projetos Relevantes</h2>
<div class="pj"><div class="pjh"><span class="pjn">OpenMetrics Dashboard</span><span class="pjl"><a href="https://github.com/example/openmetrics">github.com/example/openmetrics</a></span></div><p class="pjd">Dashboard open-source para visualização de métricas em tempo real, com múltiplas fontes e alertas configuráveis. Usado por 500+ desenvolvedores.</p><p class="pjt">TypeScript · React · Node.js · WebSocket · PostgreSQL</p></div>
<div class="pj"><div class="pjh"><span class="pjn">FastQueue</span><span class="pjl"><a href="https://github.com/example/fastqueue">github.com/example/fastqueue</a></span></div><p class="pjd">Biblioteca leve de gerenciamento de filas para Node.js com suporte a Redis e RabbitMQ.</p><p class="pjt">Node.js · TypeScript · Redis · RabbitMQ</p></div>
<h2>Formação Acadêmica</h2>
<div class="edu"><div class="eduh"><span class="educ">Bacharelado em Ciência da Computação</span><span class="edup">2014 — 2018</span></div><p class="edui">Universidade Estadual de Campinas (UNICAMP)</p></div>
<div class="edu"><div class="eduh"><span class="educ">Especialização em Arquitetura de Software</span><span class="edup">2019 — 2020</span></div><p class="edui">Instituto Tecnológico de Aeronáutica (ITA)</p></div>
<h2>Certificações</h2>
<ul class="cert"><li>AWS Certified Solutions Architect — Associate (2023)</li><li>Node.js Application Development — OpenJS Foundation (2022)</li><li>Scrum Master Certified — Scrum Alliance (2021)</li></ul>
<h2>Idiomas</h2>
<div class="langs"><span><b>Português</b> — Nativo</span><span><b>Inglês</b> — Avançado (C1)</span><span><b>Espanhol</b> — Intermediário (B1)</span></div>
</main></body></html>"""

# ============================================================
# TEMPLATE B — MODERN PROFESSIONAL
# ============================================================
FILES["template-b-modern.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucas Andrade — Modern</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;font-size:10.5pt;color:#111827;background:#eef1f5;line-height:1.45;display:flex;justify-content:center;padding:20px 0}
.r{width:210mm;min-height:297mm;background:#fff;display:grid;grid-template-columns:68mm 1fr;box-shadow:0 2px 14px rgba(0,0,0,.12)}
.side{background:#f8fafc;padding:18mm 8mm 18mm 10mm;border-right:1px solid #e5e7eb}
.nm{font-size:19pt;font-weight:800;letter-spacing:-.02em;line-height:1.05}
.rl{font-size:10.5pt;font-weight:600;color:#0f766e;margin-top:4pt;line-height:1.25}
.bk{margin-top:14pt}
.bt{font-size:8.5pt;font-weight:700;text-transform:uppercase;letter-spacing:.12em;color:#0f766e;margin-bottom:6pt}
.sl{list-style:none}
.sl li{font-size:9.5pt;color:#374151;margin-bottom:3pt;word-break:break-word;line-height:1.4}
.sl a{color:#374151;text-decoration:none;border-bottom:.5pt solid #e5e7eb}
.skl{font-weight:600;font-size:9.5pt;display:block;margin-top:6pt}
.ski{font-size:9.5pt;color:#6b7280;line-height:1.4}
.main{padding:18mm 14mm 18mm 12mm}
.ms{margin-bottom:13pt}
.mt{font-size:10.5pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#0f766e;padding-bottom:4pt;border-bottom:2pt solid #ccfbf1;margin-bottom:8pt}
.sum{font-size:10pt;line-height:1.55;color:#374151}
.job{margin-bottom:11pt}
.jh{display:flex;justify-content:space-between;gap:6pt;flex-wrap:wrap}
.co{font-weight:700;font-size:10.5pt}
.pe{font-size:9pt;color:#6b7280;white-space:nowrap}
.ro{font-size:10pt;font-weight:600;color:#0f766e;margin-top:1pt}
.lo{font-size:9pt;color:#6b7280;margin-top:1pt}
ul.bl{list-style:none;margin-top:5pt;padding-left:12pt}
ul.bl li{font-size:9.8pt;color:#374151;margin-bottom:3pt;position:relative;line-height:1.45}
ul.bl li::before{content:"";position:absolute;left:-11pt;top:6pt;width:4pt;height:4pt;background:#0f766e;border-radius:50%}
.pj{margin-bottom:9pt}
.pjn{font-weight:700;font-size:10pt}
.pjl{font-size:9pt;color:#6b7280;margin-left:6pt}
.pjl a{color:#6b7280;text-decoration:none;border-bottom:.5pt solid #e5e7eb}
.pjd{font-size:9.8pt;color:#374151;margin-top:2pt;line-height:1.45}
.pjt{font-size:8.8pt;color:#0f766e;font-weight:600;margin-top:2pt}
.edu{margin-bottom:8pt}
.educ{font-weight:700;font-size:10pt}
.edui{font-size:9.8pt;color:#374151}
.edup{font-size:9pt;color:#6b7280}
@page{size:A4;margin:0}
@media print{body{background:none;padding:0;display:block}.r{width:100%;min-height:auto;box-shadow:none}a{color:inherit;text-decoration:none;border:none!important}.mt{page-break-after:avoid}.job,.pj,.edu{page-break-inside:avoid}}
@media screen and (max-width:820px){body{padding:0}.r{width:100%;min-height:auto;grid-template-columns:1fr}.side{border-right:none;border-bottom:1px solid #e5e7eb;padding:22px 20px}.main{padding:20px}.jh{flex-direction:column;gap:2px}.pe{white-space:normal}}
</style></head><body><main class="r">
<aside class="side">
<h1 class="nm">Lucas<br>Andrade</h1>
<p class="rl">Full Stack<br>Software Engineer</p>
<div class="bk"><h2 class="bt">Contato</h2><ul class="sl">
<li>São Paulo, SP — Brasil</li>
<li><a href="mailto:email@example.com">email@example.com</a></li>
<li><a href="https://github.com/example">github.com/example</a></li>
<li><a href="https://linkedin.com/in/example">linkedin.com/in/example</a></li>
</ul></div>
<div class="bk"><h2 class="bt">Competências</h2>
<span class="skl">Languages</span><p class="ski">TypeScript · JavaScript · Python · Java · SQL</p>
<span class="skl">Backend</span><p class="ski">Node.js · NestJS · FastAPI · Laravel · GraphQL</p>
<span class="skl">Frontend</span><p class="ski">React · Next.js · HTML · CSS · Tailwind</p>
<span class="skl">Data</span><p class="ski">PostgreSQL · MySQL · Redis · MongoDB</p>
<span class="skl">Infrastructure</span><p class="ski">Docker · AWS · CI/CD · OpenTelemetry</p>
</div>
<div class="bk"><h2 class="bt">Idiomas</h2><ul class="sl">
<li>Português — Nativo</li><li>Inglês — Avançado (C1)</li><li>Espanhol — Intermediário (B1)</li>
</ul></div>
<div class="bk"><h2 class="bt">Certificações</h2><ul class="sl">
<li>AWS Solutions Architect — Associate (2023)</li>
<li>Node.js App Development — OpenJS (2022)</li>
</ul></div>
</aside>
<section class="main">
<section class="ms"><h2 class="mt">Resumo</h2><p class="sum">Engenheiro full stack com 7+ anos de experiência em sistemas distribuídos e aplicações web de alta escala. Especializado em TypeScript, Node.js e React, com histórico de redução de latência, otimização de pipelines e liderança técnica. Foco em arquitetura limpa, observabilidade e entrega contínua.</p></section>
<section class="ms"><h2 class="mt">Experiência</h2>
<article class="job"><div class="jh"><span class="co">TechNova Solutions</span><span class="pe">Mar 2022 — Presente</span></div><p class="ro">Senior Full Stack Engineer</p><p class="lo">São Paulo, SP — Remoto</p><ul class="bl">
<li>Redesenhou pipeline de documentos com workers assíncronos e Redis, reduzindo tempo médio em 42%.</li>
<li>Liderou migração de monolito Laravel para microsserviços Node.js + NestJS, escalando 3×.</li>
<li>Implementou observabilidade com OpenTelemetry e Grafana, reduzindo MTTR de 45 para 12 min.</li>
<li>Mentorou 4 engenheiros júniores em testes automatizados e design de APIs REST.</li>
</ul></article>
<article class="job"><div class="jh"><span class="co">DataFlow Systems</span><span class="pe">Jan 2020 — Fev 2022</span></div><p class="ro">Full Stack Developer</p><p class="lo">São Paulo, SP — Híbrido</p><ul class="bl">
<li>Desenvolveu dashboard analítico em React + Next.js consumindo GraphQL para 200+ clientes.</li>
<li>Otimizou consultas PostgreSQL com índices compostos, reduzindo tempo de resposta em 65%.</li>
<li>Automatizou CI/CD com GitHub Actions e Docker, reduzindo deploy de 25 para 6 min.</li>
</ul></article>
<article class="job"><div class="jh"><span class="co">StartupLab</span><span class="pe">Jun 2018 — Dez 2019</span></div><p class="ro">Backend Developer</p><p class="lo">Campinas, SP — Presencial</p><ul class="bl">
<li>Construiu APIs REST em FastAPI processando 50k+ transações diárias.</li>
<li>Implementou filas RabbitMQ para relatórios assíncronos, eliminando timeouts em pico.</li>
<li>Elevou cobertura de testes para 85%, reduzindo bugs em produção em 40%.</li>
</ul></article>
</section>
<section class="ms"><h2 class="mt">Projetos</h2>
<article class="pj"><span class="pjn">OpenMetrics Dashboard</span><span class="pjl"><a href="https://github.com/example/openmetrics">github.com/example/openmetrics</a></span><p class="pjd">Dashboard open-source para métricas em tempo real, com múltiplas fontes e alertas configuráveis. 500+ devs ativos.</p><p class="pjt">TypeScript · React · Node.js · WebSocket · PostgreSQL</p></article>
<article class="pj"><span class="pjn">FastQueue</span><span class="pjl"><a href="https://github.com/example/fastqueue">github.com/example/fastqueue</a></span><p class="pjd">Biblioteca leve de filas para Node.js com suporte a Redis e RabbitMQ.</p><p class="pjt">Node.js · TypeScript · Redis · RabbitMQ</p></article>
</section>
<section class="ms"><h2 class="mt">Formação</h2>
<article class="edu"><p class="educ">Bacharelado em Ciência da Computação</p><p class="edui">Universidade Estadual de Campinas (UNICAMP)</p><p class="edup">2014 — 2018</p></article>
<article class="edu"><p class="educ">Especialização em Arquitetura de Software</p><p class="edui">Instituto Tecnológico de Aeronáutica (ITA)</p><p class="edup">2019 — 2020</p></article>
</section>
</section>
</main></body></html>"""

# ============================================================
# TEMPLATE C — TECHNICAL / ENGINEERING
# ============================================================
FILES["template-c-technical.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucas Andrade — Technical</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:"IBM Plex Sans",Inter,Arial,sans-serif;font-size:10pt;color:#0b1220;background:#e8ecf1;line-height:1.4;display:flex;justify-content:center;padding:20px 0}
.r{width:210mm;min-height:297mm;background:#fff;padding:16mm;box-shadow:0 2px 14px rgba(0,0,0,.12)}
.mono{font-family:"IBM Plex Mono","JetBrains Mono",Consolas,monospace}
.hd{border-bottom:2pt solid #0b1220;padding-bottom:8pt;margin-bottom:10pt}
.hdtop{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:8pt}
h1{font-size:20pt;font-weight:700;letter-spacing:-.02em;line-height:1}
.rl{font-size:10pt;color:#2563eb;font-weight:600}
.meta{font-size:8.8pt;color:#64748b;margin-top:6pt;display:flex;flex-wrap:wrap;gap:6pt 14pt}
.meta a{color:#64748b;text-decoration:none;border-bottom:.5pt solid #e2e8f0}
h2{font-size:9pt;font-weight:700;text-transform:uppercase;letter-spacing:.14em;color:#0b1220;margin:10pt 0 6pt;display:flex;align-items:center;gap:6pt}
h2::before{content:"##";color:#2563eb}
h2::after{content:"";flex:1;height:1px;background:#e2e8f0}
.sum{font-size:9.8pt;line-height:1.55;color:#334155}
.tl{border-left:1.5pt solid #e2e8f0;padding-left:12pt;margin-left:2pt}
.tli{position:relative;padding-bottom:10pt}
.tli::before{content:"";position:absolute;left:-17pt;top:4pt;width:7pt;height:7pt;background:#fff;border:1.5pt solid #2563eb;border-radius:50%}
.tlh{display:flex;justify-content:space-between;gap:8pt;flex-wrap:wrap}
.tlr{font-weight:700;font-size:10.2pt}
.tlp{font-size:8.8pt;color:#64748b;white-space:nowrap}
.tlc{font-size:9.8pt;color:#2563eb;font-weight:600;margin-top:1pt}
.tll{font-size:8.5pt;color:#64748b;margin-top:1pt}
ul.bl{list-style:none;margin-top:4pt}
ul.bl li{font-size:9.6pt;color:#334155;margin-bottom:2.5pt;padding-left:11pt;position:relative;line-height:1.45}
ul.bl li::before{content:"\25B8";position:absolute;left:0;color:#2563eb;font-weight:700}
.sk{display:grid;grid-template-columns:auto 1fr;gap:5pt 10pt;font-size:9.5pt;align-items:baseline}
.skl{font-weight:700;white-space:nowrap}
.ski{color:#334155;line-height:1.5}
.chip{display:inline-block;background:#f1f5f9;border:1px solid #e2e8f0;padding:1pt 5pt;border-radius:3pt;font-size:8.5pt;color:#334155;margin:0 2pt 2pt 0}
.pj{margin-bottom:8pt}
.pjh{display:flex;justify-content:space-between;gap:8pt;flex-wrap:wrap}
.pjn{font-weight:700;font-size:9.8pt}
.pjl{font-size:8.5pt;color:#64748b}
.pjl a{color:#64748b;text-decoration:none;border-bottom:.5pt solid #e2e8f0}
.pjd{font-size:9.5pt;color:#334155;margin-top:2pt;line-height:1.45}
.pjt{font-size:8.5pt;color:#2563eb;margin-top:2pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10pt}
.ed{margin-bottom:5pt}
.edc{font-weight:700;font-size:9.8pt}
.edi{font-size:9.5pt;color:#334155}
.edp{font-size:8.5pt;color:#64748b}
.lg{font-size:9.5pt;color:#334155;margin-bottom:3pt}
.lg b{color:#0b1220}
@page{size:A4;margin:0}
@media print{body{background:none;padding:0;display:block}.r{width:100%;min-height:auto;box-shadow:none}a{color:inherit;text-decoration:none;border:none!important}h2{page-break-after:avoid}.tli,.pj{page-break-inside:avoid}}
@media screen and (max-width:820px){body{padding:0}.r{width:100%;padding:20px}.two{grid-template-columns:1fr;gap:10pt}.sk{grid-template-columns:1fr;gap:2pt}.skl{margin-top:4pt}.tlh{flex-direction:column;gap:2px}.tlp{white-space:normal}}
</style></head><body><main class="r">
<header class="hd">
<div class="hdtop"><h1>Lucas Andrade</h1><span class="rl mono">Full Stack Software Engineer</span></div>
<div class="meta mono">
<span>São Paulo, SP — Brasil</span>
<span><a href="mailto:email@example.com">email@example.com</a></span>
<span><a href="https://github.com/example">github.com/example</a></span>
<span><a href="https://linkedin.com/in/example">linkedin.com/in/example</a></span>
</div></header>
<h2>Resumo</h2>
<p class="sum">Engenheiro full stack com 7+ anos em sistemas distribuídos e aplicações web de alta escala. Especializado em TypeScript, Node.js e React, com foco em arquitetura limpa, observabilidade e entrega contínua. Histórico de redução de latência e liderança técnica.</p>
<h2>Experiência</h2>
<div class="tl">
<article class="tli"><div class="tlh"><span class="tlr">Senior Full Stack Engineer</span><span class="tlp mono">2022-03 → presente</span></div><p class="tlc">TechNova Solutions</p><p class="tll mono">São Paulo, SP — remoto</p><ul class="bl">
<li>Pipeline de documentos com workers assíncronos e Redis — 42% menos tempo médio.</li>
<li>Migração monolito Laravel → microsserviços Node.js + NestJS — 3× de escala.</li>
<li>Observabilidade com OpenTelemetry + Grafana — MTTR 45 → 12 min.</li>
<li>Mentoria de 4 engenheiros júniores em testes e design de APIs REST.</li>
</ul></article>
<article class="tli"><div class="tlh"><span class="tlr">Full Stack Developer</span><span class="tlp mono">2020-01 → 2022-02</span></div><p class="tlc">DataFlow Systems</p><p class="tll mono">São Paulo, SP — híbrido</p><ul class="bl">
<li>Dashboard analítico React + Next.js consumindo GraphQL — 200+ clientes.</li>
<li>Otimização PostgreSQL com índices compostos — 65% menos tempo de resposta.</li>
<li>CI/CD com GitHub Actions + Docker — deploy 25 → 6 min.</li>
</ul></article>
<article class="tli"><div class="tlh"><span class="tlr">Backend Developer</span><span class="tlp mono">2018-06 → 2019-12</span></div><p class="tlc">StartupLab</p><p class="tll mono">Campinas, SP — presencial</p><ul class="bl">
<li>APIs REST em FastAPI — 50k+ transações/dia.</li>
<li>Filas RabbitMQ para relatórios assíncronos — timeouts eliminados em pico.</li>
<li>Cobertura de testes 85% — 40% menos bugs em produção.</li>
</ul></article>
</div>
<h2>Stack</h2>
<div class="sk">
<span class="skl mono">languages</span><span class="ski"><span class="chip mono">TypeScript</span><span class="chip mono">JavaScript</span><span class="chip mono">Python</span><span class="chip mono">Java</span><span class="chip mono">SQL</span></span>
<span class="skl mono">backend</span><span class="ski"><span class="chip mono">Node.js</span><span class="chip mono">NestJS</span><span class="chip mono">FastAPI</span><span class="chip mono">Laravel</span><span class="chip mono">GraphQL</span><span class="chip mono">REST</span></span>
<span class="skl mono">frontend</span><span class="ski"><span class="chip mono">React</span><span class="chip mono">Next.js</span><span class="chip mono">HTML</span><span class="chip mono">CSS</span><span class="chip mono">Tailwind</span></span>
<span class="skl mono">data</span><span class="ski"><span class="chip mono">PostgreSQL</span><span class="chip mono">MySQL</span><span class="chip mono">Redis</span><span class="chip mono">MongoDB</span><span class="chip mono">RabbitMQ</span></span>
<span class="skl mono">infra</span><span class="ski"><span class="chip mono">Docker</span><span class="chip mono">AWS</span><span class="chip mono">CI/CD</span><span class="chip mono">OpenTelemetry</span></span>
</div>
<h2>Projetos</h2>
<article class="pj"><div class="pjh"><span class="pjn">OpenMetrics Dashboard</span><span class="pjl mono"><a href="https://github.com/example/openmetrics">github.com/example/openmetrics</a></span></div><p class="pjd">Dashboard open-source para métricas em tempo real, múltiplas fontes e alertas configuráveis. 500+ devs ativos.</p><p class="pjt mono">TypeScript · React · Node.js · WebSocket · PostgreSQL</p></article>
<article class="pj"><div class="pjh"><span class="pjn">FastQueue</span><span class="pjl mono"><a href="https://github.com/example/fastqueue">github.com/example/fastqueue</a></span></div><p class="pjd">Biblioteca leve de filas para Node.js com suporte a Redis e RabbitMQ.</p><p class="pjt mono">Node.js · TypeScript · Redis · RabbitMQ</p></article>
<h2>Formação & Idiomas</h2>
<div class="two">
<div>
<div class="ed"><p class="edc">Bacharelado em Ciência da Computação</p><p class="edi">UNICAMP</p><p class="edp mono">2014 — 2018</p></div>
<div class="ed"><p class="edc">Especialização em Arquitetura de Software</p><p class="edi">ITA</p><p class="edp mono">2019 — 2020</p></div>
</div>
<div>
<p class="lg"><b>Português</b> — Nativo</p>
<p class="lg"><b>Inglês</b> — Avançado (C1)</p>
<p class="lg"><b>Espanhol</b> — Intermediário (B1)</p>
</div>
</div>
</main></body></html>"""

# ============================================================
# TEMPLATE D — EXECUTIVE / PREMIUM
# ============================================================
FILES["template-d-executive.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucas Andrade — Executive</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;font-size:10.5pt;color:#151719;background:#e9e6e0;line-height:1.5;display:flex;justify-content:center;padding:24px 0}
.r{width:210mm;min-height:297mm;background:#fff;padding:26mm 24mm;box-shadow:0 2px 16px rgba(0,0,0,.1)}
.serif{font-family:Georgia,"Iowan Old Style",Cambria,serif}
.hd{text-align:center;padding-bottom:14pt;margin-bottom:20pt;border-bottom:.5pt solid #d9d4cc}
h1{font-size:26pt;font-weight:400;letter-spacing:.02em;line-height:1.1}
.rl{font-size:10pt;font-weight:500;text-transform:uppercase;letter-spacing:.28em;color:#8a6a2f;margin-top:8pt}
.meta{font-size:8.8pt;color:#7a8087;margin-top:12pt}
.meta span{white-space:nowrap}
.meta .sep{color:#d9d4cc;margin:0 8pt}
.meta a{color:#7a8087;text-decoration:none;border-bottom:.5pt solid #ece8e1}
h2{font-size:11.5pt;font-weight:400;font-style:italic;color:#151719;letter-spacing:.04em;margin:20pt 0 10pt;text-align:center}
h2 span{display:inline-block;padding:0 14pt;position:relative}
h2 span::before,h2 span::after{content:"";position:absolute;top:50%;width:36pt;height:.5pt;background:#d9d4cc}
h2 span::before{right:100%}
h2 span::after{left:100%}
.sum{font-size:11pt;line-height:1.65;color:#3a3f45;text-align:justify;font-style:italic}
.j{margin-bottom:16pt}
.jh{display:flex;justify-content:space-between;align-items:baseline;gap:10pt;flex-wrap:wrap;margin-bottom:3pt}
.jr{font-size:12pt;font-weight:400}
.jp{font-size:8.8pt;color:#7a8087;white-space:nowrap;letter-spacing:.06em;text-transform:uppercase}
.jc{font-size:9.8pt;color:#8a6a2f;font-weight:500;letter-spacing:.02em;margin-bottom:1pt}
.jl{font-size:8.8pt;color:#7a8087;margin-bottom:6pt}
ul.bl{list-style:none}
ul.bl li{font-size:9.8pt;color:#3a3f45;margin-bottom:3.5pt;padding-left:14pt;position:relative;line-height:1.55}
ul.bl li::before{content:"—";position:absolute;left:0;color:#8a6a2f}
.sk{display:flex;flex-direction:column;gap:6pt}
.skr{font-size:9.8pt;line-height:1.5;display:grid;grid-template-columns:96pt 1fr;gap:10pt;align-items:baseline}
.skl{font-style:italic;color:#151719;font-size:10pt}
.ski{color:#3a3f45}
.pj{margin-bottom:12pt}
.pjh{display:flex;justify-content:space-between;gap:10pt;flex-wrap:wrap;align-items:baseline;margin-bottom:2pt}
.pjn{font-size:11pt;font-style:italic}
.pjl{font-size:8.5pt;color:#7a8087}
.pjl a{color:#7a8087;text-decoration:none;border-bottom:.5pt solid #ece8e1}
.pjd{font-size:9.6pt;color:#3a3f45;line-height:1.55}
.pjt{font-size:8.5pt;color:#8a6a2f;letter-spacing:.04em;margin-top:3pt}
.two{display:grid;grid-template-columns:1fr 1fr;gap:24pt}
.ed{margin-bottom:10pt}
.edc{font-size:10.8pt;font-style:italic}
.edi{font-size:9.6pt;color:#3a3f45}
.edp{font-size:8.6pt;color:#7a8087;letter-spacing:.06em;text-transform:uppercase;margin-top:1pt}
.lg{font-size:9.6pt;color:#3a3f45;margin-bottom:5pt}
.lg b{font-style:italic;font-weight:400;color:#151719}
@page{size:A4;margin:0}
@media print{body{background:none;padding:0;display:block}.r{width:100%;min-height:auto;box-shadow:none}a{color:inherit;text-decoration:none;border:none!important}h2{page-break-after:avoid}.j,.pj,.ed{page-break-inside:avoid}}
@media screen and (max-width:820px){body{padding:0}.r{width:100%;padding:28px 22px}h1{font-size:22pt}.rl{letter-spacing:.18em}.meta span{white-space:normal;display:block;margin-bottom:2px}.meta .sep{display:none}.two{grid-template-columns:1fr;gap:10pt}.skr{grid-template-columns:1fr;gap:2pt}.jh{flex-direction:column;gap:2px}.jp{white-space:normal}}
</style></head><body><main class="r">
<header class="hd">
<h1 class="serif">Lucas Andrade</h1>
<p class="rl">Full Stack Software Engineer</p>
<p class="meta">
<span>São Paulo, SP — Brasil</span><span class="sep">·</span>
<span><a href="mailto:email@example.com">email@example.com</a></span><span class="sep">·</span>
<span><a href="https://github.com/example">github.com/example</a></span><span class="sep">·</span>
<span><a href="https://linkedin.com/in/example">linkedin.com/in/example</a></span>
</p></header>
<h2><span>Perfil</span></h2>
<p class="sum serif">Engenheiro de software com mais de sete anos de atuação em sistemas distribuídos e plataformas web de alta escala. Combina profundidade técnica em TypeScript, Node.js e React com visão arquitetural e liderança de equipes. Histórico consistente na redução de latência, modernização de legados e estabelecimento de práticas de observabilidade.</p>
<h2><span>Experiência</span></h2>
<article class="j"><div class="jh"><span class="jr serif">Senior Full Stack Engineer</span><span class="jp">2022 — Presente</span></div><p class="jc">TechNova Solutions</p><p class="jl">São Paulo, SP — Remoto</p><ul class="bl">
<li>Redesenhou o pipeline de processamento de documentos com workers assíncronos e Redis, reduzindo o tempo médio em 42%.</li>
<li>Liderou a migração do monolito Laravel para microsserviços Node.js e NestJS, ampliando a escalabilidade horizontal em três vezes.</li>
<li>Estabeleceu observabilidade com OpenTelemetry e Grafana, reduzindo o MTTR de incidentes críticos de 45 para 12 minutos.</li>
<li>Mentorou quatro engenheiros júniores em testes automatizados e design de APIs REST.</li>
</ul></article>
<article class="j"><div class="jh"><span class="jr serif">Full Stack Developer</span><span class="jp">2020 — 2022</span></div><p class="jc">DataFlow Systems</p><p class="jl">São Paulo, SP — Híbrido</p><ul class="bl">
<li>Desenvolveu dashboard analítico em React e Next.js sobre GraphQL, adotado por mais de 200 clientes corporativos.</li>
<li>Otimizou consultas PostgreSQL com índices compostos e materialized views, reduzindo o tempo de resposta em 65%.</li>
<li>Automatizou pipelines de CI/CD com GitHub Actions e Docker, reduzindo o deploy de 25 para 6 minutos.</li>
</ul></article>
<article class="j"><div class="jh"><span class="jr serif">Backend Developer</span><span class="jp">2018 — 2019</span></div><p class="jc">StartupLab</p><p class="jl">Campinas, SP — Presencial</p><ul class="bl">
<li>Construiu APIs REST em FastAPI processando mais de 50 mil transações diárias.</li>
<li>Implementou filas com RabbitMQ para geração assíncrona de relatórios, eliminando timeouts em horários de pico.</li>
<li>Elevou a cobertura de testes para 85%, reduzindo bugs em produção em 40%.</li>
</ul></article>
<h2><span>Competências</span></h2>
<div class="sk">
<div class="skr"><span class="skl serif">Linguagens</span><span class="ski">TypeScript · JavaScript · Python · Java · SQL</span></div>
<div class="skr"><span class="skl serif">Backend</span><span class="ski">Node.js · NestJS · FastAPI · Laravel · GraphQL · REST</span></div>
<div class="skr"><span class="skl serif">Frontend</span><span class="ski">React · Next.js · HTML · CSS · Tailwind CSS</span></div>
<div class="skr"><span class="skl serif">Dados</span><span class="ski">PostgreSQL · MySQL · Redis · MongoDB · RabbitMQ</span></div>
<div class="skr"><span class="skl serif">Infraestrutura</span><span class="ski">Docker · AWS · CI/CD · OpenTelemetry</span></div>
</div>
<h2><span>Projetos Selecionados</span></h2>
<article class="pj"><div class="pjh"><span class="pjn serif">OpenMetrics Dashboard</span><span class="pjl"><a href="https://github.com/example/openmetrics">github.com/example/openmetrics</a></span></div><p class="pjd">Dashboard open-source para visualização de métricas em tempo real, com múltiplas fontes de dados e alertas configuráveis. Adotado por mais de 500 desenvolvedores.</p><p class="pjt">TypeScript · React · Node.js · WebSocket · PostgreSQL</p></article>
<article class="pj"><div class="pjh"><span class="pjn serif">FastQueue</span><span class="pjl"><a href="https://github.com/example/fastqueue">github.com/example/fastqueue</a></span></div><p class="pjd">Biblioteca leve de gerenciamento de filas para Node.js com suporte a Redis e RabbitMQ, voltada a microsserviços.</p><p class="pjt">Node.js · TypeScript · Redis · RabbitMQ</p></article>
<h2><span>Formação & Idiomas</span></h2>
<div class="two">
<div>
<div class="ed"><p class="edc serif">Bacharelado em Ciência da Computação</p><p class="edi">Universidade Estadual de Campinas (UNICAMP)</p><p class="edp">2014 — 2018</p></div>
<div class="ed"><p class="edc serif">Especialização em Arquitetura de Software</p><p class="edi">Instituto Tecnológico de Aeronáutica (ITA)</p><p class="edp">2019 — 2020</p></div>
</div>
<div>
<p class="lg"><b>Português</b> — Nativo</p>
<p class="lg"><b>Inglês</b> — Avançado (C1)</p>
<p class="lg"><b>Espanhol</b> — Intermediário (B1)</p>
<p class="lg" style="margin-top:14pt"><b>AWS Certified Solutions Architect</b> — Associate, 2023</p>
<p class="lg"><b>Node.js Application Development</b> — OpenJS Foundation, 2022</p>
</div>
</div>
</main></body></html>"""

# ============================================================
# TEMPLATE E — CREATIVE TECH
# ============================================================
FILES["template-e-creative.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lucas Andrade — Creative Tech</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;font-size:10pt;color:#0f172a;background:#dde3ec;line-height:1.45;display:flex;justify-content:center;padding:20px 0}
.r{width:210mm;min-height:297mm;background:#fff;box-shadow:0 4px 18px rgba(0,0,0,.14);display:flex;flex-direction:column;overflow:hidden}
.hd{background:linear-gradient(135deg,#4f46e5 0%,#7c3aed 100%);color:#fff;padding:14mm 16mm 12mm}
h1{font-size:24pt;font-weight:800;letter-spacing:-.02em;line-height:1.05}
.rl{font-size:11pt;font-weight:500;color:#e0e7ff;margin-top:4pt;letter-spacing:.02em}
.meta{display:flex;flex-wrap:wrap;gap:6pt 16pt;margin-top:12pt;font-size:9pt}
.meta a{color:#e0e7ff;text-decoration:none;border-bottom:1px solid rgba(255,255,255,.35)}
.bd{padding:14mm 16mm 16mm;display:flex;flex-direction:column;gap:12pt;flex:1}
h2{font-size:10.5pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#4f46e5;margin-bottom:7pt;display:flex;align-items:center;gap:8pt}
h2::after{content:"";flex:1;height:2pt;background:#eef2ff;border-radius:2pt}
.sum{font-size:10pt;line-height:1.55;color:#334155;background:#eef2ff;padding:10pt 12pt;border-radius:6pt;border-left:3pt solid #4f46e5}
.job{padding:9pt 0;border-bottom:1px dashed #e2e8f0}
.job:last-child{border-bottom:none;padding-bottom:0}
.jh{display:flex;justify-content:space-between;gap:8pt;flex-wrap:wrap;align-items:baseline}
.jr{font-weight:700;font-size:10.5pt}
.jp{font-size:8.8pt;color:#4f46e5;font-weight:600;background:#eef2ff;padding:1pt 6pt;border-radius:3pt;white-space:nowrap}
.jc{font-size:9.8pt;color:#334155;font-weight:600;margin-top:1pt}
.jl{font-size:8.8pt;color:#64748b;margin-bottom:5pt}
ul.bl{list-style:none}
ul.bl li{font-size:9.6pt;color:#334155;margin-bottom:3pt;padding-left:13pt;position:relative;line-height:1.5}
ul.bl li::before{content:"";position:absolute;left:0;top:6pt;width:5pt;height:5pt;background:#4f46e5;border-radius:2pt;transform:rotate(45deg)}
.sks{display:grid;grid-template-columns:repeat(2,1fr);gap:8pt}
.skg{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6pt;padding:8pt 10pt}
.skl{font-size:8.5pt;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:#4f46e5;margin-bottom:4pt;display:block}
.ski{font-size:9.4pt;color:#334155;line-height:1.5}
.pjs{display:grid;grid-template-columns:1fr 1fr;gap:8pt}
.pj{background:#f8fafc;border:1px solid #e2e8f0;border-radius:6pt;padding:9pt 10pt}
.pjn{font-weight:700;font-size:10pt}
.pjl{font-size:8.4pt;color:#4f46e5;display:block;margin-top:1pt;word-break:break-all}
.pjl a{color:#4f46e5;text-decoration:none}
.pjd{font-size:9.2pt;color:#334155;margin-top:4pt;line-height:1.45}
.pjt{font-size:8.4pt;color:#64748b;margin-top:4pt;font-weight:600}
.two{display:grid;grid-template-columns:1.4fr 1fr;gap:16pt}
.ed{margin-bottom:6pt}
.edc{font-weight:700;font-size:9.8pt}
.edi{font-size:9.5pt;color:#334155}
.edp{font-size:8.5pt;color:#64748b}
.lg{font-size:9.5pt;color:#334155;margin-bottom:3pt}
.lg b{color:#0f172a}
@page{size:A4;margin:0}
@media print{body{background:none;padding:0;display:block}.r{width:100%;min-height:auto;box-shadow:none}.hd{background:#4f46e5!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}a{color:inherit;text-decoration:none;border:none!important}h2{page-break-after:avoid}.job,.pj,.skg{page-break-inside:avoid}}
@media screen and (max-width:820px){body{padding:0}.r{width:100%;min-height:auto}.hd{padding:22px 20px}h1{font-size:20pt}.bd{padding:20px}.sks,.pjs{grid-template-columns:1fr}.two{grid-template-columns:1fr;gap:10pt}.jh{flex-direction:column;gap:3pt}.jp{align-self:flex-start}}
</style></head><body><main class="r">
<header class="hd">
<h1>Lucas Andrade</h1>
<p class="rl">Full Stack Software Engineer</p>
<div class="meta">
<span>São Paulo, SP — Brasil</span>
<span><a href="mailto:email@example.com">email@example.com</a></span>
<span><a href="https://github.com/example">github.com/example</a></span>
<span><a href="https://linkedin.com/in/example">linkedin.com/in/example</a></span>
</div></header>
<div class="bd">
<section><h2>Resumo</h2><p class="sum">Engenheiro full stack com 7+ anos construindo sistemas distribuídos e produtos web de alta escala. Especializado em TypeScript, Node.js e React, com foco em arquitetura limpa, observabilidade e entrega contínua. Liderança técnica comprovada em times multidisciplinares.</p></section>
<section><h2>Experiência</h2>
<article class="job"><div class="jh"><span class="jr">Senior Full Stack Engineer</span><span class="jp">2022 — Presente</span></div><p class="jc">TechNova Solutions</p><p class="jl">São Paulo, SP — Remoto</p><ul class="bl">
<li>Pipeline de documentos com workers assíncronos e Redis — 42% menos tempo médio.</li>
<li>Migração monolito Laravel → microsserviços Node.js + NestJS — 3× de escala.</li>
<li>Observabilidade com OpenTelemetry e Grafana — MTTR 45 → 12 min.</li>
<li>Mentoria de 4 engenheiros júniores em testes e design de APIs REST.</li>
</ul></article>
<article class="job"><div class="jh"><span class="jr">Full Stack Developer</span><span class="jp">2020 — 2022</span></div><p class="jc">DataFlow Systems</p><p class="jl">São Paulo, SP — Híbrido</p><ul class="bl">
<li>Dashboard analítico React + Next.js sobre GraphQL — 200+ clientes.</li>
<li>Otimização PostgreSQL com índices compostos — 65% menos tempo de resposta.</li>
<li>CI/CD com GitHub Actions + Docker — deploy 25 → 6 min.</li>
</ul></article>
<article class="job"><div class="jh"><span class="jr">Backend Developer</span><span class="jp">2018 — 2019</span></div><p class="jc">StartupLab</p><p class="jl">Campinas, SP — Presencial</p><ul class="bl">
<li>APIs REST em FastAPI — 50k+ transações/dia.</li>
<li>Filas RabbitMQ para relatórios assíncronos — timeouts eliminados em pico.</li>
<li>Cobertura de testes 85% — 40% menos bugs em produção.</li>
</ul></article>
</section>
<section><h2>Competências</h2>
<div class="sks">
<div class="skg"><span class="skl">Languages</span><p class="ski">TypeScript · JavaScript · Python · Java · SQL</p></div>
<div class="skg"><span class="skl">Backend</span><p class="ski">Node.js · NestJS · FastAPI · Laravel · GraphQL · REST</p></div>
<div class="skg"><span class="skl">Frontend</span><p class="ski">React · Next.js · HTML · CSS · Tailwind CSS</p></div>
<div class="skg"><span class="skl">Data</span><p class="ski">PostgreSQL · MySQL · Redis · MongoDB · RabbitMQ</p></div>
<div class="skg"><span class="skl">Infrastructure</span><p class="ski">Docker · AWS · CI/CD · OpenTelemetry</p></div>
<div class="skg"><span class="skl">Idiomas</span><p class="ski">Português — Nativo · Inglês — C1 · Espanhol — B1</p></div>
</div>
</section>
<section><h2>Projetos</h2>
<div class="pjs">
<article class="pj"><p class="pjn">OpenMetrics Dashboard</p><span class="pjl"><a href="https://github.com/example/openmetrics">github.com/example/openmetrics</a></span><p class="pjd">Dashboard open-source para métricas em tempo real, com múltiplas fontes e alertas. 500+ devs ativos.</p><p class="pjt">TypeScript · React · Node.js · PostgreSQL</p></article>
<article class="pj"><p class="pjn">FastQueue</p><span class="pjl"><a href="https://github.com/example/fastqueue">github.com/example/fastqueue</a></span><p class="pjd">Biblioteca leve de filas para Node.js com suporte a Redis e RabbitMQ.</p><p class="pjt">Node.js · TypeScript · Redis · RabbitMQ</p></article>
</div>
</section>
<section><h2>Formação & Certificações</h2>
<div class="two">
<div>
<div class="ed"><p class="edc">Bacharelado em Ciência da Computação</p><p class="edi">Universidade Estadual de Campinas (UNICAMP)</p><p class="edp">2014 — 2018</p></div>
<div class="ed"><p class="edc">Especialização em Arquitetura de Software</p><p class="edi">Instituto Tecnológico de Aeronáutica (ITA)</p><p class="edp">2019 — 2020</p></div>
</div>
<div>
<p class="lg"><b>AWS Certified Solutions Architect</b> — Associate, 2023</p>
<p class="lg"><b>Node.js Application Development</b> — OpenJS Foundation, 2022</p>
<p class="lg"><b>Scrum Master Certified</b> — Scrum Alliance, 2021</p>
</div>
</div>
</section>
</div>
</main></body></html>"""

# ============================================================
# INDEX COM SELETOR (iframe)
# ============================================================
FILES["index.html"] = r"""<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Templates de Currículo — Lucas Andrade</title>
<style>
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:Inter,Arial,sans-serif;background:#dde3ec;height:100vh;overflow:hidden;display:flex;flex-direction:column}
nav{background:rgba(15,23,42,.96);height:52px;display:flex;align-items:center;justify-content:center;gap:6px;border-bottom:1px solid rgba(255,255,255,.08);font-size:13px;flex-wrap:wrap;padding:0 8px}
label{color:#94a3b8;margin-right:8px;font-weight:500}
button{background:transparent;border:1px solid rgba(255,255,255,.15);color:#cbd5e1;padding:6px 14px;border-radius:6px;cursor:pointer;font:inherit;transition:all .15s}
button:hover{background:rgba(255,255,255,.08);color:#fff}
button.active{background:#4f46e5;border-color:#4f46e5;color:#fff;font-weight:600}
iframe{flex:1;border:0;width:100%;background:#dde3ec}
@media (max-width:640px){label{display:none}button{font-size:11px;padding:5px 10px}}
</style></head><body>
<nav>
<label>Template:</label>
<button data-src="template-a-ats.html" class="active">A — ATS / Corporate</button>
<button data-src="template-b-modern.html">B — Modern Professional</button>
<button data-src="template-c-technical.html">C — Technical</button>
<button data-src="template-d-executive.html">D — Executive</button>
<button data-src="template-e-creative.html">E — Creative Tech</button>
</nav>
<iframe id="v" src="template-a-ats.html" title="Visualização do template"></iframe>
<script>
var btns=document.querySelectorAll('button'),f=document.getElementById('v');
btns.forEach(function(b){b.addEventListener('click',function(){
  btns.forEach(function(x){x.classList.remove('active')});
  b.classList.add('active');
  f.src=b.getAttribute('data-src');
})});
</script>
</body></html>"""

# ============================================================
# README
# ============================================================
FILES["README.md"] = """# Templates de Currículo — Lucas Andrade

Conjunto de 5 templates profissionais, com foco em ATS, legibilidade e impressão A4.

## Conteúdo
- `template-a-ats.html` — ATS / Corporate (1 coluna, sem ruído)
- `template-b-modern.html` — Modern Professional (sidebar + main)
- `template-c-technical.html` — Technical / Engineering (timeline + chips)
- `template-d-executive.html` — Executive / Premium (serifado, muito respiro)
- `template-e-creative.html` — Creative Tech (header colorido, grid)
- `index.html` — seletor visual com iframe

## Como usar
1. Abra `index.html` no navegador (Chrome/Firefox/Edge).
2. Clique nos botões para alternar entre os templates.
3. Para exportar PDF: abra o arquivo do template direto (ex.: `template-a-ats.html`)
   e use `Ctrl+P` (Cmd+P no macOS) → Destino: "Salvar como PDF" → Papel A4 →
   Margens: Nenhuma → Layout: Retrato → marque "Gráficos de segundo plano".

## Trocar o conteúdo
Cada arquivo é standalone: todo o conteúdo está no HTML, o CSS embutido em `<style>`.
Basta editar os textos diretamente (nome, empresas, datas, links) mantendo a estrutura de tags.

## Impressão
Cada template já define `@page { size: A4; margin: 0 }` e regras que evitam
quebras ruins (títulos órfãos, bullets partidos, seções cortadas).

## Licença
Uso livre. Conteúdo mock fictício.
"""

for name, content in FILES.items():
    (ROOT / name).write_text(content, encoding="utf-8")

zip_path = pathlib.Path("templates-curriculo.zip")
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
    for f in sorted(ROOT.rglob("*")):
        z.write(f, f.relative_to(ROOT.parent))

print("OK — {}".format(zip_path.resolve()))
print("Conteudo:")
for f in sorted(ROOT.rglob("*")):
    print("  " + str(f))
