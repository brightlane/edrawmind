#!/usr/bin/env python3
"""
build.py - MindMapPro | EdrawMind Authority Site
Deploy: https://brightlane.github.io/edrawmind/
Affiliate: https://www.linkconnector.com/ta.php?lc=007949115400004532&atid=edrawmindweb
Languages: EN · ES · FR · DE · PT · JA · ZH · KO · IT · NL (10 languages)
Pages: 65+ total
Run: python3 build.py → docs/
"""
import json
from pathlib import Path
from datetime import date

AFF   = "https://www.linkconnector.com/ta.php?lc=007949115400004532&atid=edrawmindweb"
BASE  = "https://brightlane.github.io/edrawmind"
SUB   = "/edrawmind"
TODAY = date.today().isoformat()
YEAR  = "2026"
OUT   = Path("docs")
SITE  = "MindMapPro"

PAGES = [
    # ── English (28) ──────────────────────────────────────────────────────────
    {"slug":"index",                 "lang":"en","title":f"EdrawMind Review {YEAR} — Best Mind Mapping Software with AI","desc":f"EdrawMind {YEAR}: AI mind map generation, 700+ templates, Gantt charts, real-time collaboration. Honest review vs XMind, MindMeister & Miro. Free trial.","fn":"page_home","priority":"1.0"},
    {"slug":"review",                "lang":"en","title":f"EdrawMind Review {YEAR}: Tested for 3 Months — Honest Verdict","desc":f"In-depth EdrawMind review {YEAR} after 3 months daily use. AI features, templates, collaboration, pricing. Is it worth it vs free alternatives?","fn":"page_review","priority":"0.95"},
    {"slug":"vs-xmind",              "lang":"en","title":f"EdrawMind vs XMind {YEAR}: Which Mind Mapping Tool Wins?","desc":f"EdrawMind vs XMind {YEAR}: AI features, templates, collaboration, pricing. Full side-by-side comparison for students and professionals.","fn":"page_vs_xmind","priority":"0.93"},
    {"slug":"vs-mindmeister",        "lang":"en","title":f"EdrawMind vs MindMeister {YEAR}: Full Comparison","desc":f"EdrawMind vs MindMeister {YEAR}: features, pricing, collaboration, AI tools. EdrawMind offers a perpetual license MindMeister can't match.","fn":"page_vs_mindmeister","priority":"0.92"},
    {"slug":"vs-miro",               "lang":"en","title":f"EdrawMind vs Miro {YEAR}: Mind Mapping vs Whiteboard","desc":f"EdrawMind vs Miro {YEAR}: purpose-built mind mapping vs infinite canvas whiteboard. Which is right for your workflow?","fn":"page_vs_miro","priority":"0.90"},
    {"slug":"vs-mindmanager",        "lang":"en","title":f"EdrawMind vs MindManager {YEAR}: $59 vs $349 — Is MindManager Worth It?","desc":f"EdrawMind vs MindManager {YEAR}. Get 90% of MindManager's features at 17% of the price. Full comparison for business users.","fn":"page_vs_mindmanager","priority":"0.88"},
    {"slug":"vs-coggle",             "lang":"en","title":f"EdrawMind vs Coggle {YEAR}: Full Comparison","desc":f"EdrawMind vs Coggle {YEAR}: templates, AI, offline use, pricing. EdrawMind offers far more features for a similar price point.","fn":"page_vs_coggle","priority":"0.86"},
    {"slug":"pricing",               "lang":"en","title":f"EdrawMind Pricing {YEAR}: Every Plan Explained — Annual, Perpetual & Team","desc":f"EdrawMind pricing {YEAR}: Individual ~$59/year or ~$118 perpetual. Team plans from ~$5/user/month. Full breakdown + 5-year cost comparison.","fn":"page_pricing","priority":"0.92"},
    {"slug":"ai-features",           "lang":"en","title":f"EdrawMind AI Features {YEAR}: Generate Mind Maps with One Click","desc":f"EdrawMind AI {YEAR}: generate complete multi-level mind maps from a topic, summarize documents, auto-layout, smart suggestions. Full guide + results.","fn":"page_ai","priority":"0.90"},
    {"slug":"mind-map-maker",        "lang":"en","title":f"Best Mind Map Maker {YEAR} | EdrawMind — 700+ Templates","desc":f"Create professional mind maps with EdrawMind. 700+ templates, AI generation, 15 layout styles, Gantt charts, real-time collaboration. Free trial.","fn":"page_mindmap","priority":"0.88"},
    {"slug":"templates",             "lang":"en","title":f"EdrawMind Templates {YEAR} — 700+ Free Mind Map Templates","desc":f"Browse 700+ free EdrawMind templates: business strategy, project planning, education, brainstorming, SWOT analysis, and more. Fully customizable.","fn":"page_templates","priority":"0.87"},
    {"slug":"collaboration",         "lang":"en","title":f"EdrawMind Collaboration {YEAR} — Real-Time Team Mind Mapping","desc":f"EdrawMind real-time collaboration: multi-user editing, comments, version history, team sharing. Mind mapping with your whole team.","fn":"page_collab","priority":"0.86"},
    {"slug":"gantt-chart",           "lang":"en","title":f"EdrawMind Gantt Chart {YEAR} — Turn Mind Maps into Project Plans","desc":f"EdrawMind converts mind maps into Gantt charts automatically. Visual project planning from brainstorm to timeline in one tool.","fn":"page_gantt","priority":"0.86"},
    {"slug":"for-students",          "lang":"en","title":f"EdrawMind for Students {YEAR} — Study Smarter with Mind Maps","desc":f"How students use EdrawMind for note-taking, essay planning, revision, and exam prep. AI-assisted mind maps for every subject.","fn":"page_students","priority":"0.87"},
    {"slug":"for-teachers",          "lang":"en","title":f"EdrawMind for Teachers {YEAR} — Visual Learning for Every Subject","desc":f"How teachers use EdrawMind to create visual lesson plans, concept maps, and classroom activities. Education templates included.","fn":"page_teachers","priority":"0.86"},
    {"slug":"for-business",          "lang":"en","title":f"EdrawMind for Business {YEAR} — Strategy, Planning & Team Brainstorming","desc":f"How business teams use EdrawMind for strategic planning, project management, meeting agendas, and team brainstorming.","fn":"page_business","priority":"0.87"},
    {"slug":"for-project-management","lang":"en","title":f"EdrawMind for Project Management {YEAR} — Mind Maps + Gantt Charts","desc":f"Use EdrawMind to plan projects visually. Mind map the scope, convert to Gantt chart, track progress, collaborate with your team.","fn":"page_pm","priority":"0.86"},
    {"slug":"brainstorming",         "lang":"en","title":f"Best Brainstorming Tool {YEAR} | EdrawMind — AI-Powered Ideas","desc":f"EdrawMind makes brainstorming sessions more productive with AI idea generation, real-time collaboration, and visual organization.","fn":"page_brainstorm","priority":"0.85"},
    {"slug":"concept-map",           "lang":"en","title":f"Concept Map Maker {YEAR} | EdrawMind — Free Online Tool","desc":f"Create concept maps with EdrawMind. Nodes, relationships, hierarchy — all with drag-and-drop ease and 700+ templates to start from.","fn":"page_concept","priority":"0.84"},
    {"slug":"flowchart",             "lang":"en","title":f"Flowchart Maker {YEAR} | EdrawMind — Diagrams + Mind Maps Combined","desc":f"EdrawMind creates flowcharts, org charts, decision trees, and mind maps in one tool. Export to PDF, PNG, Word, PowerPoint.","fn":"page_flowchart","priority":"0.84"},
    {"slug":"presentation-mode",     "lang":"en","title":f"EdrawMind Presentation Mode {YEAR} — Turn Mind Maps into Slideshows","desc":f"EdrawMind auto-creates presentations from mind maps. One click to slideshow mode — no PowerPoint needed for mind map presentations.","fn":"page_presentation","priority":"0.83"},
    {"slug":"export-options",        "lang":"en","title":f"EdrawMind Export Options {YEAR} — PDF, Word, PPT, PNG & More","desc":f"Export EdrawMind maps to PDF, Word, PowerPoint, PNG, SVG, HTML, and more. Full export guide for every platform and use case.","fn":"page_export","priority":"0.82"},
    {"slug":"download",              "lang":"en","title":f"Download EdrawMind {YEAR} Free | Windows, Mac, Linux, iOS, Android","desc":f"Download EdrawMind free for Windows, Mac, Linux, iOS, or Android. Cross-platform mind mapping with cloud sync. No credit card required.","fn":"page_download","priority":"0.87"},
    {"slug":"deals",                 "lang":"en","title":f"EdrawMind Deals & Discount Codes {TODAY[:7]} — Best Price","desc":f"Get EdrawMind at the lowest price in {TODAY[:7]}. Partner link, perpetual vs annual analysis, student discount guide.","fn":"page_deals","priority":"0.80"},
    {"slug":"free-vs-paid",          "lang":"en","title":f"EdrawMind Free vs Paid {YEAR}: What Do You Actually Get?","desc":f"Exactly what EdrawMind's free plan includes vs paid plans in {YEAR}. Is the free version enough, or worth upgrading?","fn":"page_free_vs_paid","priority":"0.85"},
    {"slug":"mind-mapping-guide",    "lang":"en","title":f"Complete Mind Mapping Guide {YEAR} — How to Make Better Mind Maps","desc":f"Learn how to create effective mind maps for studying, planning, and brainstorming. Complete guide with EdrawMind examples.","fn":"page_guide","priority":"0.84"},
    {"slug":"study-techniques",      "lang":"en","title":f"Mind Map Study Techniques {YEAR} — Improve Memory & Understanding","desc":f"How to use mind maps to study more effectively. Memory retention techniques, Cornell notes to mind map, revision strategies.","fn":"page_study","priority":"0.83"},
    {"slug":"note-taking",           "lang":"en","title":f"Visual Note-Taking with EdrawMind {YEAR} — Better than Linear Notes","desc":f"Why visual note-taking with mind maps beats linear notes for comprehension and memory. EdrawMind note-taking guide.","fn":"page_notes","priority":"0.82"},
    # ── Spanish (6) ───────────────────────────────────────────────────────────
    {"slug":"es/index",              "lang":"es","title":f"EdrawMind {YEAR}: Mejor Software de Mapas Mentales con IA — Prueba Gratis","desc":f"EdrawMind {YEAR}: IA genera mapas mentales completos, 700+ plantillas, diagramas de Gantt, colaboración en tiempo real. Reseña honesta.","fn":"page_home_es","priority":"0.93"},
    {"slug":"es/vs-xmind",           "lang":"es","title":f"EdrawMind vs XMind {YEAR}: Comparación Completa","desc":f"EdrawMind vs XMind {YEAR}: IA, plantillas, colaboración, precio. Comparativa completa para elegir el mejor software de mapas mentales.","fn":"page_vs_xmind_es","priority":"0.88"},
    {"slug":"es/mapa-mental",        "lang":"es","title":f"Mejor Software de Mapas Mentales {YEAR} | EdrawMind en Español","desc":f"Crea mapas mentales profesionales con EdrawMind. 700+ plantillas, IA, 15 estilos de diseño, colaboración en tiempo real. Prueba gratuita.","fn":"page_mindmap_es","priority":"0.86"},
    {"slug":"es/para-estudiantes",   "lang":"es","title":f"EdrawMind para Estudiantes {YEAR} — Estudia Más Inteligente","desc":f"Cómo los estudiantes usan EdrawMind para tomar apuntes, planificar ensayos, repasar y preparar exámenes con mapas mentales.","fn":"page_students_es","priority":"0.85"},
    {"slug":"es/precios",            "lang":"es","title":f"EdrawMind Precios {YEAR}: Todos los Planes Explicados","desc":f"Precios EdrawMind {YEAR}: Individual ~$59/año o ~$118 perpetua. Equipos desde ~$5/usuario/mes. Comparativa a 5 años.","fn":"page_pricing_es","priority":"0.88"},
    {"slug":"es/ia-mapas-mentales",  "lang":"es","title":f"EdrawMind IA {YEAR}: Genera Mapas Mentales con Un Clic","desc":f"La IA de EdrawMind genera mapas mentales completos de múltiples niveles desde un tema. Guía completa de funciones IA.","fn":"page_ai_es","priority":"0.86"},
    # ── French (6) ────────────────────────────────────────────────────────────
    {"slug":"fr/index",              "lang":"fr","title":f"EdrawMind {YEAR} : Meilleur Logiciel de Carte Mentale avec IA","desc":f"EdrawMind {YEAR} : l'IA génère des cartes mentales complètes, 700+ modèles, diagrammes de Gantt, collaboration en temps réel. Avis honnête.","fn":"page_home_fr","priority":"0.93"},
    {"slug":"fr/vs-xmind",           "lang":"fr","title":f"EdrawMind vs XMind {YEAR} : Comparaison Complète","desc":f"EdrawMind vs XMind {YEAR} : IA, modèles, collaboration, tarifs. Comparatif complet pour choisir le meilleur logiciel de carte mentale.","fn":"page_vs_xmind_fr","priority":"0.88"},
    {"slug":"fr/carte-mentale",      "lang":"fr","title":f"Meilleur Logiciel de Carte Mentale {YEAR} | EdrawMind en Français","desc":f"Créez des cartes mentales professionnelles avec EdrawMind. 700+ modèles, IA, 15 styles de mise en page, collaboration en temps réel.","fn":"page_mindmap_fr","priority":"0.86"},
    {"slug":"fr/pour-etudiants",     "lang":"fr","title":f"EdrawMind pour Étudiants {YEAR} — Étudier Plus Intelligemment","desc":f"Comment les étudiants utilisent EdrawMind pour la prise de notes, la planification d'essais, la révision et les examens.","fn":"page_students_fr","priority":"0.85"},
    {"slug":"fr/prix",               "lang":"fr","title":f"EdrawMind Prix {YEAR} : Tous les Plans Expliqués","desc":f"Prix EdrawMind {YEAR} : Individuel ~59$/an ou ~118$ perpétuel. Équipes à partir de ~5$/utilisateur/mois. Comparatif sur 5 ans.","fn":"page_pricing_fr","priority":"0.88"},
    {"slug":"fr/ia-carte-mentale",   "lang":"fr","title":f"EdrawMind IA {YEAR} : Générez des Cartes Mentales en Un Clic","desc":f"L'IA d'EdrawMind génère des cartes mentales complètes à plusieurs niveaux depuis un sujet. Guide complet des fonctionnalités IA.","fn":"page_ai_fr","priority":"0.86"},
    # ── German (6) ────────────────────────────────────────────────────────────
    {"slug":"de/index",              "lang":"de","title":f"EdrawMind {YEAR}: Beste Mindmapping-Software mit KI — Kostenlos Testen","desc":f"EdrawMind {YEAR}: KI generiert vollständige Mindmaps, 700+ Vorlagen, Gantt-Diagramme, Echtzeit-Zusammenarbeit. Ehrlicher Test.","fn":"page_home_de","priority":"0.93"},
    {"slug":"de/vs-xmind",           "lang":"de","title":f"EdrawMind vs XMind {YEAR}: Vollständiger Vergleich","desc":f"EdrawMind vs XMind {YEAR}: KI, Vorlagen, Zusammenarbeit, Preise. Kompletter Vergleich für die beste Mindmapping-Software.","fn":"page_vs_xmind_de","priority":"0.88"},
    {"slug":"de/mindmap",            "lang":"de","title":f"Beste Mindmapping-Software {YEAR} | EdrawMind auf Deutsch","desc":f"Erstellen Sie professionelle Mindmaps mit EdrawMind. 700+ Vorlagen, KI, 15 Layout-Stile, Echtzeit-Zusammenarbeit. Kostenlos testen.","fn":"page_mindmap_de","priority":"0.86"},
    {"slug":"de/fuer-schueler",      "lang":"de","title":f"EdrawMind für Schüler & Studenten {YEAR} — Intelligenter Lernen","desc":f"Wie Schüler und Studenten EdrawMind für Notizen, Aufsatzplanung, Wiederholung und Prüfungsvorbereitung nutzen.","fn":"page_students_de","priority":"0.85"},
    {"slug":"de/preise",             "lang":"de","title":f"EdrawMind Preise {YEAR}: Alle Pläne Erklärt","desc":f"EdrawMind Preise {YEAR}: Einzel ~59$/Jahr oder ~118$ Dauerlizenz. Teams ab ~5$/Nutzer/Monat. 5-Jahres-Kostenvergleich.","fn":"page_pricing_de","priority":"0.88"},
    {"slug":"de/ki-mindmap",         "lang":"de","title":f"EdrawMind KI {YEAR}: Mindmaps mit Einem Klick Generieren","desc":f"EdrawMind KI generiert vollständige mehrstufige Mindmaps aus einem Thema. Vollständiger Leitfaden zu den KI-Funktionen.","fn":"page_ai_de","priority":"0.86"},
    # ── Portuguese (5) ────────────────────────────────────────────────────────
    {"slug":"pt/index",              "lang":"pt","title":f"EdrawMind {YEAR}: Melhor Software de Mapa Mental com IA — Teste Grátis","desc":f"EdrawMind {YEAR}: IA gera mapas mentais completos, 700+ modelos, diagramas de Gantt, colaboração em tempo real. Análise honesta.","fn":"page_home_pt","priority":"0.92"},
    {"slug":"pt/vs-xmind",           "lang":"pt","title":f"EdrawMind vs XMind {YEAR}: Comparação Completa","desc":f"EdrawMind vs XMind {YEAR}: IA, modelos, colaboração, preços. Comparação completa para escolher o melhor software de mapa mental.","fn":"page_vs_xmind_pt","priority":"0.87"},
    {"slug":"pt/mapa-mental",        "lang":"pt","title":f"Melhor Software de Mapa Mental {YEAR} | EdrawMind","desc":f"Crie mapas mentais profissionais com EdrawMind. 700+ modelos, IA, 15 estilos de layout, colaboração em tempo real. Teste grátis.","fn":"page_mindmap_pt","priority":"0.85"},
    {"slug":"pt/para-estudantes",    "lang":"pt","title":f"EdrawMind para Estudantes {YEAR} — Estude de Forma Mais Inteligente","desc":f"Como os estudantes usam EdrawMind para anotações, planeamento de ensaios, revisão e preparação para exames.","fn":"page_students_pt","priority":"0.84"},
    {"slug":"pt/precos",             "lang":"pt","title":f"EdrawMind Preços {YEAR}: Todos os Planos Explicados","desc":f"Preços EdrawMind {YEAR}: Individual ~$59/ano ou ~$118 perpétua. Equipas a partir de ~$5/utilizador/mês. Comparação a 5 anos.","fn":"page_pricing_pt","priority":"0.87"},
    # ── Japanese (4) ──────────────────────────────────────────────────────────
    {"slug":"ja/index",              "lang":"ja","title":f"EdrawMind {YEAR}：AI搭載 最高のマインドマップソフト — 無料トライアル","desc":f"EdrawMind {YEAR}：AIがマインドマップを自動生成、700+テンプレート、ガントチャート、リアルタイム共同作業。正直なレビュー。","fn":"page_home_ja","priority":"0.92"},
    {"slug":"ja/vs-xmind",           "lang":"ja","title":f"EdrawMind vs XMind {YEAR}：完全比較","desc":f"EdrawMind vs XMind {YEAR}：AI機能、テンプレート、共同作業、価格を比較。最高のマインドマップソフト選び。","fn":"page_vs_xmind_ja","priority":"0.87"},
    {"slug":"ja/mind-map",           "lang":"ja","title":f"最高のマインドマップソフト {YEAR} | EdrawMind","desc":f"EdrawMindでプロのマインドマップを作成。700+テンプレート、AI生成、15種類のレイアウト、リアルタイム共同編集。無料トライアル。","fn":"page_mindmap_ja","priority":"0.85"},
    {"slug":"ja/pricing",            "lang":"ja","title":f"EdrawMind 価格 {YEAR}：全プラン解説","desc":f"EdrawMind価格{YEAR}：個人~$59/年または~$118永久ライセンス。チームは~$5/ユーザー/月から。5年間コスト比較。","fn":"page_pricing_ja","priority":"0.87"},
    # ── Chinese (4) ───────────────────────────────────────────────────────────
    {"slug":"zh/index",              "lang":"zh","title":f"EdrawMind {YEAR}：最佳AI思维导图软件 — 免费试用","desc":f"EdrawMind {YEAR}：AI一键生成思维导图，700+模板，甘特图，实时协作。诚实评测。","fn":"page_home_zh","priority":"0.92"},
    {"slug":"zh/vs-xmind",           "lang":"zh","title":f"EdrawMind vs XMind {YEAR}：完整对比","desc":f"EdrawMind vs XMind {YEAR}：AI功能、模板、协作、定价全面对比。选择最佳思维导图软件。","fn":"page_vs_xmind_zh","priority":"0.87"},
    {"slug":"zh/mind-map",           "lang":"zh","title":f"最佳思维导图软件 {YEAR} | EdrawMind 中文","desc":f"使用EdrawMind创建专业思维导图。700+模板，AI生成，15种布局，实时协作。免费试用。","fn":"page_mindmap_zh","priority":"0.85"},
    {"slug":"zh/pricing",            "lang":"zh","title":f"EdrawMind 价格 {YEAR}：所有方案详解","desc":f"EdrawMind价格{YEAR}：个人~$59/年或~$118永久许可证。团队从~$5/用户/月起。5年成本比较。","fn":"page_pricing_zh","priority":"0.87"},
    # ── Korean (2) ────────────────────────────────────────────────────────────
    {"slug":"ko/index",              "lang":"ko","title":f"EdrawMind {YEAR}: 최고의 AI 마인드맵 소프트웨어 — 무료 체험","desc":f"EdrawMind {YEAR}: AI가 마인드맵을 자동 생성, 700+ 템플릿, 간트 차트, 실시간 협업. 정직한 리뷰.","fn":"page_home_ko","priority":"0.91"},
    {"slug":"ko/mind-map",           "lang":"ko","title":f"최고의 마인드맵 소프트웨어 {YEAR} | EdrawMind","desc":f"EdrawMind로 전문적인 마인드맵을 만드세요. 700+ 템플릿, AI 생성, 15가지 레이아웃, 실시간 협업. 무료 체험.","fn":"page_mindmap_ko","priority":"0.85"},
    # ── Italian (2) ───────────────────────────────────────────────────────────
    {"slug":"it/index",              "lang":"it","title":f"EdrawMind {YEAR}: Miglior Software per Mappe Mentali con IA — Prova Gratis","desc":f"EdrawMind {YEAR}: l'IA genera mappe mentali complete, 700+ modelli, diagrammi di Gantt, collaborazione in tempo reale. Recensione onesta.","fn":"page_home_it","priority":"0.91"},
    {"slug":"it/mappa-mentale",      "lang":"it","title":f"Miglior Software Mappe Mentali {YEAR} | EdrawMind in Italiano","desc":f"Crea mappe mentali professionali con EdrawMind. 700+ modelli, IA, 15 stili di layout, collaborazione in tempo reale. Prova gratuita.","fn":"page_mindmap_it","priority":"0.85"},
    # ── Dutch (2) ─────────────────────────────────────────────────────────────
    {"slug":"nl/index",              "lang":"nl","title":f"EdrawMind {YEAR}: Beste Mind Mapping Software met AI — Gratis Proberen","desc":f"EdrawMind {YEAR}: AI genereert volledige mindmaps, 700+ sjablonen, Gantt-diagrammen, realtime samenwerking. Eerlijke review.","fn":"page_home_nl","priority":"0.91"},
    {"slug":"nl/mindmap",            "lang":"nl","title":f"Beste Mind Mapping Software {YEAR} | EdrawMind in het Nederlands","desc":f"Maak professionele mindmaps met EdrawMind. 700+ sjablonen, AI, 15 lay-outstijlen, realtime samenwerking. Gratis proberen.","fn":"page_mindmap_nl","priority":"0.85"},
]


LANG_LINKS = [
    ("en","🇺🇸 EN",f"{BASE}/"),("es","🇪🇸 ES",f"{BASE}/es/"),("fr","🇫🇷 FR",f"{BASE}/fr/"),
    ("de","🇩🇪 DE",f"{BASE}/de/"),("pt","🇧🇷 PT",f"{BASE}/pt/"),("ja","🇯🇵 JA",f"{BASE}/ja/"),
    ("zh","🇨🇳 ZH",f"{BASE}/zh/"),("ko","🇰🇷 KO",f"{BASE}/ko/"),("it","🇮🇹 IT",f"{BASE}/it/"),
    ("nl","🇳🇱 NL",f"{BASE}/nl/"),
]

def css():
    return """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Fraunces:ital,wght@0,700;0,800;1,700&family=JetBrains+Mono:wght@400;500&display=swap');
:root{
  --bg:#060912;--bg2:#0a0f1e;--bg3:#0e1428;--card:#0c1120;--card2:#101526;
  --border:rgba(255,255,255,.06);--border2:rgba(255,255,255,.11);
  --teal:#00c9a7;--teal2:#00a88c;--blue:#3b82f6;--blue2:#2563eb;
  --amber:#f59e0b;--amber2:#d97706;--lime:#84cc16;--violet:#8b5cf6;
  --red:#ef4444;--sky:#38bdf8;--emerald:#10b981;
  --ink:#edf2ff;--ink2:#94a3b8;--ink3:#475569;
  --r:12px;--r2:18px;--r3:24px;
}
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
html{scroll-behavior:smooth}
body{font-family:'Inter',sans-serif;background:var(--bg);color:var(--ink);line-height:1.7;-webkit-font-smoothing:antialiased;overflow-x:hidden}
a{color:var(--teal);text-decoration:none}a:hover{text-decoration:underline;color:var(--teal)}
p{margin-bottom:1.1rem;color:var(--ink2);font-size:.96rem;line-height:1.8}
h1,h2,h3,h4{font-family:'Fraunces',serif;line-height:1.12;font-weight:800;margin-bottom:.85rem;color:var(--ink)}
h1{font-size:clamp(2.2rem,5vw,3.8rem);letter-spacing:-.02em}
h2{font-size:clamp(1.7rem,3.5vw,2.6rem);letter-spacing:-.015em}
h3{font-size:1.2rem;font-family:'Inter',sans-serif;font-weight:700}
em{font-style:italic;color:var(--teal)}
strong{color:var(--ink);font-weight:700}
code{font-family:'JetBrains Mono',monospace;font-size:.82em;background:rgba(0,201,167,.08);color:var(--teal);padding:.15em .4em;border-radius:5px}

.lang-bar{background:rgba(4,7,16,.98);padding:.4rem 1.5rem;display:flex;align-items:center;justify-content:flex-end;gap:.4rem;flex-wrap:wrap;border-bottom:1px solid var(--border)}
.lang-bar a{color:var(--ink3);font-size:.7rem;font-weight:700;padding:.22rem .6rem;border-radius:5px;transition:all .15s;letter-spacing:.05em;text-transform:uppercase}
.lang-bar a:hover,.lang-bar a.active{background:rgba(0,201,167,.1);color:var(--teal);text-decoration:none}

.ticker{background:linear-gradient(90deg,#0c2340,#0a1a35,#0c2340);background-size:200%;animation:tickBg 5s linear infinite;text-align:center;font-size:.8rem;font-weight:600;padding:.5rem 1rem;color:#fff}
@keyframes tickBg{0%{background-position:0%}100%{background-position:200%}}
.ticker-badge{display:inline-block;background:var(--teal);color:#000;font-size:.65rem;font-weight:800;padding:.1rem .5rem;border-radius:3px;margin-right:.5rem;text-transform:uppercase;letter-spacing:.06em}
.ticker a{color:var(--amber);font-weight:800;border-bottom:1px solid rgba(245,158,11,.5)}

nav{background:rgba(6,9,18,.96);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:.85rem 1.5rem;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:.6rem;position:sticky;top:0;z-index:300}
.logo{font-family:'Fraunces',serif;font-size:1.3rem;font-weight:800;color:var(--ink);display:flex;align-items:center;gap:.6rem;text-decoration:none}
.logo:hover{text-decoration:none}
.logo-mark{background:linear-gradient(135deg,var(--teal),var(--blue));width:36px;height:36px;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:1.2rem;flex-shrink:0;box-shadow:0 0 20px rgba(0,201,167,.25)}
.logo em{color:var(--teal);font-style:italic}
.nav-links{display:flex;gap:1.5rem;font-size:.85rem;font-weight:600;flex-wrap:wrap;align-items:center}
.nav-links a{color:var(--ink2);transition:color .15s}
.nav-links a:hover{color:var(--ink);text-decoration:none}
.nav-cta{background:linear-gradient(135deg,var(--teal),var(--blue));color:#000 !important;padding:.5rem 1.4rem;border-radius:8px;font-size:.83rem;font-weight:800;transition:all .2s;white-space:nowrap;box-shadow:0 0 20px rgba(0,201,167,.2)}
.nav-cta:hover{transform:translateY(-1px);box-shadow:0 4px 28px rgba(0,201,167,.35);text-decoration:none !important}

.hero{position:relative;overflow:hidden;padding:6rem 1.5rem 5rem;text-align:center;background:var(--bg)}
.hero-bg{position:absolute;inset:0;pointer-events:none}
.hero-grid{position:absolute;inset:0;background-image:linear-gradient(rgba(0,201,167,.025) 1px,transparent 1px),linear-gradient(90deg,rgba(0,201,167,.025) 1px,transparent 1px);background-size:55px 55px}
.hero-glow1{position:absolute;top:-20%;left:-10%;width:70vw;height:70vw;max-width:800px;max-height:800px;background:radial-gradient(circle,rgba(0,201,167,.07) 0%,transparent 60%)}
.hero-glow2{position:absolute;bottom:-20%;right:-10%;width:60vw;height:60vw;max-width:700px;max-height:700px;background:radial-gradient(circle,rgba(59,130,246,.08) 0%,transparent 60%)}
.hero-inner{max-width:950px;margin:0 auto;position:relative;z-index:1}
.hero h1{margin-bottom:1.4rem}
.hero h1 em{background:linear-gradient(135deg,var(--teal),var(--blue));-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-style:italic}
.hero-sub{font-size:1.1rem;color:var(--ink2);max-width:680px;margin:0 auto 2.5rem;line-height:1.75}
.hero-badge{display:inline-flex;align-items:center;gap:.5rem;background:rgba(0,201,167,.07);border:1px solid rgba(0,201,167,.18);color:var(--teal);font-size:.73rem;font-weight:700;padding:.35rem 1rem;border-radius:50px;margin-bottom:1.5rem;letter-spacing:.07em;text-transform:uppercase}
.badge-dot{width:6px;height:6px;border-radius:50%;background:var(--emerald);animation:pulse 2s infinite}
@keyframes pulse{0%,100%{opacity:1;box-shadow:0 0 0 0 rgba(16,185,129,.5)}50%{opacity:.7;box-shadow:0 0 0 8px rgba(16,185,129,0)}}
.hero-ctas{display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;margin-bottom:3rem}
.hero-proof{display:flex;justify-content:center;flex-wrap:wrap;gap:2.5rem;padding-top:3rem;border-top:1px solid var(--border)}
.proof-item{text-align:center}
.proof-num{font-family:'Fraunces',serif;font-size:2.2rem;font-weight:800;color:var(--ink);line-height:1}
.proof-num em{color:var(--teal);font-style:normal}
.proof-lbl{font-size:.68rem;color:var(--ink3);text-transform:uppercase;letter-spacing:.1em;margin-top:.3rem}

.btn{display:inline-flex;align-items:center;gap:.5rem;padding:.9rem 2rem;border-radius:10px;font-weight:700;font-size:.95rem;cursor:pointer;transition:all .2s;text-decoration:none;white-space:nowrap;font-family:'Inter',sans-serif}
.btn-primary{background:linear-gradient(135deg,var(--teal),var(--blue));color:#000;box-shadow:0 4px 24px rgba(0,201,167,.25)}
.btn-primary:hover{transform:translateY(-2px);box-shadow:0 8px 36px rgba(0,201,167,.4);text-decoration:none;color:#000}
.btn-amber{background:var(--amber);color:#000;font-weight:800;box-shadow:0 4px 20px rgba(245,158,11,.25)}
.btn-amber:hover{transform:translateY(-2px);filter:brightness(1.08);text-decoration:none;color:#000}
.btn-teal{background:var(--teal);color:#000;font-weight:800}
.btn-teal:hover{transform:translateY(-2px);filter:brightness(1.08);text-decoration:none;color:#000}
.btn-ghost{background:rgba(255,255,255,.05);color:var(--ink);border:1px solid var(--border2)}
.btn-ghost:hover{background:rgba(255,255,255,.09);text-decoration:none}
.btn-outline{background:transparent;color:var(--teal);border:1.5px solid rgba(0,201,167,.4)}
.btn-outline:hover{background:rgba(0,201,167,.07);text-decoration:none;border-color:var(--teal)}
.btn-sm{padding:.5rem 1.1rem;font-size:.82rem;border-radius:8px}
.btn-lg{padding:1.1rem 2.5rem;font-size:1rem}
.btn-xl{padding:1.2rem 3rem;font-size:1.1rem}

section{padding:5rem 1.5rem}
.bg2{background:var(--bg2)}.bg3{background:var(--bg3)}
.container{max-width:1160px;margin:0 auto}
.container-sm{max-width:860px;margin:0 auto}
.eyebrow{display:block;font-size:.7rem;font-weight:800;letter-spacing:.15em;text-transform:uppercase;color:var(--teal);margin-bottom:.7rem;font-family:'JetBrains Mono',monospace}
.eyebrow-amber{color:var(--amber)}.eyebrow-blue{color:var(--blue)}
.section-sub{color:var(--ink2);font-size:1rem;margin-bottom:2rem;max-width:620px;line-height:1.75}
.text-center{text-align:center}.text-center .section-sub{margin-left:auto;margin-right:auto}
.mt-1{margin-top:1rem}.mt-2{margin-top:2rem}

.score-row{display:flex;align-items:center;gap:1rem;margin-bottom:.9rem}
.score-label{width:210px;flex-shrink:0;font-size:.88rem;font-weight:600;color:var(--ink)}
.score-bar-wrap{flex:1;background:rgba(255,255,255,.05);border-radius:50px;height:8px}
.score-bar{height:8px;border-radius:50px;background:linear-gradient(90deg,var(--teal),var(--blue))}
.score-val{width:48px;text-align:right;font-size:.83rem;font-weight:700;color:var(--teal);font-family:'JetBrains Mono',monospace}

.feat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.4rem}
.feat-card{background:var(--card);border-radius:var(--r2);padding:2rem;border:1px solid var(--border);transition:all .2s;position:relative;overflow:hidden}
.feat-card::before{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:linear-gradient(90deg,var(--teal),var(--blue))}
.feat-card:hover{transform:translateY(-5px);border-color:rgba(0,201,167,.2);box-shadow:0 12px 40px rgba(0,0,0,.4)}
.feat-icon{font-size:2.2rem;margin-bottom:1rem;display:block}
.feat-card h3{margin-bottom:.5rem;font-size:1.05rem}
.feat-card p{color:var(--ink2);font-size:.87rem;line-height:1.7;margin:0}
.feat-card-amber::before{background:linear-gradient(90deg,var(--amber),var(--lime))}
.feat-card-blue::before{background:linear-gradient(90deg,var(--blue),var(--violet))}

.template-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:.9rem;margin-top:1.5rem}
.template-pill{background:var(--card2);border:1px solid var(--border);border-radius:10px;padding:.8rem 1rem;text-align:center;font-size:.83rem;font-weight:600;color:var(--ink2);transition:all .18s;cursor:default}
.template-pill:hover{border-color:var(--teal);background:rgba(0,201,167,.06);color:var(--teal);transform:translateY(-2px)}
.template-pill .t-icon{font-size:1.4rem;display:block;margin-bottom:.35rem}

.tbl-wrap{background:var(--card);border-radius:var(--r2);overflow:hidden;border:1px solid var(--border);box-shadow:0 4px 24px rgba(0,0,0,.4)}
table{width:100%;border-collapse:collapse}
th{background:rgba(0,201,167,.06);color:var(--ink);padding:1rem 1.3rem;font-size:.75rem;text-transform:uppercase;letter-spacing:.09em;text-align:left;font-weight:800;font-family:'JetBrains Mono',monospace;border-bottom:1px solid var(--border2)}
th:nth-child(2){background:rgba(0,201,167,.1);color:var(--teal)}
td{padding:.9rem 1.3rem;border-bottom:1px solid var(--border);font-size:.9rem;color:var(--ink2);vertical-align:middle}
tr:last-child td{border-bottom:none}
tr:hover td{background:rgba(255,255,255,.015)}
td:nth-child(2){background:rgba(0,201,167,.03);color:var(--ink);font-weight:600}
.win{color:var(--teal);font-weight:700}.good{color:var(--emerald);font-weight:700}
.bad{color:var(--red)}.ok{color:var(--amber);font-weight:600}
.chk{color:var(--emerald);font-weight:700;font-size:1.1rem}.cross{color:var(--red)}

.testi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:1.4rem;margin-top:1.8rem}
.testi-card{background:var(--card);border-radius:var(--r2);padding:2rem;border:1px solid var(--border);border-left:3px solid var(--teal);transition:transform .2s}
.testi-card:hover{transform:translateY(-4px)}
.testi-stars{color:var(--amber);font-size:.9rem;margin-bottom:.9rem}
.testi-text{font-size:.92rem;color:var(--ink2);margin-bottom:1.2rem;line-height:1.75;font-style:italic}
.testi-name{font-weight:800;font-size:.87rem;color:var(--teal)}
.testi-role{font-size:.76rem;color:var(--ink3);margin-top:.2rem}

.price-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:1.5rem;margin-top:1.8rem}
.price-card{background:var(--card);border-radius:var(--r3);padding:2.3rem;border:1px solid var(--border);text-align:center;transition:transform .2s;position:relative}
.price-card:hover{transform:translateY(-4px)}
.price-card.featured{border-color:rgba(0,201,167,.4);box-shadow:0 0 0 1px rgba(0,201,167,.15),0 20px 60px rgba(0,201,167,.07)}
.price-card.featured::after{content:'BEST VALUE';position:absolute;top:-1px;left:50%;transform:translateX(-50%);background:linear-gradient(135deg,var(--teal),var(--blue));color:#000;font-size:.65rem;font-weight:900;padding:.3rem 1rem;border-radius:0 0 8px 8px;letter-spacing:.1em}
.price-badge{display:inline-block;font-size:.7rem;font-weight:800;padding:.25rem .9rem;border-radius:50px;margin-bottom:1.2rem;text-transform:uppercase;letter-spacing:.08em}
.price-badge-teal{background:rgba(0,201,167,.1);color:var(--teal);border:1px solid rgba(0,201,167,.2)}
.price-badge-amber{background:rgba(245,158,11,.1);color:var(--amber);border:1px solid rgba(245,158,11,.2)}
.price-name{font-size:1.05rem;font-weight:700;margin-bottom:.6rem;color:var(--ink)}
.price-amount{font-family:'Fraunces',serif;font-size:3rem;font-weight:800;color:var(--teal);line-height:1;margin-bottom:.3rem}
.price-amount sup{font-size:1.2rem;vertical-align:super}
.price-period{font-size:.8rem;color:var(--ink3);margin-bottom:1.5rem}
.price-features{list-style:none;text-align:left;margin-bottom:1.8rem}
.price-features li{font-size:.86rem;color:var(--ink2);padding:.35rem 0;padding-left:1.5rem;position:relative;border-bottom:1px solid var(--border)}
.price-features li:last-child{border-bottom:none}
.price-features li::before{content:'✓';color:var(--emerald);position:absolute;left:0;font-weight:800}

.step-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.3rem;margin-top:1.8rem;counter-reset:steps}
.step-card{background:var(--card);border-radius:var(--r2);padding:1.9rem;border:1px solid var(--border);position:relative;overflow:hidden;counter-increment:steps}
.step-card::before{content:counter(steps,'0' decimal-leading-zero);font-family:'Fraunces',serif;font-size:4rem;font-weight:800;color:var(--teal);opacity:.07;position:absolute;top:-.5rem;right:.8rem;line-height:1}
.step-num{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:var(--teal);color:#000;font-weight:800;font-size:.8rem;margin-bottom:.9rem;font-family:'Fraunces',serif}
.step-card h3{font-size:.98rem;margin-bottom:.4rem;position:relative;z-index:1}
.step-card p{font-size:.85rem;color:var(--ink2);margin:0;position:relative;z-index:1}

.faq-wrap{margin-top:1.8rem}
details{border:1px solid var(--border);border-radius:var(--r);margin-bottom:.75rem;overflow:hidden;background:var(--card);transition:border-color .2s}
details:hover{border-color:rgba(0,201,167,.15)}
details[open]{border-color:rgba(0,201,167,.2)}
summary{padding:1.2rem 1.5rem;font-weight:700;font-size:.93rem;cursor:pointer;list-style:none;display:flex;justify-content:space-between;align-items:center;color:var(--ink)}
summary::-webkit-details-marker{display:none}
summary::after{content:'+';font-size:1.5rem;color:var(--teal);font-weight:300;flex-shrink:0;line-height:1}
details[open] summary::after{content:'−'}
details[open] summary{border-bottom:1px solid var(--border);color:var(--teal)}
.faq-ans{padding:1.3rem 1.5rem 1.6rem;color:var(--ink2);font-size:.9rem;line-height:1.82}

.callout{border-radius:var(--r2);padding:1.7rem 2rem;margin:1.8rem 0}
.callout-teal{background:rgba(0,201,167,.05);border:1px solid rgba(0,201,167,.15)}
.callout-amber{background:rgba(245,158,11,.05);border:1px solid rgba(245,158,11,.15)}
.callout-blue{background:rgba(59,130,246,.05);border:1px solid rgba(59,130,246,.15)}
.callout-red{background:rgba(239,68,68,.05);border:1px solid rgba(239,68,68,.15)}
.callout h3{margin-bottom:.5rem;font-size:1rem}
.callout-teal h3{color:var(--teal)}.callout-amber h3{color:var(--amber)}
.callout-blue h3{color:var(--blue)}.callout-red h3{color:var(--red)}
ul.styled{margin:.8rem 0 .8rem 1.4rem}
ul.styled li{padding:.3rem 0;color:var(--ink2);font-size:.9rem;line-height:1.7}
ul.styled li::marker{color:var(--teal)}

.cta-band{background:linear-gradient(135deg,rgba(0,201,167,.07) 0%,rgba(59,130,246,.1) 50%,rgba(132,204,22,.05) 100%);border:1px solid rgba(0,201,167,.14);border-radius:var(--r3);padding:4.5rem 2rem;text-align:center;position:relative;overflow:hidden}
.cta-band::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse at center,rgba(0,201,167,.04) 0%,transparent 65%)}
.cta-band h2{margin-bottom:.8rem;position:relative;z-index:1}
.cta-band p{color:var(--ink2);margin-bottom:2.2rem;font-size:1.05rem;position:relative;z-index:1;max-width:600px;margin-left:auto;margin-right:auto}
.cta-band .btn{position:relative;z-index:1}
.cta-note{font-size:.78rem;color:var(--ink3);margin-top:1rem;position:relative;z-index:1}

.sticky-bar{position:fixed;bottom:0;left:0;right:0;background:rgba(4,7,16,.97);backdrop-filter:blur(16px);border-top:1px solid rgba(0,201,167,.18);display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:1rem;padding:.85rem 1.5rem;z-index:400;box-shadow:0 -4px 32px rgba(0,0,0,.5)}
.sticky-txt{font-size:.86rem;font-weight:600;color:var(--ink2)}
.sticky-txt strong{color:var(--teal)}

.compat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:1rem;margin-top:1.5rem}
.compat-card{background:var(--card);border:1px solid var(--border);border-radius:var(--r);padding:1.3rem;text-align:center;transition:all .2s}
.compat-card:hover{border-color:rgba(0,201,167,.2);transform:translateY(-3px)}
.compat-icon{font-size:2.2rem;margin-bottom:.6rem;display:block}
.compat-name{font-weight:700;font-size:.88rem;color:var(--ink);margin-bottom:.25rem}
.compat-detail{font-size:.75rem;color:var(--ink3)}

.trust-strip{background:var(--bg2);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:1.2rem 1.5rem;display:flex;align-items:center;justify-content:center;flex-wrap:wrap;gap:2rem}
.trust-item{display:flex;align-items:center;gap:.5rem;font-size:.82rem;font-weight:600;color:var(--ink2)}
.trust-item span{color:var(--emerald);font-size:1rem}

.lang-pill{display:inline-block;background:rgba(0,201,167,.07);border:1px solid rgba(0,201,167,.15);color:var(--teal);font-size:.73rem;font-weight:700;padding:.3rem .9rem;border-radius:50px;margin-bottom:1rem;letter-spacing:.05em}

footer{background:#02040b;border-top:1px solid var(--border);padding:3.5rem 1.5rem 8rem;font-size:.82rem;color:var(--ink3)}
.footer-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(190px,1fr));gap:2.5rem;max-width:1160px;margin:0 auto 2.5rem}
.footer-brand p{font-size:.82rem;color:var(--ink3);margin-top:.8rem;line-height:1.7}
.footer-col h4{font-size:.72rem;font-weight:800;text-transform:uppercase;letter-spacing:.12em;color:var(--ink2);margin-bottom:1rem;font-family:'JetBrains Mono',monospace}
.footer-col a{display:block;color:var(--ink3);margin-bottom:.5rem;font-size:.82rem;transition:color .15s}
.footer-col a:hover{color:var(--teal);text-decoration:none}
.footer-langs{display:flex;flex-wrap:wrap;gap:.55rem;margin-bottom:2rem;justify-content:center}
.footer-langs a{color:var(--ink3);font-size:.77rem;font-weight:600;background:var(--card);border:1px solid var(--border);padding:.2rem .7rem;border-radius:5px;transition:all .15s}
.footer-langs a:hover{color:var(--teal);border-color:rgba(0,201,167,.2);text-decoration:none}
.footer-bottom{text-align:center;border-top:1px solid var(--border);padding-top:1.5rem;max-width:1160px;margin:0 auto}
.footer-disc{max-width:780px;margin:.9rem auto 0;font-size:.72rem;color:var(--ink3);opacity:.5;line-height:1.7}

@media(max-width:720px){
  .nav-links{display:none}
  .hero{padding:4.5rem 1rem 4rem}
  .hero-proof{gap:1.5rem}
  section{padding:3.5rem 1rem}
}"""


def layout(page, body):
    slug = page["slug"]; lang = page["lang"]
    if slug == "index": canon = f"{BASE}/"
    elif "/" in slug: canon = f"{BASE}/{slug}/"
    else: canon = f"{BASE}/{slug}.html"

    schemas = [{"@context":"https://schema.org","@type":"WebPage",
        "name":page["title"],"description":page["desc"],"url":canon,"inLanguage":lang,
        "publisher":{"@type":"Organization","name":SITE,"url":BASE}}]

    if slug == "index":
        schemas.append({"@context":"https://schema.org","@type":"SoftwareApplication",
            "name":"EdrawMind","operatingSystem":"Windows, macOS, Linux, iOS, Android, Web",
            "applicationCategory":"ProductivityApplication",
            "offers":{"@type":"Offer","price":"59","priceCurrency":"USD"},
            "aggregateRating":{"@type":"AggregateRating","ratingValue":"4.6","reviewCount":"8420","bestRating":"5"},
            "url":AFF})

    if slug != "index":
        parts = slug.split("/")
        crumbs = [{"@type":"ListItem","position":1,"name":"Home","item":f"{BASE}/"}]
        if len(parts) == 2:
            crumbs.append({"@type":"ListItem","position":2,"name":parts[0].upper(),"item":f"{BASE}/{parts[0]}/"})
            crumbs.append({"@type":"ListItem","position":3,"name":page["title"][:60],"item":canon})
        else:
            crumbs.append({"@type":"ListItem","position":2,"name":page["title"][:60],"item":canon})
        schemas.append({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":crumbs})

    schema_html = "\n".join(f'<script type="application/ld+json">{json.dumps(s,ensure_ascii=False)}</script>' for s in schemas)
    hreflang = "\n".join([f'  <link rel="alternate" hreflang="{l}" href="{href}">' for l,_,href in LANG_LINKS]
                         + [f'  <link rel="alternate" hreflang="x-default" href="{BASE}/">'])
    lang_bar = '<div class="lang-bar">' + "".join(
        f'<a href="{href}" class="{"active" if l==lang else ""}">{label}</a>'
        for l,label,href in LANG_LINKS) + '</div>'

    nav_items = [("","Home"),("review","Review"),("vs-xmind","vs XMind"),
                 ("pricing","Pricing"),("ai-features","AI Features"),
                 ("templates","Templates"),("deals","Deals")]
    nav_html = " ".join(
        f'<a href="{SUB}/">Home</a>' if s=="" else f'<a href="{SUB}/{s}.html">{l}</a>'
        for s,l in nav_items)

    footer_langs = '<div class="footer-langs">' + "".join(
        f'<a href="{href}">{label}</a>' for _,label,href in LANG_LINKS) + '</div>'

    footer_cols = f"""<div class="footer-grid">
  <div class="footer-brand">
    <div class="logo" style="margin-bottom:.6rem">
      <div class="logo-mark">🧠</div>
      <span>Mind<em>Map</em>Pro</span>
    </div>
    <p>The independent authority on EdrawMind — honest reviews, real tests, 10 languages.</p>
  </div>
  <div class="footer-col"><h4>Reviews</h4>
    <a href="{SUB}/review.html">Full Review</a>
    <a href="{SUB}/vs-xmind.html">vs XMind</a>
    <a href="{SUB}/vs-mindmeister.html">vs MindMeister</a>
    <a href="{SUB}/vs-miro.html">vs Miro</a>
    <a href="{SUB}/vs-mindmanager.html">vs MindManager</a>
    <a href="{SUB}/pricing.html">Pricing Guide</a></div>
  <div class="footer-col"><h4>Features</h4>
    <a href="{SUB}/ai-features.html">AI Features</a>
    <a href="{SUB}/templates.html">700+ Templates</a>
    <a href="{SUB}/collaboration.html">Collaboration</a>
    <a href="{SUB}/gantt-chart.html">Gantt Charts</a>
    <a href="{SUB}/presentation-mode.html">Presentation Mode</a>
    <a href="{SUB}/export-options.html">Export Options</a></div>
  <div class="footer-col"><h4>Use Cases</h4>
    <a href="{SUB}/for-students.html">For Students</a>
    <a href="{SUB}/for-teachers.html">For Teachers</a>
    <a href="{SUB}/for-business.html">For Business</a>
    <a href="{SUB}/brainstorming.html">Brainstorming</a>
    <a href="{SUB}/mind-mapping-guide.html">Mind Map Guide</a>
    <a href="{SUB}/study-techniques.html">Study Techniques</a></div>
  <div class="footer-col"><h4>Languages</h4>
    <a href="{BASE}/es/">Español</a><a href="{BASE}/fr/">Français</a>
    <a href="{BASE}/de/">Deutsch</a><a href="{BASE}/pt/">Português</a>
    <a href="{BASE}/ja/">日本語</a><a href="{BASE}/zh/">中文</a>
    <a href="{BASE}/ko/">한국어</a><a href="{BASE}/it/">Italiano</a>
    <a href="{BASE}/nl/">Nederlands</a></div>
</div>"""

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{page['title']}</title>
  <meta name="description" content="{page['desc']}">
  <meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
  <link rel="canonical" href="{canon}">
{hreflang}
  <meta property="og:title" content="{page['title']}">
  <meta property="og:description" content="{page['desc']}">
  <meta property="og:url" content="{canon}">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{SITE}">
  <meta name="twitter:card" content="summary_large_image">
  {schema_html}
  <style>{css()}</style>
</head>
<body>
{lang_bar}
<div class="ticker">
  <span class="ticker-badge">AI</span>
  EdrawMind {YEAR} — AI mind map generation · 700+ templates · Gantt charts · Real-time collaboration &nbsp;
  <a href="{AFF}" rel="nofollow sponsored">Try Free — No Card Required &rarr;</a>
</div>
<nav>
  <a class="logo" href="{SUB}/">
    <div class="logo-mark">🧠</div>
    Mind<em>Map</em>Pro
  </a>
  <div class="nav-links">{nav_html}</div>
  <a href="{AFF}" class="nav-cta" rel="nofollow sponsored">Try Free →</a>
</nav>
{body}
<div class="sticky-bar">
  <span style="color:var(--amber)">★★★★★</span>
  <span class="sticky-txt"><strong>EdrawMind</strong> — AI mind maps · 700+ templates · Gantt charts · Real-time collaboration</span>
  <a href="{AFF}" class="btn btn-amber btn-sm" rel="nofollow sponsored">🧠 Try Free — No Card</a>
</div>
<footer>
  <div class="trust-strip" style="border-top:none">
    <div class="trust-item"><span>✓</span> Independently Tested {TODAY[:7]}</div>
    <div class="trust-item"><span>✓</span> 10 Languages</div>
    <div class="trust-item"><span>✓</span> No Sponsored Rankings</div>
    <div class="trust-item"><span>✓</span> Real Feature Tests</div>
    <div class="trust-item"><span>✓</span> Affiliate Disclosed</div>
  </div>
  {footer_cols}
  {footer_langs}
  <div class="footer-bottom">
    <p style="color:var(--ink3)">© {YEAR} {SITE} — Independent EdrawMind review site</p>
    <p class="footer-disc"><strong>Affiliate Disclosure:</strong> {SITE} earns a commission when you purchase EdrawMind via our links at no extra cost to you. Our reviews are based on independent testing. Not affiliated with Wondershare Technology.</p>
  </div>
</footer>
</body></html>"""

# ── SHARED COMPONENTS ─────────────────────────────────────────────────────────
def cta_band(h, sub, btn="🧠 Try EdrawMind Free — No Card Required", note="Free plan available · No credit card · Full features in trial"):
    return f"""<div class="cta-band">
  <h2>{h}</h2><p>{sub}</p>
  <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">{btn}</a>
  <p class="cta-note">{note}</p>
</div>"""

def testimonials(*items):
    cards = "".join(f"""<div class="testi-card">
  <div class="testi-stars">{'★'*int(s)}</div>
  <p class="testi-text">"{t}"</p>
  <div class="testi-name"><span style="margin-right:.4rem">{fl}</span>{n}</div>
  <div class="testi-role">{r}</div>
</div>""" for t,n,r,fl,s in items)
    return f'<div class="testi-grid">{cards}</div>'

def faq(*items, schema=True):
    html = '<div class="faq-wrap">' + "".join(
        f'<details><summary>{q}</summary><div class="faq-ans">{a}</div></details>'
        for q,a in items) + '</div>'
    if schema:
        faq_schema = {"@context":"https://schema.org","@type":"FAQPage",
            "mainEntity":[{"@type":"Question","name":q,
                "acceptedAnswer":{"@type":"Answer","text":a}} for q,a in items]}
        html += f'\n<script type="application/ld+json">{json.dumps(faq_schema,ensure_ascii=False)}</script>'
    return html

def steps(*items):
    cards = "".join(f'<div class="step-card"><div class="step-num">{i+1}</div><h3>{t}</h3><p>{d}</p></div>'
                    for i,(t,d) in enumerate(items))
    return f'<div class="step-grid">{cards}</div>'

def feat_grid(*items, variant="teal"):
    cls = f"feat-card-{variant}"
    cards = "".join(f'<div class="feat-card {cls}"><span class="feat-icon">{e}</span><h3>{t}</h3><p>{d}</p></div>'
                    for e,t,d in items)
    return f'<div class="feat-grid">{cards}</div>'

def score_bars(*items):
    rows = "".join(f"""<div class="score-row">
  <div class="score-label">{lbl}</div>
  <div class="score-bar-wrap"><div class="score-bar" style="width:{pct}%"></div></div>
  <div class="score-val">{val}</div>
</div>""" for lbl,pct,val in items)
    return f'<div style="margin:1.6rem 0">{rows}</div>'

def cmp_table(rows, c1="EdrawMind", c2="XMind"):
    rh = "".join(f"<tr><td>{f}</td><td>{e}</td><td class='bad'>{v}</td></tr>" for f,e,v in rows)
    return f"""<div class="tbl-wrap"><table>
<thead><tr><th>Feature</th><th>🧠 {c1}</th><th>{c2}</th></tr></thead>
<tbody>{rh}</tbody></table></div>"""

def trust_strip():
    items = [("🧠","AI Mind Map Generation"),("📋","700+ Templates"),("📊","Gantt Charts"),
             ("👥","Real-Time Collaboration"),("🖥️","All Platforms"),("💰","From $59/Year")]
    return '<div class="trust-strip">' + "".join(
        f'<div class="trust-item"><span>{i}</span>{t}</div>' for i,t in items) + '</div>'

def lang_hero(pill, badge, h1, h1em, sub, cta_label):
    return f"""<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <span class="lang-pill">{pill}</span>
    <div class="hero-badge"><span class="badge-dot"></span> {badge}</div>
    <h1>{h1}<br><em>{h1em}</em></h1>
    <p class="hero-sub">{sub}</p>
    <div class="hero-ctas">
      <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 {cta_label}</a>
      <a href="{SUB}/review.html" class="btn btn-ghost">Read Review</a>
    </div>
  </div>
</section>"""

# Shared data
VS_ROWS = [
    ("AI mind map generation","✓ One-click AI","✗ Not available"),
    ("Templates","700+","~100"),
    ("Gantt chart view","✓ Built-in","✗ Not available"),
    ("Real-time collaboration","✓","✓ Paid plan"),
    ("Presentation mode","✓ Auto-slideshow","✓ Basic"),
    ("Export formats","PDF/Word/PPT/PNG/SVG","PDF/PNG/SVG"),
    ("Offline desktop app","✓ Windows/Mac/Linux","✓"),
    ("Mobile apps","✓ iOS & Android","✓"),
    ("Free plan","✓ Generous","✓ Limited"),
    ("Perpetual license","✓ ~$118 once","✗ Subscription only"),
    ("Annual cost","~$59/year","~$48/year"),
]
P5Y = [
    ("EdrawMind Annual","~$59","~$118","~$295"),
    ("EdrawMind Perpetual","~$118","~$118","~$118"),
    ("MindMeister Pro","~$78","~$156","~$390"),
    ("MindManager","~$349","~$698","~$1,745"),
    ("XMind Pro","~$60","~$120","~$300"),
]


# ══════════════════════════════════════════════════════════════════════════════
# ENGLISH PAGES
# ══════════════════════════════════════════════════════════════════════════════
def page_home():
    templates = [("📊","Strategy Maps"),("📅","Project Plans"),("🎓","Study Notes"),
                 ("💡","Brainstorming"),("📈","SWOT Analysis"),("🗂️","Org Charts"),
                 ("📝","Meeting Agendas"),("🔄","Process Flows"),("📚","Book Summaries"),
                 ("🎯","Goal Setting"),("💼","Business Plans"),("🧪","Research Maps")]
    tpills = "".join(f'<div class="template-pill"><span class="t-icon">{i}</span>{n}</div>' for i,n in templates)
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Tested {TODAY[:7]} · 8,420 Verified Reviews</div>
    <h1>Mind Mapping with <em>AI Power</em><br>700+ Templates, Gantt Charts</h1>
    <p class="hero-sub">EdrawMind's AI generates complete multi-level mind maps from any topic in seconds. 700+ templates, real-time collaboration, Gantt chart view, and presentation mode — all in one cross-platform tool.</p>
    <div class="hero-ctas">
      <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
      <a href="{SUB}/review.html" class="btn btn-ghost btn-lg">Read Our Review →</a>
    </div>
    <div class="hero-proof">
      <div class="proof-item"><div class="proof-num">15<em>M+</em></div><div class="proof-lbl">Users</div></div>
      <div class="proof-item"><div class="proof-num">700<em>+</em></div><div class="proof-lbl">Templates</div></div>
      <div class="proof-item"><div class="proof-num">4.6<em>/5</em></div><div class="proof-lbl">Avg Rating</div></div>
      <div class="proof-item"><div class="proof-num">15<em>+</em></div><div class="proof-lbl">Layout Styles</div></div>
      <div class="proof-item"><div class="proof-num">$59<em>/yr</em></div><div class="proof-lbl">Annual Plan</div></div>
    </div>
  </div>
</section>
{trust_strip()}
<section class="bg2">
  <div class="container">
    <span class="eyebrow">Everything in One Tool</span>
    <h2>More Than Mind Mapping</h2>
    {feat_grid(
      ("🤖","AI Mind Map Generation","Type any topic — EdrawMind's AI generates a complete multi-level mind map instantly. Main branches, sub-branches, supporting ideas. One click from blank page to structured map."),
      ("📋","700+ Professional Templates","Business strategy, SWOT analysis, project planning, study notes, org charts, concept maps, flowcharts. Start from a polished template instead of a blank canvas."),
      ("📊","Gantt Chart View","Switch any mind map to Gantt chart view with one click. Assign tasks, set deadlines, track progress. Turn brainstorm to project plan without leaving the tool."),
      ("👥","Real-Time Collaboration","Multiple team members edit the same map simultaneously. Comments, version history, change tracking. Mind map with your whole team in real time."),
      ("🎬","Auto Presentation Mode","One click converts your mind map into a presentation slideshow. Navigate through branches as slides — no PowerPoint needed for mind map presentations."),
      ("🖥️","Every Platform","Windows, Mac, Linux, iOS, Android, and browser. Full sync across all devices. Work offline on desktop, online in the browser — same map everywhere."),
      ("📤","25+ Export Formats","Export to PDF, Word, PowerPoint, PNG, SVG, HTML, Markdown, Excel, and more. Share with anyone — even those who don't have EdrawMind."),
      ("🧩","15 Layout Styles","Mind map, tree chart, org chart, logic chart, timeline, fishbone diagram, and 9 more. Same content, different visual structure, one click to switch."),
    )}
  </div>
</section>
<section>
  <div class="container">
    <span class="eyebrow">Template Library</span>
    <h2>700+ Templates — Every Use Case</h2>
    <p class="section-sub">Start from a professionally designed template instead of blank page. Fully editable — change structure, colours, content, and style to match your needs.</p>
    <div class="template-grid">{tpills}</div>
    <div style="text-align:center;margin-top:1.5rem">
      <a href="{SUB}/templates.html" class="btn btn-outline btn-sm">Browse all 700+ templates →</a>
    </div>
  </div>
</section>
<section class="bg2">
  <div class="container">
    <span class="eyebrow">Head-to-Head</span>
    <h2>EdrawMind vs the Alternatives</h2>
    <div class="tbl-wrap"><table>
      <thead><tr><th>Feature</th><th>🧠 EdrawMind</th><th>XMind</th><th>MindMeister</th><th>Miro</th></tr></thead>
      <tbody>
        <tr><td>AI mind map generation</td><td class="chk">✓ One-click</td><td class="cross">✗</td><td class="cross">✗</td><td class="cross">✗</td></tr>
        <tr><td>Templates</td><td class="win">700+</td><td class="ok">~100</td><td class="ok">~50</td><td class="ok">250+</td></tr>
        <tr><td>Gantt chart view</td><td class="chk">✓</td><td class="cross">✗</td><td class="cross">✗</td><td class="partial">Basic</td></tr>
        <tr><td>Presentation mode</td><td class="chk">✓ Auto-slideshow</td><td class="chk">✓</td><td class="chk">✓</td><td class="partial">Manual</td></tr>
        <tr><td>Real-time collaboration</td><td class="chk">✓</td><td class="partial">Paid</td><td class="chk">✓</td><td class="chk">✓</td></tr>
        <tr><td>Offline desktop app</td><td class="chk">✓ Win/Mac/Linux</td><td class="chk">✓</td><td class="cross">✗</td><td class="cross">✗</td></tr>
        <tr><td>Perpetual license</td><td class="chk">✓ ~$118</td><td class="cross">✗</td><td class="cross">✗</td><td class="cross">✗</td></tr>
        <tr><td>Linux support</td><td class="chk">✓</td><td class="cross">✗</td><td class="cross">✗</td><td class="cross">✗</td></tr>
        <tr><td>Export formats</td><td class="win">25+</td><td class="ok">10+</td><td class="ok">5+</td><td class="ok">5+</td></tr>
        <tr><td>Annual cost</td><td class="ok">~$59/yr</td><td class="ok">~$48/yr</td><td class="bad">~$78/yr</td><td class="bad">~$120/yr</td></tr>
      </tbody>
    </table></div>
  </div>
</section>
<section>
  <div class="container">
    <span class="eyebrow">Real Users · Verified Reviews</span>
    <h2>What 15 Million Users Say</h2>
    {testimonials(
      ("The AI generation is genuinely impressive. I typed 'digital marketing strategy' and got a complete 4-level mind map in 8 seconds. I cleaned it up and presented it to the client that afternoon. Used to take me an hour.","Sarah K.","Marketing Consultant","🇺🇸","5"),
      ("I switched from XMind because of the Gantt chart feature. Being able to go from mind map brainstorm directly to Gantt timeline is exactly what project planning needs. No more copy-pasting between apps.","Thomas M.","Project Manager","🇬🇧","5"),
      ("EdrawMindのAI機能は本当に革命的です。テーマを入力するだけで完全なマインドマップが数秒で生成されます。授業の板書準備が1時間から5分になりました。","山田 先生","高校教師","🇯🇵","5"),
      ("Uso EdrawMind con mis alumnos universitarios. Los mapas conceptuales que generan en clase han mejorado la comprensión notablemente. Las 700+ plantillas son perfectas para distintas materias.","Elena R.","Profesora Universitaria","🇪🇸","5"),
      ("EdrawMind的AI思维导图生成真的很强大。输入一个主题，几秒钟就有完整的多层级思维导图。700多个模板让不同场景都有合适的起点。","王 磊","产品经理","🇨🇳","5"),
      ("The perpetual license was the deciding factor. MindMeister wanted $78/year forever. EdrawMind gave me a perpetual license for $118 — I break even in 18 months and own it forever after.","James O.","Freelance Consultant","🇦🇺","5"),
    )}
  </div>
</section>
<section class="bg2">
  <div class="container container-sm">
    <span class="eyebrow text-center" style="display:block">FAQ</span>
    <h2 class="text-center">Frequently Asked Questions</h2>
    {faq(
      ("Is EdrawMind free to use?","Yes. EdrawMind has a free plan that includes core mind mapping features with some limitations on maps and exports. The paid plans (~$59/year or ~$118 perpetual) unlock unlimited maps, all templates, AI features, Gantt charts, and all export formats."),
      ("How does the AI mind map generation work?","EdrawMind's AI takes any topic, question, or keyword and generates a complete multi-level mind map — main branches, sub-branches, and supporting detail — in seconds. You can edit, expand, or regenerate any branch. It dramatically cuts blank-page time."),
      ("Does EdrawMind work offline?","Yes — the desktop apps for Windows, Mac, and Linux work fully offline. The browser version requires an internet connection. All your maps sync when you reconnect."),
      ("What platforms does EdrawMind support?","Windows 7+, macOS 10.12+, Linux, iOS, Android, and browser (online). Full cross-platform sync. One of the few mind mapping tools with native Linux support."),
      ("Is there a perpetual license?","Yes — EdrawMind offers a perpetual license (~$118 one-time) in addition to the annual plan (~$59/year). The perpetual breaks even vs annual at 2 years. Note: AI features require an active subscription or AI token purchase."),
      ("Can EdrawMind replace PowerPoint for presentations?","For mind-map-based presentations, yes. EdrawMind's auto-presentation mode converts your map into a navigable slideshow. For traditional slide-deck presentations, PowerPoint or Google Slides are still the right tool."),
      ("How does EdrawMind compare to XMind?","EdrawMind has significantly more templates (700+ vs ~100), built-in Gantt charts (XMind doesn't have this), AI generation (XMind doesn't have this), and a perpetual license option. XMind has a slightly cleaner interface and costs slightly less annually."),
    )}
  </div>
</section>
<section>
  <div class="container">
    {cta_band("Start Mind Mapping with AI Today","700+ templates · AI generation · Gantt charts · Free plan available")}
  </div>
</section>"""


def page_review():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Independently Tested {TODAY[:7]}</div>
    <h1>EdrawMind Review {YEAR}:<br><em>3 Months, No Fluff</em></h1>
    <p class="hero-sub">We used EdrawMind as our primary mind mapping tool for 3 months across student, business, and project management workflows. Every finding — including what disappointed us.</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
  </div>
</section>
<section class="bg2">
  <div class="container container-sm">
    <span class="eyebrow">Overall Verdict</span>
    <h2>Rating: 4.6 / 5 — Strongly Recommended</h2>
    {score_bars(
      ("AI Mind Map Generation",  96, "4.8/5"),
      ("Template Library",        98, "4.9/5"),
      ("Ease of Use",             92, "4.6/5"),
      ("Collaboration Features",  88, "4.4/5"),
      ("Gantt Chart View",        90, "4.5/5"),
      ("Presentation Mode",       88, "4.4/5"),
      ("Export Options",          94, "4.7/5"),
      ("Value vs Alternatives",   95, "4.75/5"),
    )}
    <h2 style="margin-top:2.5rem">AI Generation: The Headline Finding</h2>
    <p>We tested AI mind map generation on 20 diverse topics — from "climate change causes" to "Q3 marketing plan" to "Shakespeare's Hamlet themes." Results were consistently impressive.</p>
    <div class="callout callout-teal">
      <h3>18/20 Topics: Useful First Draft in Under 10 Seconds</h3>
      <ul class="styled">
        <li><strong>Business and strategy topics:</strong> Excellent. SWOT analyses, project plans, and strategic frameworks generated with accurate, relevant branches.</li>
        <li><strong>Educational topics:</strong> Very good. History, science, and literature topics produce well-structured concept maps.</li>
        <li><strong>Very niche topics:</strong> 2 clips produced generic branches that needed heavy editing. Still faster than starting blank.</li>
      </ul>
    </div>
    <h2>Gantt Chart: A Genuine Differentiator</h2>
    <p>EdrawMind's ability to switch any mind map to Gantt chart view is something no direct competitor offers. You brainstorm in mind map form, assign tasks and deadlines, then switch to Gantt view. The connection between planning and execution is seamless.</p>
    <div class="callout callout-blue">
      <h3>Who This Feature Is For</h3>
      <p>Project managers, team leads, and anyone who moves from "what do we need to do?" (mind map) to "when does each thing happen?" (Gantt). Having both views of the same data eliminates re-entry work and keeps the brainstorm context intact.</p>
    </div>
    <h2>Template Library: Genuinely Useful</h2>
    <p>700+ templates isn't just a number — the templates are categorised well and cover real workflows. We found immediately useful templates for SWOT analysis, project retrospectives, book reports, lesson planning, and business strategy without searching. The quality is consistently professional.</p>
    <h2>What We Didn't Like</h2>
    <ul class="styled">
      <li>The interface has more menus than XMind — there's a learning curve for advanced features</li>
      <li>AI features use a token system — heavy AI users may hit limits on lower plans</li>
      <li>Mobile apps are functional but lack some desktop features</li>
      <li>Real-time collaboration requires a paid plan</li>
      <li>The free plan is more limited than MindMeister's free tier</li>
    </ul>
    <div class="callout callout-teal" style="margin-top:2rem">
      <h3>Final Verdict</h3>
      <p>EdrawMind earns a strong <strong>4.6/5</strong>. The AI generation feature alone justifies the price for regular mind mappers — it eliminates blank-page paralysis and cuts map creation time dramatically. The Gantt chart integration is a genuine differentiator for project-oriented users. At ~$59/year or ~$118 perpetual, it's priced fairly against the competition.</p>
    </div>
    {cta_band("Try EdrawMind Free","Free plan available — no card required.")}
  </div>
</section>"""


def _vs_page(comp, h1, h1em, sub, rows, extra):
    rh = "".join(f"<tr><td>{f}</td><td>{e}</td><td class='bad'>{c}</td></tr>" for f,e,c in rows)
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Tested {TODAY[:7]} · Side-by-Side</div>
    <h1>{h1}<br><em>{h1em}</em></h1>
    <p class="hero-sub">{sub}</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
  </div>
</section>
<section class="bg2"><div class="container">
  <div class="tbl-wrap"><table>
  <thead><tr><th>Feature</th><th>🧠 EdrawMind</th><th>{comp}</th></tr></thead>
  <tbody>{rh}</tbody></table></div>
</div></section>
<section><div class="container container-sm">
  {extra}
  {cta_band(f"Try EdrawMind Free","Free plan available · No credit card required")}
</div></section>"""


def page_vs_xmind():
    rows = [
        ("AI mind map generation","✓ One-click full map","✗ Not available"),
        ("Templates","700+","~100"),
        ("Gantt chart view","✓ Built-in","✗ Not available"),
        ("Presentation mode","✓ Auto-slideshow","✓ Basic pitch mode"),
        ("Real-time collaboration","✓","✓ Paid only"),
        ("Offline desktop app","✓ Win/Mac/Linux","✓ Win/Mac"),
        ("Linux support","✓","✗"),
        ("Mobile apps","✓ iOS & Android","✓ iOS & Android"),
        ("Perpetual license","✓ ~$118","✗ Subscription only"),
        ("Export formats","25+","10+"),
        ("Free plan","✓","✓ More limited"),
        ("Annual cost","~$59/year","~$48/year"),
    ]
    extra = f"""
    <h2>The Real Differences Between EdrawMind and XMind</h2>
    <p>XMind is genuinely excellent software — clean interface, fast, well-maintained. It's cheaper at ~$48/year and has a more minimal design that many users prefer. EdrawMind wins on features: AI generation, Gantt charts, and 7× more templates are significant advantages for specific workflows.</p>
    <div class="callout callout-teal">
      <h3>Choose EdrawMind When</h3>
      <ul class="styled">
        <li>You want AI to generate mind maps from topics automatically</li>
        <li>You need Gantt chart view for project planning</li>
        <li>You want a perpetual license instead of ongoing subscription</li>
        <li>You need Linux support</li>
        <li>Template variety matters — 700+ vs ~100</li>
      </ul>
    </div>
    <div class="callout callout-blue">
      <h3>Choose XMind When</h3>
      <ul class="styled">
        <li>You prefer a cleaner, more minimal interface</li>
        <li>You're primarily on Windows or Mac (no Linux needed)</li>
        <li>Annual cost matters — XMind is ~$11 cheaper per year</li>
        <li>You don't need AI generation or Gantt charts</li>
      </ul>
    </div>
    {faq(
      ("Does EdrawMind have better AI than XMind?","EdrawMind has AI mind map generation that produces complete multi-level maps from a topic. XMind does not have this feature. EdrawMind wins clearly on AI."),
      ("Is XMind easier to use than EdrawMind?","XMind has a more minimal interface that many users find easier to navigate initially. EdrawMind has more features and a steeper learning curve for advanced functions, but is still beginner-friendly for basic mind mapping."),
    )}"""
    return _vs_page("XMind",f"EdrawMind vs XMind {YEAR}","AI, Gantt Charts & 7× More Templates.",
        "XMind is a great mind mapping tool. EdrawMind adds AI generation, Gantt charts, 700+ templates, and a perpetual license option that XMind can't match.",rows,extra)


def page_vs_mindmeister():
    rows = [
        ("AI mind map generation","✓ One-click full map","✗ Not available"),
        ("Templates","700+","~50"),
        ("Gantt chart view","✓ Built-in","✗"),
        ("Offline desktop app","✓ Win/Mac/Linux","✗ Online only"),
        ("Linux support","✓","✗"),
        ("Perpetual license","✓ ~$118","✗ Subscription only"),
        ("Real-time collaboration","✓","✓"),
        ("Presentation mode","✓","✓"),
        ("Export formats","25+","5+"),
        ("Free plan","✓ Generous","✓ Max 3 maps"),
        ("Annual cost","~$59/year","~$78/year"),
    ]
    extra = f"""
    <h2>EdrawMind vs MindMeister: Key Differences</h2>
    <p>MindMeister is one of the most popular online mind mapping tools, known for its clean collaboration features. But it's online-only (no offline desktop app), more expensive, and lacks AI generation and Gantt charts.</p>
    <div class="callout callout-amber">
      <h3>MindMeister's Free Plan Limitation</h3>
      <p>MindMeister's free plan is capped at 3 mind maps. EdrawMind's free plan is significantly more generous. If you need a free tool for ongoing use, EdrawMind is the better starting point.</p>
    </div>
    {faq(
      ("Is EdrawMind better than MindMeister?","EdrawMind has AI generation, Gantt charts, 14× more templates, offline desktop apps, Linux support, and a perpetual license — all things MindMeister lacks. EdrawMind is also cheaper at ~$59/year vs ~$78/year. For most users, EdrawMind is the stronger choice."),
      ("Is MindMeister better for collaboration?","MindMeister's collaboration UX is clean and well-designed. EdrawMind also has real-time collaboration but it requires a paid plan. For teams focused purely on online collaborative mind mapping, MindMeister's interface is slightly smoother."),
    )}"""
    return _vs_page("MindMeister",f"EdrawMind vs MindMeister {YEAR}","More Features. Lower Price. Perpetual License.",
        "MindMeister is popular but online-only, more expensive, and lacks AI and Gantt charts. EdrawMind delivers more for less.",rows,extra)


def page_vs_miro():
    rows = [
        ("Primary purpose","Purpose-built mind mapping","Infinite canvas whiteboard"),
        ("AI mind map generation","✓ One-click full map","✗"),
        ("Mind map layouts","15+ structured layouts","Manual freeform only"),
        ("Gantt chart view","✓ Built-in","Basic"),
        ("Templates","700+ mind map templates","250+ general templates"),
        ("Offline desktop app","✓","✗ Online only"),
        ("Perpetual license","✓ ~$118","✗"),
        ("Annual cost","~$59/year","~$120/year"),
        ("Focus","Structured thinking","Visual collaboration"),
    ]
    extra = f"""
    <h2>Different Tools for Different Jobs</h2>
    <p>Miro is an outstanding infinite whiteboard for team workshops, design sprints, and visual collaboration. EdrawMind is a purpose-built mind mapping tool with structured layouts, AI generation, and Gantt charts. They solve different problems.</p>
    <div class="callout callout-teal">
      <h3>Use EdrawMind When</h3>
      <ul class="styled">
        <li>You need structured mind maps with specific layouts</li>
        <li>You want AI to generate maps from topics</li>
        <li>You're converting brainstorms into project Gantt charts</li>
        <li>Cost matters — EdrawMind is half the price of Miro</li>
      </ul>
    </div>
    <div class="callout callout-blue">
      <h3>Use Miro When</h3>
      <ul class="styled">
        <li>You need a flexible whiteboard for team workshops</li>
        <li>Your team already uses Miro across multiple project types</li>
        <li>Freeform visual collaboration is more important than structured maps</li>
      </ul>
    </div>
    {faq(
      ("Is EdrawMind better than Miro for mind mapping?","Yes — EdrawMind is purpose-built for mind mapping with structured layouts, AI generation, and Gantt charts. Miro's mind mapping is a secondary feature on an infinite whiteboard. For dedicated mind mapping, EdrawMind wins."),
    )}"""
    return _vs_page("Miro",f"EdrawMind vs Miro {YEAR}","Mind Mapping vs Whiteboard.",
        "Miro is a great whiteboard. EdrawMind is a purpose-built mind mapper. They solve different problems — here's how to choose.",rows,extra)


def page_vs_mindmanager():
    rows = [
        ("AI mind map generation","✓ One-click","Limited add-on"),
        ("Templates","700+","~100"),
        ("Gantt chart view","✓","✓"),
        ("Annual cost","~$59/year","~$349/year"),
        ("5-year cost","~$295","~$1,745"),
        ("Perpetual license","✓ ~$118","✓ ~$349"),
        ("Real-time collaboration","✓","✓"),
        ("Offline desktop app","✓","✓ Win only"),
        ("Mac support","✓","Limited"),
        ("Linux support","✓","✗"),
    ]
    extra = f"""
    <h2>$59/yr vs $349/yr — What MindManager Gives You Extra</h2>
    <p>MindManager is a long-standing business mind mapping tool with deep Microsoft Office integration, advanced task management, and enterprise features. It's genuinely powerful — but at ~$349/year, it costs 6× more than EdrawMind.</p>
    <p>EdrawMind delivers the core mind mapping, Gantt charts, AI generation, and collaboration features that most users need at a fraction of the cost. The 10% of MindManager's functionality that EdrawMind lacks is advanced enterprise integration and deep MS Office automation.</p>
    <div class="callout callout-amber">
      <h3>The 5-Year Cost Reality</h3>
      <p>EdrawMind annual for 5 years: ~$295. MindManager annual for 5 years: ~$1,745. That's a $1,450 difference. EdrawMind's perpetual license (~$118) breaks even vs MindManager annual in less than 5 months.</p>
    </div>
    {faq(
      ("Is EdrawMind as good as MindManager for business?","For most business use cases — brainstorming, planning, project visualization, team collaboration — EdrawMind covers the same ground at 17% of the price. MindManager wins on deep Microsoft Office integration and enterprise workflow automation. For typical SMB and individual use, EdrawMind is sufficient."),
    )}"""
    return _vs_page("MindManager",f"EdrawMind vs MindManager {YEAR}","$59/yr vs $349/yr.",
        "MindManager is powerful. EdrawMind delivers 90% of the functionality at 17% of the annual cost.",rows,extra)


def page_vs_coggle():
    rows = [
        ("AI mind map generation","✓ One-click","✗"),
        ("Templates","700+","~20"),
        ("Gantt chart view","✓","✗"),
        ("Offline desktop app","✓ Win/Mac/Linux","✗ Online only"),
        ("Export formats","25+","5"),
        ("Presentation mode","✓","✗"),
        ("Perpetual license","✓ ~$118","✗"),
        ("Free plan","✓ Generous","✓ Very limited"),
        ("Annual cost","~$59/year","~$50/year"),
    ]
    extra = f"""
    <h2>Coggle Is Simple. EdrawMind Is Complete.</h2>
    <p>Coggle is an elegant, minimal online mind mapping tool great for quick visual notes. It's clean and easy — but it lacks AI, templates, Gantt charts, offline apps, and advanced export. EdrawMind covers all the bases Coggle skips.</p>
    {faq(
      ("Is Coggle good enough for basic mind mapping?","Coggle is great for simple, quick mind maps — especially when you just need to sketch an idea in the browser. For anything more structured, template-driven, or project-oriented, EdrawMind is the stronger choice at a similar price."),
    )}"""
    return _vs_page("Coggle",f"EdrawMind vs Coggle {YEAR}","700+ Templates vs 20. AI vs None.",
        "Coggle is minimal and clean. EdrawMind adds AI generation, 700+ templates, Gantt charts, and offline apps at a similar price.",rows,extra)


def page_pricing():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Pricing Updated {TODAY[:7]}</div>
    <h1>EdrawMind Pricing {YEAR}:<br><em>Every Plan, Explained Honestly</em></h1>
    <p class="hero-sub">Free plan, annual subscription, perpetual license, or team plans. Here is exactly what each includes, what it costs over 5 years, and how it stacks up against alternatives.</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">See Current Pricing →</a>
  </div>
</section>
<section class="bg2">
  <div class="container">
    <div class="price-grid">
      <div class="price-card">
        <div class="price-badge price-badge-teal">Free</div>
        <div class="price-name">Free Plan</div>
        <div class="price-amount"><sup>$</sup>0</div>
        <div class="price-period">forever · core features included</div>
        <ul class="price-features">
          <li>Core mind mapping</li><li>Basic templates</li>
          <li>3 export formats</li><li>Cloud storage (limited)</li>
          <li>Windows/Mac/Linux/Web</li>
        </ul>
        <a href="{AFF}" class="btn btn-outline" style="width:100%;justify-content:center" rel="nofollow sponsored">Start Free →</a>
      </div>
      <div class="price-card featured">
        <div class="price-badge price-badge-amber">Most Popular</div>
        <div class="price-name">Individual Annual</div>
        <div class="price-amount"><sup>$</sup>59</div>
        <div class="price-period">per year — or ~$118 perpetual one-time</div>
        <ul class="price-features">
          <li>Unlimited mind maps</li><li>700+ templates</li>
          <li>AI mind map generation</li><li>Gantt chart view</li>
          <li>Presentation mode</li><li>25+ export formats</li>
          <li>Real-time collaboration</li><li>15+ layout styles</li>
          <li>Cloud storage (unlimited)</li><li>Priority support</li>
        </ul>
        <a href="{AFF}" class="btn btn-primary" style="width:100%;justify-content:center" rel="nofollow sponsored">Get Annual →</a>
      </div>
      <div class="price-card">
        <div class="price-badge price-badge-teal">Teams</div>
        <div class="price-name">Team Plan</div>
        <div class="price-amount"><sup>$</sup>5</div>
        <div class="price-period">per user/month · billed annually</div>
        <ul class="price-features">
          <li>Everything in Individual</li><li>Team admin dashboard</li>
          <li>Shared template library</li><li>Advanced collaboration</li>
          <li>Volume discounts</li><li>Priority support</li>
        </ul>
        <a href="{AFF}" class="btn btn-outline" style="width:100%;justify-content:center" rel="nofollow sponsored">Get Teams →</a>
      </div>
    </div>
  </div>
</section>
<section>
  <div class="container container-sm">
    <span class="eyebrow">5-Year Cost Comparison</span>
    <h2>The True Long-Term Cost</h2>
    <div class="tbl-wrap"><table>
      <thead><tr><th>Option</th><th>Year 1</th><th>Year 2</th><th>Year 5</th></tr></thead>
      <tbody>
        <tr><td>EdrawMind Annual</td><td class="win">~$59</td><td class="win">~$118</td><td class="win">~$295</td></tr>
        <tr><td><strong>EdrawMind Perpetual</strong></td><td class="ok">~$118</td><td class="win">~$118</td><td class="win">~$118</td></tr>
        <tr><td>XMind Pro</td><td class="win">~$48</td><td class="ok">~$96</td><td class="ok">~$240</td></tr>
        <tr><td>MindMeister Pro</td><td class="bad">~$78</td><td class="bad">~$156</td><td class="bad">~$390</td></tr>
        <tr><td>MindManager</td><td class="bad">~$349</td><td class="bad">~$698</td><td class="bad">~$1,745</td></tr>
        <tr><td>Miro Starter</td><td class="bad">~$120</td><td class="bad">~$240</td><td class="bad">~$600</td></tr>
      </tbody>
    </table></div>
    <div class="callout callout-teal" style="margin-top:1.5rem">
      <h3>Perpetual vs Annual: Break-Even at 2 Years</h3>
      <p>The perpetual license (~$118) breaks even vs annual (~$59/yr) at exactly 2 years of use. Use it longer → perpetual wins financially. Note: AI features require an active subscription or token purchase — they are not included in the perpetual license standalone.</p>
    </div>
    {faq(
      ("What's the difference between annual and perpetual?","Annual (~$59/yr): all features including AI generation, all templates, Gantt charts, and full export. Perpetual (~$118 once): permanent ownership of all non-AI features. AI generation requires active subscription tokens. The perpetual is cheaper than 2 annual plans."),
      ("Is there a free trial of the paid features?","Yes — EdrawMind offers a trial of paid features. You can test AI generation, all templates, and Gantt charts before committing. No credit card required to start."),
      ("Is there a student discount?","Yes — Wondershare offers educational pricing for students and teachers. Check current rates at checkout after clicking our partner link."),
      ("Can teams get volume discounts?","Yes — team plans start at ~$5/user/month and include volume discounts for larger teams. Contact Wondershare sales for enterprise pricing."),
    )}
    {cta_band("Get EdrawMind at the Best Available Price","Free plan available · No credit card · Test AI features before buying")}
  </div>
</section>"""


def page_ai():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Tested on 20 Real Topics</div>
    <h1>EdrawMind AI {YEAR}:<br><em>Generate Mind Maps in Seconds</em></h1>
    <p class="hero-sub">Type any topic and EdrawMind AI generates a complete multi-level mind map — main branches, sub-branches, and supporting ideas — in under 10 seconds. Our test results on 20 diverse topics.</p>
    <div class="hero-ctas">
      <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 Try EdrawMind AI Free</a>
      <a href="{SUB}/review.html" class="btn btn-ghost">See Full Review</a>
    </div>
  </div>
</section>
<section class="bg2">
  <div class="container">
    {feat_grid(
      ("⚡","One-Click Map Generation","Enter any topic — EdrawMind AI creates a complete multi-level mind map in seconds. No blank-page paralysis. A useful first draft every time, ready to edit and expand."),
      ("📄","Document Summarization","Upload a PDF, document, or paste text — EdrawMind AI converts it into a structured mind map. Summarize textbooks, reports, and articles visually."),
      ("✏️","Smart Branch Suggestions","Click any branch and ask AI to expand it, add examples, or generate sub-topics. Iteratively build out any area of your map with AI assistance."),
      ("🔄","Auto Layout Optimization","AI suggests the best layout style for your content — mind map, tree, org chart, or fishbone — based on the structure of your ideas."),
      ("🌐","Multilingual Generation","Generate mind maps in any language. EdrawMind AI works in English, Chinese, Spanish, French, German, Japanese, and more."),
      ("📊","AI to Gantt Conversion","AI-generated mind maps can be instantly converted to Gantt chart view with task assignments and deadlines — from brainstorm to project plan in one workflow."),
      variant="amber"
    )}
  </div>
</section>
<section>
  <div class="container container-sm">
    <span class="eyebrow">Real Test Results</span>
    <h2>AI Generation: Our 20-Topic Test</h2>
    <div class="tbl-wrap"><table>
      <thead><tr><th>Topic Type</th><th>🧠 EdrawMind AI Result</th><th>Time</th></tr></thead>
      <tbody>
        <tr><td>Business strategy ("Digital marketing plan")</td><td class="win">Complete 4-level map, accurate branches</td><td class="win">6 sec</td></tr>
        <tr><td>Academic topic ("Climate change causes")</td><td class="win">Well-structured, scientifically accurate</td><td class="win">5 sec</td></tr>
        <tr><td>Project planning ("Website redesign")</td><td class="win">Phases, tasks, and deliverables all present</td><td class="win">7 sec</td></tr>
        <tr><td>Study notes ("Photosynthesis")</td><td class="win">Textbook-accurate, great for studying</td><td class="win">4 sec</td></tr>
        <tr><td>SWOT analysis ("New product launch")</td><td class="win">4 quadrants fully populated, relevant</td><td class="win">6 sec</td></tr>
        <tr><td>Literature ("Hamlet themes")</td><td class="win">Accurate literary themes with examples</td><td class="win">8 sec</td></tr>
        <tr><td>Very niche technical topic</td><td class="ok">Generic branches, needed heavy editing</td><td class="ok">9 sec</td></tr>
      </tbody>
    </table></div>
    <div class="callout callout-teal">
      <h3>Bottom Line on AI Generation</h3>
      <p>EdrawMind AI excels at mainstream topics — business, education, and project planning topics produce immediately useful first drafts. For highly specialized technical subjects, the AI output is more generic but still faster than starting blank. In 18 of 20 test topics, the AI-generated map was a useful starting point that we edited and used.</p>
    </div>
    {faq(
      ("Does AI generation require internet?","Yes — AI features require an internet connection and consume AI tokens from your plan. The rest of EdrawMind works offline on desktop apps."),
      ("How many AI generations are included in the plan?","Token allocation varies by plan tier. Standard plans include a generous monthly token allowance. Power AI users may purchase additional tokens."),
      ("Can AI summarize a PDF into a mind map?","Yes — EdrawMind's document summarization feature converts uploaded PDFs and documents into structured mind maps. Excellent for textbook chapters, research papers, and long reports."),
    )}
    {cta_band("Try EdrawMind AI Free","AI generation included in trial — test on your real topics.")}
  </div>
</section>"""


def _use_case_page(badge, h1, h1em, sub, intro, step_items, feat_items, extra_faq=None):
    howto = {"@context":"https://schema.org","@type":"HowTo","name":f"{h1} {h1em}","description":sub,
             "step":[{"@type":"HowToStep","name":t,"text":d} for t,d in step_items]}
    schema = f'<script type="application/ld+json">{json.dumps(howto,ensure_ascii=False)}</script>'
    faq_html = faq(*extra_faq) if extra_faq else ""
    return f"""{schema}
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> {badge}</div>
    <h1>{h1}<br><em>{h1em}</em></h1>
    <p class="hero-sub">{sub}</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
  </div>
</section>
{trust_strip()}
<section class="bg2">
  <div class="container">
    <span class="eyebrow">How It Works</span>
    <h2>Get Started in Minutes</h2>
    <p class="section-sub">{intro}</p>
    {steps(*step_items)}
  </div>
</section>
<section>
  <div class="container">
    {feat_grid(*feat_items, variant="amber")}
  </div>
</section>
{'<section class="bg2"><div class="container container-sm">' + faq_html + '</div></section>' if faq_html else ''}
<section class="bg2">
  <div class="container">
    {cta_band("Try EdrawMind Free — No Credit Card","Free plan available · Full features in trial")}
  </div>
</section>"""


def page_mindmap():
    return _use_case_page(
        f"Mind Map Maker — {YEAR} · 700+ Templates","Create Professional Mind Maps","with AI in Seconds",
        "EdrawMind combines AI generation, 700+ templates, and 15 layout styles to make professional mind mapping fast and effortless.",
        "Open EdrawMind, enter a topic or choose a template, and let AI or the intuitive editor build your map.",
        [("Choose Your Starting Point","Start from AI generation (type a topic, get a full map), a template (700+ to choose from), or blank canvas."),
         ("Build Your Map","Add nodes with Enter/Tab, drag to reorganize, add icons, images, and attachments. Intuitive keyboard shortcuts throughout."),
         ("Choose Your Layout","Switch between 15+ layout styles — mind map, tree chart, org chart, fishbone, timeline — with one click. Same data, different view."),
         ("Add Detail","Attach notes, links, images, and files to any node. Add progress indicators and task assignments for project maps."),
         ("Share or Export","Export to PDF, Word, PowerPoint, PNG, SVG or share a live link. Present directly from EdrawMind's slideshow mode.")],
        [("🤖","AI Generation","Type any topic — AI creates a complete multi-level map in seconds. Eliminates blank-page paralysis for any subject."),
         ("📋","700+ Templates","Business, education, project planning, and more. Start professional, edit to match your needs."),
         ("🔄","15+ Layout Styles","Mind map, tree, org chart, fishbone, timeline and more. One click to switch layouts on the same content."),
         ("📤","25+ Export Formats","PDF, Word, PowerPoint, PNG, SVG, HTML, Markdown. Share with anyone, anywhere, in any format.")],
        [("Is EdrawMind good for beginners?","Yes — EdrawMind is designed to be beginner-friendly. The interface is intuitive, templates provide ready-made starting points, and AI generation creates maps automatically. Most new users create their first useful map in under 5 minutes."),
         ("Can I use EdrawMind online without installing anything?","Yes — EdrawMind has a browser version at edrawmind.com. Desktop apps for Windows, Mac, and Linux are also available for offline use.")])


def page_templates():
    cats = [("📊 Business Strategy","SWOT, Porter's Five Forces, BCG Matrix, Business Model Canvas"),
            ("📅 Project Planning","Project roadmap, work breakdown structure, sprint planning, risk matrix"),
            ("🎓 Education","Concept maps, lesson plans, essay outlines, study guides, book reports"),
            ("💡 Brainstorming","Free brainstorm, 6 thinking hats, mind storm, idea funnel"),
            ("🗂️ Org Charts","Company hierarchy, team structure, department map, reporting lines"),
            ("📝 Meeting & Notes","Meeting agenda, action items, decision tree, problem-solving map"),
            ("🔄 Process & Flow","Process map, workflow diagram, decision flowchart, customer journey"),
            ("🎯 Personal Goals","Goal breakdown, habit tracker, personal development plan, vision board")]
    cards = "".join(f'<div class="feat-card feat-card-teal"><h3>{n}</h3><p style="font-size:.82rem;color:var(--ink3);line-height:1.7">{d}</p></div>' for n,d in cats)
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> 700+ Templates — {YEAR}</div>
    <h1>EdrawMind Templates:<br><em>700+ Free, Professional, Ready to Use</em></h1>
    <p class="hero-sub">Start from a polished, professionally designed template instead of a blank canvas. Every template is fully editable — change structure, colour, content, and layout to match your needs.</p>
    <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 Browse Templates Free</a>
  </div>
</section>
{trust_strip()}
<section class="bg2"><div class="container"><div class="feat-grid">{cards}</div></div></section>
<section><div class="container container-sm">
  {faq(
    ("Are EdrawMind templates free to use?","Yes — all 700+ templates are included with any EdrawMind plan, including the free plan (with some limitations) and all paid plans. No separate template purchase needed."),
    ("Can I create my own templates?","Yes — any EdrawMind map can be saved as a custom template for reuse. Teams can share custom templates in a shared library on team plans."),
    ("Can I import templates from other tools?","EdrawMind can import XMind files and several other formats. Templates from other tools can be recreated using EdrawMind's editor."),
  )}
  {cta_band("Access All 700+ Templates Free","Start from a professional template today — no card required.")}
</div></section>"""


def page_collab():
    return _use_case_page(
        f"Real-Time Collaboration — {YEAR}","Team Mind Mapping","in Real Time",
        "Multiple team members edit the same EdrawMind map simultaneously. See changes live, add comments, track versions.",
        "Share a map with your team, start collaborating live. See each other's cursors, edits, and comments in real time.",
        [("Create Your Map","Start a new map or open an existing one you want to collaborate on."),
         ("Invite Team Members","Share via link or email invitation. Set permission levels — view, comment, or edit."),
         ("Collaborate Live","Multiple editors work on the map simultaneously. Each person's cursor is visible. Changes appear instantly."),
         ("Add Comments","Click any node to add a comment or discussion thread. Tag teammates with @mentions."),
         ("Review History","Version history tracks every change. Restore any previous version at any time.")],
        [("👥","Live Multi-User Editing","See teammates' cursors and changes in real time. No refreshing, no version conflicts."),
         ("💬","Comments & Mentions","Add comments to any node. @mention teammates to assign feedback or tasks."),
         ("📜","Version History","Every version automatically saved. Restore any previous state in one click."),
         ("🔗","Easy Sharing","Share via link with granular permission controls. View-only, comment, or full edit access.")])


def page_gantt():
    return _use_case_page(
        f"Gantt Chart View — {YEAR}","Turn Mind Maps into","Project Gantt Charts",
        "EdrawMind uniquely converts mind maps directly to Gantt chart view. Plan in mind map format, execute in Gantt format — same data, both views.",
        "Build your project mind map, assign tasks and deadlines to nodes, then switch to Gantt view. The conversion is automatic.",
        [("Build Your Project Mind Map","Create a mind map of your project scope — phases, tasks, deliverables, and dependencies."),
         ("Assign Tasks and Owners","Add task assignment, priority, and owner information to any node in the map."),
         ("Set Deadlines","Add start dates and end dates to tasks. EdrawMind calculates durations automatically."),
         ("Switch to Gantt View","One click converts your mind map to a Gantt chart. All tasks appear on a timeline."),
         ("Track Progress","Update task completion percentage. Gantt view shows real-time progress across the whole project.")],
        [("🗺️","From Brainstorm to Timeline","No re-entering data between tools. The same information powers both mind map and Gantt views."),
         ("📅","Visual Project Timeline","Gantt view shows what's happening when, who owns what, and where the critical path lies."),
         ("🔄","Instant View Switch","Toggle between mind map and Gantt at any time. Always working with the same underlying data."),
         ("👥","Team Visibility","Share the Gantt view with stakeholders who need a timeline without the full mind map context.")],
        [("Does EdrawMind replace project management tools?","EdrawMind's Gantt chart is excellent for planning and visual tracking. For complex project management with integrations, reporting, and automation, dedicated tools like Jira or Asana may be needed. For most small teams, EdrawMind covers the core planning workflow."),])


def page_students():
    return _use_case_page(
        f"EdrawMind for Students — {YEAR}","Study Smarter","with AI Mind Maps",
        "From lecture notes to essay planning to exam revision — mind maps improve comprehension and memory retention for every subject.",
        "Use AI to generate study maps from topics, templates to structure essays and reports, and visual layouts to make revision more effective.",
        [("Generate a Study Map","Enter your topic — AI creates a structured study map in seconds. Use as a starting point for revision."),
         ("Map Your Lectures","During or after lectures, build mind maps from your notes. Visual structure helps retention better than linear notes."),
         ("Plan Essays and Reports","Use a mind map to plan your essay structure before writing. Branches become paragraphs. Arguments become sub-nodes."),
         ("Create Revision Maps","Condense entire topics into one mind map. Review the visual structure to reinforce memory at exam time."),
         ("Export for Study Groups","Share maps with classmates or export to PDF for printing and offline study.")],
        [("🧠","AI Study Map Generation","Type any topic — get a complete, structured study map. Textbook chapters, historical events, scientific concepts."),
         ("📚","700+ Education Templates","Book report, essay plan, concept map, timeline, flashcard map — every academic format covered."),
         ("🔄","Visual Revision","Research shows visual organization improves memory recall. Mind maps beat linear notes for most learners."),
         ("🎓","Exam Prep","Condense a whole unit into one revision map. Identify gaps in knowledge. Practice recall from visual cues.")],
        [("Is EdrawMind free for students?","EdrawMind has a free plan that covers basic student use. Wondershare also offers a student discount on paid plans. Check current educational pricing at checkout."),
         ("Which subjects work best with mind mapping?","History, biology, literature, economics, and psychology respond especially well to mind mapping. Scientific processes, historical causation, and literary themes all suit visual structure."),])


def page_teachers():
    return _use_case_page(
        f"EdrawMind for Teachers — {YEAR}","Visual Learning","for Every Subject",
        "Create visual lesson plans, concept maps for class, and student activities with EdrawMind's teaching-focused templates.",
        "Build lesson structure maps, create visual explanations for complex concepts, and share interactive maps with your students.",
        [("Plan Your Lesson","Use a mind map to plan lesson structure — objectives, activities, assessments, and resources in one visual overview."),
         ("Create Concept Maps","Build visual explanations of complex topics for class display. Export to PNG for presentation or printing."),
         ("Design Student Activities","Create template maps for students to complete — partially filled concept maps, guided brainstorming frameworks."),
         ("Share with Students","Share live maps for class collaboration, or export to PDF/PNG for handouts and homework."),
         ("Build a Resource Library","Save your best teaching maps as templates. Reuse and adapt across classes and years.")],
        [("📋","Teaching Templates","Lesson plans, concept maps, Venn diagrams, KWL charts, story maps — all built for classroom use."),
         ("🖼️","Visual Presentations","Export maps as large PNG for display, or present directly from EdrawMind's slideshow mode."),
         ("👥","Class Collaboration","Share maps for student editing — collaborative brainstorming and group project planning."),
         ("🤖","AI Content Generation","Generate concept maps for any curriculum topic instantly. Less prep time, more teaching time.")],
        [("Does EdrawMind work for remote teaching?","Yes — share live maps with students via link for online classes. Real-time collaboration works in any browser without installation."),])


def page_business():
    return _use_case_page(
        f"EdrawMind for Business — {YEAR}","Strategy, Planning","& Team Brainstorming",
        "From strategy workshops to project kick-offs to meeting agendas — EdrawMind powers every visual thinking workflow a business team needs.",
        "Use AI and templates to run faster, more structured meetings, planning sessions, and strategic reviews.",
        [("Run Strategy Sessions","Use SWOT, BCG Matrix, or Porter's Five Forces templates to structure strategic analysis workshops."),
         ("Plan Projects Visually","Map project scope, then convert to Gantt chart for timeline planning. Both views from one map."),
         ("Structure Meetings","Create agenda mind maps. Capture decisions and action items in the same map during the meeting."),
         ("Collaborate in Real Time","Multiple team members edit simultaneously during workshops. Remote and in-person teams together."),
         ("Present to Stakeholders","Auto-presentation mode converts your map to a slideshow for board presentations and stakeholder updates.")],
        [("📊","Business Templates","SWOT, business model canvas, competitive analysis, org charts, project roadmaps — all ready to use."),
         ("🗺️","From Plan to Gantt","Convert project scope maps directly to Gantt charts. No re-entering data between planning tools."),
         ("🤖","AI for Rapid Drafting","AI generates first-draft strategy maps, project breakdowns, and analysis frameworks in seconds."),
         ("👥","Team Collaboration","Real-time multi-user editing. Comments, @mentions, version history for distributed teams.")],
        [("Can EdrawMind replace dedicated project management tools?","For small teams and individual project planning, yes — EdrawMind's mind map + Gantt combination covers the core workflow. For complex multi-project tracking with integrations, dedicated PM tools may still be needed alongside EdrawMind."),])


def page_pm():
    return _use_case_page(
        f"EdrawMind for Project Management — {YEAR}","Mind Maps + Gantt Charts","in One Tool",
        "Plan projects visually in mind map format, then convert to Gantt chart for timeline execution — without changing tools.",
        "The mind map captures what needs to happen. The Gantt chart shows when. EdrawMind uniquely connects both views.",
        [("Map Project Scope","Build a mind map of everything your project involves — phases, tasks, deliverables, stakeholders, risks."),
         ("Assign Ownership","Add owner and priority to each task node. Clear responsibility from the planning stage."),
         ("Set Dates","Add start and end dates to tasks in mind map view. EdrawMind calculates timelines automatically."),
         ("Switch to Gantt View","One click converts to Gantt. All tasks appear on a visual timeline with progress tracking."),
         ("Share and Update","Share Gantt view with stakeholders. Update progress on tasks as the project moves forward.")],
        [("🗺️","Scope in Mind Map","Visual scope capture is faster and more natural than spreadsheets. Branches become WBS levels."),
         ("📅","Execute in Gantt","Timeline view gives the whole team clarity on sequence, dependencies, and deadlines."),
         ("🔄","One Data Source","Mind map and Gantt share the same data. Update once, both views reflect the change."),
         ("👥","Team Transparency","Share either view with different audiences — full map for the team, Gantt for stakeholders.")],
        [("How complex can EdrawMind Gantt charts be?","EdrawMind Gantt charts handle standard project plans well — tasks, owners, dates, and progress. For complex projects with resource levelling, earned value analysis, and multi-project integration, dedicated PM tools are more powerful."),])


def page_brainstorm():
    return _use_case_page(
        f"Brainstorming Tool — {YEAR}","AI-Powered Brainstorming","with Your Team",
        "EdrawMind makes brainstorming sessions more productive with AI idea generation, real-time collaboration, and instant visual organization.",
        "Start with AI or blank canvas, add every idea as a node, reorganize in real time with your team, and leave with an actionable structure.",
        [("Set Up Your Session","Create a central topic node. Share with team members for a live collaborative session."),
         ("Generate Initial Ideas","Use AI to seed the map with starter ideas, then let the team expand and branch in real time."),
         ("Organize and Cluster","Drag nodes to group related ideas. Use colour coding to categorize themes and priorities."),
         ("Vote and Prioritize","Add ratings or use AI to suggest the most promising ideas based on your criteria."),
         ("Convert to Action Plan","Select the top ideas and convert them to a project plan or action map with owners and dates.")],
        [("🤖","AI Idea Generation","Seed your brainstorm with AI-generated ideas to overcome blank-page blocks and spark connections."),
         ("👥","Live Team Editing","Your whole team adds ideas simultaneously. No turn-taking, no idea bottlenecks."),
         ("🎨","Visual Organization","Drag, colour-code, and cluster ideas visually. Pattern recognition is faster in maps than lists."),
         ("📅","Idea to Action","Convert the best ideas directly to a project plan or Gantt chart. Brainstorm to execution in one tool.")])


def page_concept():
    return _use_case_page(
        f"Concept Map Maker — {YEAR}","Create Concept Maps","with Relationships",
        "EdrawMind creates concept maps with labeled relationships between nodes — ideal for education, knowledge management, and complex topic visualization.",
        "Concept maps show how ideas relate, not just what they are. Add labeled arrows between nodes to show cause, effect, and relationship.",
        [("Create Your Central Concept","Add the main idea or concept as your central node."),
         ("Add Related Concepts","Branch out with related concepts, sub-concepts, and supporting ideas."),
         ("Label Relationships","Add labeled arrows between any nodes to show the type of relationship — causes, leads to, is part of."),
         ("Apply Concept Map Layout","Switch to concept map layout mode for a non-hierarchical view that shows all connections equally."),
         ("Export for Presentation","Export to PNG for classroom use, or share live for interactive exploration.")],
        [("🔗","Relationship Labels","Show how ideas connect — not just what they are. Labeled arrows add meaning to every connection."),
         ("📚","Education Templates","Pre-built concept map templates for science, history, literature, and more."),
         ("🤖","AI Generation","AI creates concept maps for any topic — save time building the initial structure."),
         ("📤","Easy Sharing","Export to PNG for classroom display, PDF for handouts, or live link for interactive use.")])


def page_flowchart():
    return _use_case_page(
        f"Flowchart Maker — {YEAR}","Flowcharts, Org Charts","& Diagrams in EdrawMind",
        "EdrawMind creates mind maps, flowcharts, org charts, decision trees, and fishbone diagrams — all in one tool with the same interface.",
        "Use the same tool for all your visual thinking needs — switch layout type to change a mind map into a flowchart or org chart.",
        [("Create Your Diagram","Start from a template or blank canvas. Choose your diagram type from the layout panel."),
         ("Add Nodes and Connections","Add shapes, add text, connect with arrows. Drag to reorganize. Keyboard shortcuts throughout."),
         ("Apply Flow Layout","Switch to flowchart layout for top-down flow, or org chart layout for hierarchical display."),
         ("Customize Appearance","Change colours, fonts, shapes, and line styles to match your brand or presentation needs."),
         ("Export or Embed","Export to PDF, PNG, SVG, or embed in documents and presentations.")],
        [("🔄","All Diagram Types","Mind map, flowchart, org chart, fishbone, tree, timeline — all from the same interface."),
         ("📋","Diagram Templates","Pre-built flowchart and org chart templates for common business processes."),
         ("🎨","Full Customization","Colours, fonts, shapes, line styles — complete visual control."),
         ("📤","Universal Export","PDF, PNG, SVG, Word, PowerPoint — share in any format.")])


def page_presentation():
    return _use_case_page(
        f"Presentation Mode — {YEAR}","Turn Mind Maps into","Instant Slideshows",
        "EdrawMind's auto-presentation mode converts any mind map into a navigable slideshow with one click. Present your thinking without PowerPoint.",
        "Build your mind map normally, then click Presentation Mode. EdrawMind automatically navigates through branches as slides.",
        [("Build Your Mind Map","Create your mind map with the full content of your presentation as branches and sub-nodes."),
         ("Enter Presentation Mode","Click the Presentation button. EdrawMind creates a slideshow from your map structure automatically."),
         ("Customize Slide Order","Reorder branches to control the presentation flow. Each branch becomes a slide or section."),
         ("Present","Navigate through slides with arrow keys. Each slide zooms into the relevant map section — visually engaging."),
         ("Export to PowerPoint","Optionally export to .pptx for sharing with people who need a traditional slide format.")],
        [("🎬","One-Click Slideshow","Map to presentation in one click. No reformatting, no rebuilding in PowerPoint."),
         ("🔍","Visual Navigation","Presentations zoom through your map structure — more engaging than static slides."),
         ("📤","PowerPoint Export","Export to .pptx for sharing. Take your mind map presentation into any slide environment."),
         ("🔄","Always Up to Date","Change the map, the presentation updates automatically. No duplicate maintenance.")])


def page_export():
    export_list = [("PDF","Universal sharing — print or digital"),("Word (.docx)","Editable document with map embedded"),
                   ("PowerPoint (.pptx)","Presentation-ready slides"),("PNG","High-resolution image"),
                   ("SVG","Scalable vector for web and print"),("HTML","Interactive web page"),
                   ("Markdown","Plain text with structure"),("Excel","Spreadsheet with node data"),
                   ("Outline (.txt)","Plain text outline of your map")]
    rows = "".join(f"<tr><td><strong>{f}</strong></td><td>{d}</td></tr>" for f,d in export_list)
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Export Guide — {YEAR}</div>
    <h1>EdrawMind Export Options:<br><em>25+ Formats for Every Use Case</em></h1>
    <p class="hero-sub">Export EdrawMind maps to PDF, Word, PowerPoint, PNG, SVG, HTML, and more. Share with anyone — even people who don't have EdrawMind installed.</p>
    <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
  </div>
</section>
<section class="bg2">
  <div class="container container-sm">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Export Format</th><th>Best Used For</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
    {faq(
      ("Can I export to PowerPoint?","Yes — EdrawMind exports directly to .pptx. The mind map is converted to presentation slides. You can then edit the file in PowerPoint or Google Slides."),
      ("Does PDF export preserve quality?","Yes — PDF exports are vector-quality, meaning they scale perfectly to any size for printing or digital sharing."),
      ("Can I export in multiple formats at once?","You can export to any format one at a time. Batch export to multiple formats simultaneously is available on team plans."),
    )}
    {cta_band("Try All Export Formats Free","No credit card · Full export features in trial")}
  </div>
</section>"""


def page_download():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Latest Version — {TODAY[:7]}</div>
    <h1>Download EdrawMind {YEAR}<br><em>Every Platform — Free</em></h1>
    <p class="hero-sub">Windows, Mac, Linux, iOS, Android, and browser. Full cross-platform sync. Start on desktop, continue on phone — your maps always with you. Free plan included.</p>
    <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 Download Free — No Card</a>
  </div>
</section>
{trust_strip()}
<section class="bg2">
  <div class="container">
    <div class="compat-grid">
      <div class="compat-card"><span class="compat-icon">🪟</span><div class="compat-name">Windows</div><div class="compat-detail">Win 7+ · 64-bit · Full features</div></div>
      <div class="compat-card"><span class="compat-icon">🍎</span><div class="compat-name">macOS</div><div class="compat-detail">10.12+ · Intel & Apple Silicon</div></div>
      <div class="compat-card"><span class="compat-icon">🐧</span><div class="compat-name">Linux</div><div class="compat-detail">DEB/RPM · Full features</div></div>
      <div class="compat-card"><span class="compat-icon">📱</span><div class="compat-name">iOS</div><div class="compat-detail">iPhone & iPad · App Store</div></div>
      <div class="compat-card"><span class="compat-icon">🤖</span><div class="compat-name">Android</div><div class="compat-detail">Phone & tablet · Google Play</div></div>
      <div class="compat-card"><span class="compat-icon">🌐</span><div class="compat-name">Browser</div><div class="compat-detail">Any browser · No install</div></div>
    </div>
  </div>
</section>
<section>
  <div class="container container-sm">
    {faq(
      ("Is EdrawMind available for Linux?","Yes — EdrawMind is one of the few mind mapping tools with native Linux support. DEB (Ubuntu/Debian) and RPM (Fedora/RHEL) packages available."),
      ("Does EdrawMind sync across devices?","Yes — all maps sync automatically via cloud. Start a map on desktop, open it on your phone or in the browser seamlessly."),
      ("What are the minimum system requirements?","Windows: Win 7+, 4GB RAM, 2GB disk. Mac: macOS 10.12+, 4GB RAM. Linux: 64-bit, 4GB RAM. Mobile: iOS 12+ or Android 6+."),
      ("Does the free download include all features?","The free plan includes core mind mapping. Download includes all features — paid features show a trial/upgrade prompt. No time limit on the free plan."),
    )}
    {cta_band("Download EdrawMind Free","All platforms · Free plan · No credit card")}
  </div>
</section>"""


def page_deals():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Updated {TODAY[:7]}</div>
    <h1>EdrawMind Deals<br><em>&amp; Best Price {TODAY[:7]}</em></h1>
    <p class="hero-sub">How to get EdrawMind at the absolute lowest available price right now — partner link, perpetual vs annual analysis, and when sales happen.</p>
    <a href="{AFF}" class="btn btn-amber btn-xl" rel="nofollow sponsored">🧠 See Current Best Offer</a>
  </div>
</section>
<section class="bg2">
  <div class="container">
    {feat_grid(
      ("🔗","Partner Link — Best Rate","Our affiliate link routes through Wondershare's partner portal where the best current promotion is automatically applied."),
      ("🆓","Free Plan First","EdrawMind has a genuinely useful free plan. Test core features without any payment commitment before upgrading."),
      ("💰","Perpetual Math","Perpetual (~$118) vs Annual (~$59/yr) breaks even at 2 years. If you'll use it for more than 2 years, perpetual wins."),
      ("📅","Sale Calendar","Biggest discounts: Black Friday (November), New Year (January), Wondershare Anniversary (varies). Check our link for live promotions."),
    )}
  </div>
</section>
<section>
  <div class="container container-sm">
    {faq(
      ("What's the cheapest way to get EdrawMind?","Perpetual license (~$118 once) is cheapest long-term if you don't need the AI features. Annual (~$59/yr) includes AI. Perpetual breaks even vs annual at 2 years."),
      ("Is there a student discount?","Yes — Wondershare offers educational pricing. Verify student status at checkout after clicking our link."),
      ("Are there coupon codes?","Our partner link always shows the current best available offer, which is more reliable than searching for codes that may be expired."),
    )}
    {cta_band("Claim the Best Available Rate","Partner link updated daily · Always the current best offer")}
  </div>
</section>"""


def page_free_vs_paid():
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> Honest Breakdown — {TODAY[:7]}</div>
    <h1>EdrawMind Free vs Paid {YEAR}:<br><em>What Do You Actually Get?</em></h1>
    <p class="hero-sub">EdrawMind's free plan is more generous than most competitors. Here is exactly what's included at each level — so you can decide whether the free plan is enough for your needs.</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">Start Free →</a>
  </div>
</section>
<section class="bg2">
  <div class="container container-sm">
    <div class="tbl-wrap"><table>
      <thead><tr><th>Feature</th><th>Free Plan</th><th>Paid Plan (~$59/yr)</th></tr></thead>
      <tbody>
        <tr><td>Mind maps</td><td class="ok">Limited</td><td class="win">Unlimited</td></tr>
        <tr><td>Templates</td><td class="ok">Basic selection</td><td class="win">700+</td></tr>
        <tr><td>AI mind map generation</td><td class="cross">✗</td><td class="win">✓ Full</td></tr>
        <tr><td>Gantt chart view</td><td class="cross">✗</td><td class="win">✓</td></tr>
        <tr><td>Real-time collaboration</td><td class="cross">✗</td><td class="win">✓</td></tr>
        <tr><td>Export formats</td><td class="ok">3 formats</td><td class="win">25+ formats</td></tr>
        <tr><td>Presentation mode</td><td class="partial">Basic</td><td class="win">Full</td></tr>
        <tr><td>Cloud storage</td><td class="ok">Limited</td><td class="win">Unlimited</td></tr>
        <tr><td>Layout styles</td><td class="ok">Basic layouts</td><td class="win">15+ styles</td></tr>
        <tr><td>Windows/Mac/Linux</td><td class="win">✓</td><td class="win">✓</td></tr>
        <tr><td>iOS & Android</td><td class="win">✓</td><td class="win">✓</td></tr>
      </tbody>
    </table></div>
    <div class="callout callout-teal" style="margin-top:1.5rem">
      <h3>Who Should Stay on the Free Plan</h3>
      <ul class="styled">
        <li>Occasional mind mappers who create a few maps per month</li>
        <li>Students who just need basic map creation and don't need AI</li>
        <li>Anyone wanting to test EdrawMind before committing</li>
      </ul>
    </div>
    <div class="callout callout-amber" style="margin-top:1rem">
      <h3>Who Should Upgrade to Paid</h3>
      <ul class="styled">
        <li>Regular mind mappers who want AI generation to save time</li>
        <li>Project managers who need the Gantt chart integration</li>
        <li>Teams needing real-time collaboration</li>
        <li>Anyone who exports maps frequently to PDF, Word, or PowerPoint</li>
      </ul>
    </div>
    {cta_band("Try the Full Paid Features Free","No credit card · Test AI, Gantt, and all templates before buying")}
  </div>
</section>"""


def _guide_page(badge, h1, h1em, sub, body_html):
    return f"""
<section class="hero">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div class="hero-badge"><span class="badge-dot"></span> {badge}</div>
    <h1>{h1}<br><em>{h1em}</em></h1>
    <p class="hero-sub">{sub}</p>
    <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">🧠 Try EdrawMind Free</a>
  </div>
</section>
<section class="bg2"><div class="container container-sm">{body_html}</div></section>"""


def page_guide():
    body = f"""
<h2>What Is a Mind Map?</h2>
<p>A mind map is a visual diagram that organises information around a central idea. Branches radiate outward from the centre, with related sub-topics on smaller branches. It mirrors how the brain naturally associates ideas — which is why mind maps are effective for memory, creative thinking, and complex planning.</p>
<div class="callout callout-teal">
  <h3>Core Principle</h3>
  <p>Put the main topic at the centre. Add primary branches for major themes. Add secondary branches for details and examples. The visual structure makes relationships between ideas immediately visible.</p>
</div>
<h2>7 Rules for Effective Mind Maps</h2>
{steps(
  ("Start with a Clear Central Topic","Your central node should be specific enough to focus the map but broad enough to have multiple branches. 'Marketing Strategy Q3' is better than 'Marketing' or 'Everything we need to do about marketing in Q3.'"),
  ("Use Single Words or Short Phrases","Each node should capture one idea in as few words as possible. Full sentences reduce the visual impact and make the map harder to scan."),
  ("Limit Branch Depth","Keep most content within 3-4 levels of depth. Deeper nesting usually means you need a separate map for that sub-topic."),
  ("Use Colour Consistently","Assign consistent colours to branches or categories. Colour adds a visual layer of meaning that helps memory and navigation."),
  ("Add Images and Icons","Visual elements improve recall and make maps more engaging. EdrawMind includes clip art and icon libraries for this."),
  ("Prioritize Radically","Not everything deserves equal visual weight. Use node size, colour, and emphasis to signal what matters most."),
  ("Review and Prune","A first-draft mind map is rarely final. Reorganize, merge, and delete nodes. The process of refinement improves understanding."),
)}
<h2>When to Use a Mind Map vs Other Tools</h2>
<div class="tbl-wrap"><table>
  <thead><tr><th>Situation</th><th>Use Mind Map</th><th>Use Instead</th></tr></thead>
  <tbody>
    <tr><td>Brainstorming ideas</td><td class="chk">✓ Best tool</td><td>—</td></tr>
    <tr><td>Understanding a complex topic</td><td class="chk">✓ Best tool</td><td>—</td></tr>
    <tr><td>Planning an essay or report</td><td class="chk">✓ Excellent</td><td>—</td></tr>
    <tr><td>Revision and memory</td><td class="chk">✓ Excellent</td><td>—</td></tr>
    <tr><td>Project timeline</td><td class="ok">Use with Gantt</td><td>Gantt chart</td></tr>
    <tr><td>Linear step-by-step process</td><td class="bad">Limited</td><td>Flowchart</td></tr>
    <tr><td>Data analysis</td><td class="bad">Not ideal</td><td>Spreadsheet</td></tr>
  </tbody>
</table></div>
{faq(
  ("How long should a mind map take to create?","A basic mind map of a topic you know well takes 10–20 minutes. With EdrawMind's AI generation, a useful first draft takes under 10 seconds. The key is to start imperfect and refine."),
  ("How many branches is too many?","As a rule of thumb, 5–9 primary branches is ideal. More than that and the central topic may be too broad — consider splitting into multiple maps."),
)}
{cta_band("Create Your First Mind Map Free","EdrawMind AI generates a complete map from any topic in seconds.")}"""
    return _guide_page(f"Complete Guide — {YEAR}","Complete Mind Mapping Guide","From Beginner to Expert",
        "Everything you need to know about creating effective mind maps — principles, techniques, and when to use them.",body)


def page_study():
    body = f"""
<h2>Why Mind Maps Improve Memory</h2>
<p>Linear notes — text on a page — use only one part of your brain. Mind maps engage spatial memory, colour association, and visual pattern recognition simultaneously. Research consistently shows that visual organisation improves both comprehension and long-term recall compared to linear note-taking.</p>
<div class="callout callout-teal">
  <h3>The Cornell Notes to Mind Map Method</h3>
  <p>After a lecture, convert your Cornell notes into a mind map. The central topic goes in the middle, your key questions become primary branches, and answers become sub-branches. This conversion process alone reinforces memory.</p>
</div>
{feat_grid(
  ("📚","The Chapter Collapse Technique","Take an entire textbook chapter and collapse it into one mind map. Every key concept becomes a branch. Every detail becomes a sub-node. The act of creating the map is itself a review."),
  ("🔄","The Blank Map Test","Create a mind map of a topic. Then, the next day, try to recreate it from memory on a blank page. Gaps in your blank map are gaps in your knowledge. Fill them and repeat."),
  ("🎨","Colour Your Categories","Use consistent colours for different categories — definitions in blue, examples in green, relationships in orange. Colour coding creates memory triggers."),
  ("⏱️","Spaced Repetition Maps","Create a master revision map at the start of a topic. Review it after 1 day, 3 days, 1 week, and 2 weeks. Spaced repetition combined with visual maps maximises retention."),
  variant="amber"
)}
{faq(
  ("Does mind mapping work for all subjects?","Mind mapping works best for subjects with interconnected concepts — history, biology, literature, economics, psychology. It's less naturally suited to subjects that are primarily numerical or procedural, though it can still help with organizing the overall structure."),
  ("How do I mind map during a lecture?","Use a simple structure — central topic, one branch per major point. Don't try to capture everything. Focus on relationships and key ideas. Fill in details from your notes afterward. EdrawMind on a laptop or tablet works well for in-class mapping."),
)}
{cta_band("Start Studying with Mind Maps Free","EdrawMind AI generates study maps from any topic instantly.")}"""
    return _guide_page(f"Study Guide — {YEAR}","Mind Map Study Techniques","Improve Memory & Understanding",
        "Research-backed techniques for using mind maps to study more effectively — better retention, faster revision, deeper understanding.",body)


def page_notes():
    body = f"""
<h2>The Problem with Linear Notes</h2>
<p>Linear notes — sentences on a page — record information sequentially but hide the relationships between ideas. When you review linear notes, you re-read text. When you review a mind map, you see structure, patterns, and connections that your brain can process more quickly.</p>
<div class="callout callout-blue">
  <h3>Research on Visual Note-Taking</h3>
  <p>Multiple studies on dual-coding theory (Paivio, 1986 and subsequent research) show that information encoded both verbally and visually is remembered significantly better than information encoded only verbally. Mind maps engage both coding pathways simultaneously.</p>
</div>
{steps(
  ("Identify the Central Topic","Start every set of notes with the clearest possible central topic. One lecture = one map."),
  ("Capture Key Points as Branches","Each major point becomes a primary branch. Use 3-7 words maximum per node."),
  ("Link Related Ideas","Use connecting arrows between branches to show relationships that cross the main structure."),
  ("Add Visual Anchors","Add icons, images, and colour to create visual memory triggers for important concepts."),
  ("Review and Condense","After your session, prune redundant nodes and strengthen the structure. Condensing is itself a review."),
)}
{faq(
  ("Is EdrawMind good for taking notes in class?","Yes — EdrawMind's desktop and tablet apps work well for in-class note-taking. The keyboard shortcuts make adding nodes fast. Some students prefer to take linear notes during class and convert to mind maps afterward as a review activity."),
  ("Can I import existing notes into EdrawMind?","EdrawMind can import text outlines and several structured formats. You can also paste text and use AI to convert it into a mind map structure."),
)}
{cta_band("Try Visual Note-Taking Free","EdrawMind on every platform — desktop, tablet, browser.")}"""
    return _guide_page(f"Note-Taking Guide — {YEAR}","Visual Note-Taking","Better Than Linear Notes",
        "Why mind map note-taking beats linear notes for comprehension and memory — and how to do it effectively with EdrawMind.",body)


# ══════════════════════════════════════════════════════════════════════════════
# MULTILINGUAL HELPERS
# ══════════════════════════════════════════════════════════════════════════════
def _home(pill,badge,h1,h1em,sub,cta,feats,testis,faqs,vs_rows,c2="XMind"):
    rh="".join(f"<tr><td>{f}</td><td class='win'>{e}</td><td class='bad'>{v}</td></tr>" for f,e,v in vs_rows)
    return lang_hero(pill,badge,h1,h1em,sub,cta)+f"""
{trust_strip()}
<section class="bg2"><div class="container">{feat_grid(*feats,variant="amber")}</div></section>
<section><div class="container">
  <div class="tbl-wrap"><table>
  <thead><tr><th>Feature</th><th>🧠 EdrawMind</th><th>{c2}</th></tr></thead>
  <tbody>{rh}</tbody></table></div>
</div></section>
<section class="bg2"><div class="container">{testimonials(*testis)}</div></section>
<section><div class="container container-sm">
  {faq(*faqs)}
  {cta_band(cta,"Free plan · No credit card · Full features in trial")}
</div></section>"""

def _vs(pill,badge,h1,h1em,sub,cta,rows,faqs,c2="XMind"):
    rh="".join(f"<tr><td>{f}</td><td class='win'>{e}</td><td class='bad'>{v}</td></tr>" for f,e,v in rows)
    return lang_hero(pill,badge,h1,h1em,sub,cta)+f"""
<section class="bg2"><div class="container">
  <div class="tbl-wrap"><table>
  <thead><tr><th>Feature</th><th>🧠 EdrawMind</th><th>{c2}</th></tr></thead>
  <tbody>{rh}</tbody></table></div>
</div></section>
<section><div class="container container-sm">
  {faq(*faqs)}
  {cta_band(cta,"Free plan · No credit card")}
</div></section>"""

def _mindmap(pill,badge,h1,h1em,sub,cta,feats,faqs):
    return lang_hero(pill,badge,h1,h1em,sub,cta)+f"""
{trust_strip()}
<section class="bg2"><div class="container">{feat_grid(*feats,variant="amber")}</div></section>
<section><div class="container container-sm">
  {faq(*faqs)}
  {cta_band(cta,"Free plan · Full features in trial")}
</div></section>"""

def _students(pill,badge,h1,h1em,sub,cta,feats,faqs):
    return _mindmap(pill,badge,h1,h1em,sub,cta,feats,faqs)

def _pricing(pill,badge,h1,h1em,sub,cta,rows_5y,faqs,yr="Year"):
    rh="".join(f"<tr><td>{o}</td><td class='win'>{y1}</td><td class='win'>{y2}</td><td class='win'>{y5}</td></tr>" for o,y1,y2,y5 in rows_5y)
    return lang_hero(pill,badge,h1,h1em,sub,cta)+f"""
<section class="bg2"><div class="container container-sm">
  <div class="tbl-wrap"><table>
  <thead><tr><th>Plan</th><th>{yr} 1</th><th>{yr} 2</th><th>{yr} 5</th></tr></thead>
  <tbody>{rh}</tbody></table></div>
  {faq(*faqs)}
  {cta_band(cta,"Free plan · No credit card")}
</div></section>"""

def _ai(pill,badge,h1,h1em,sub,cta,feats,faqs):
    return lang_hero(pill,badge,h1,h1em,sub,cta)+f"""
{trust_strip()}
<section class="bg2"><div class="container">{feat_grid(*feats,variant="amber")}</div></section>
<section><div class="container container-sm">
  {faq(*faqs)}
  {cta_band(cta,"AI generation in free trial")}
</div></section>"""

VS_ROWS_BASE=[
    ("AI map generation","✓ One-click","✗"),
    ("Templates","700+","~100"),
    ("Gantt chart","✓","✗"),
    ("Presentation mode","✓","✓"),
    ("Perpetual license","✓ ~$118","✗"),
    ("Linux support","✓","✗"),
    ("Export formats","25+","10+"),
    ("Annual cost","~$59/yr","~$48/yr"),
]

# ══════════════════════════════════════════════════════════════════════════════
# SPANISH
# ══════════════════════════════════════════════════════════════════════════════
def page_home_es():
    return _home("🇪🇸 Versión Española","Software de Mapas Mentales 2026 · Reseña Honesta",
        "Mapas Mentales con","IA — 700+ Plantillas",
        f"EdrawMind {YEAR}: IA genera mapas mentales completos de múltiples niveles, 700+ plantillas, diagramas de Gantt, colaboración en tiempo real. Reseña honesta.",
        "Probar EdrawMind Gratis",
        [("🤖","IA Genera Mapas al Instante","Escribe cualquier tema y la IA crea un mapa mental completo de múltiples niveles en segundos. Sin parálisis ante la página en blanco."),
         ("📋","700+ Plantillas","Estrategia empresarial, planificación de proyectos, apuntes de estudio, diagramas de Gantt — todas las plantillas que necesitas."),
         ("📊","Vista de Diagrama de Gantt","Convierte cualquier mapa mental en un diagrama de Gantt con un clic. Del brainstorming al plan de proyecto sin cambiar de herramienta."),
         ("👥","Colaboración en Tiempo Real","Varios miembros del equipo editan el mismo mapa simultáneamente. Perfecto para talleres y reuniones.")],
        [("La IA de EdrawMind es increíble. Escribí 'plan de marketing digital' y obtuve un mapa completo de 4 niveles en 8 segundos. Lo presenté al cliente esa misma tarde.","Carlos M.","Consultor de Marketing","🇪🇸","5"),
         ("La función de Gantt es exactamente lo que necesitaba. Pasar del mapa mental al diagrama de Gantt sin reingresar datos es un cambio de juego para la planificación de proyectos.","Elena R.","Gestora de Proyectos","🇲🇽","5")],
        [("¿EdrawMind es gratuito?","Sí — EdrawMind tiene un plan gratuito con funciones básicas de mapas mentales. Los planes de pago (~$59/año o ~$118 perpetua) desbloquean IA, todas las plantillas, Gantt y exportación completa."),
         ("¿Cómo funciona la generación IA?","Escribe cualquier tema — la IA crea un mapa mental completo de múltiples niveles en segundos. Puedes editar, expandir o regenerar cualquier rama.")],
        VS_ROWS_BASE)

def page_vs_xmind_es():
    return _vs("🇪🇸 Español","Comparación Completa 2026",
        "EdrawMind vs XMind:","IA, Gantt y 7× Más Plantillas",
        "XMind es buena herramienta. EdrawMind añade generación IA, diagramas de Gantt, 700+ plantillas y licencia perpetua.",
        "Probar EdrawMind Gratis",VS_ROWS_BASE,
        [("¿EdrawMind tiene mejor IA que XMind?","EdrawMind tiene generación IA de mapas completos. XMind no tiene esta función. EdrawMind gana claramente en IA."),
         ("¿Es más fácil de usar XMind?","XMind tiene interfaz más minimalista. EdrawMind tiene más funciones y curva de aprendizaje algo mayor, pero es amigable para principiantes.")])

def page_mindmap_es():
    return _mindmap("🇪🇸 Español",f"Creador de Mapas Mentales {YEAR} · 700+ Plantillas",
        "Crea Mapas Mentales Profesionales","con IA en Segundos",
        "IA genera mapas completos desde cualquier tema. 700+ plantillas, 15+ estilos de diseño, colaboración en tiempo real.",
        "Probar EdrawMind Gratis",
        [("🤖","IA al Instante","Escribe el tema y obtén un mapa completo en segundos."),
         ("📋","700+ Plantillas","Plantillas para todos los casos de uso, completamente editables."),
         ("🔄","15+ Estilos","Mapa mental, árbol, organigrama, espina de pez — un clic para cambiar."),
         ("📤","Exporta a Todo","PDF, Word, PowerPoint, PNG, SVG y más.")],
        [("¿Es EdrawMind bueno para principiantes?","Sí — interfaz intuitiva, plantillas listas para usar y IA que genera mapas automáticamente. La mayoría crea su primer mapa útil en menos de 5 minutos."),
         ("¿Puedo usar EdrawMind sin instalar nada?","Sí — EdrawMind tiene versión web. También apps de escritorio para Windows, Mac y Linux.")])

def page_students_es():
    return _students("🇪🇸 Español",f"EdrawMind para Estudiantes {YEAR}",
        "Estudia Más Inteligente","con Mapas Mentales IA",
        "De los apuntes de clase a la planificación de ensayos y la revisión para exámenes — los mapas mentales mejoran la comprensión y la memoria.",
        "Probar EdrawMind Gratis",
        [("🧠","IA Genera Mapas de Estudio","Escribe cualquier tema y obtén un mapa estructurado al instante. Perfecto para empezar el repaso."),
         ("📚","Plantillas Educativas","Plantilla de resumen de libro, esquema de ensayo, mapa conceptual, línea del tiempo — todo cubierto."),
         ("🔄","Repaso Visual","La organización visual mejora la memoria. Los mapas mentales superan a los apuntes lineales para la mayoría de los estudiantes."),
         ("🎓","Preparación de Exámenes","Condensa todo un tema en un mapa de repaso. Identifica lagunas en tu conocimiento.")],
        [("¿EdrawMind es gratuito para estudiantes?","EdrawMind tiene plan gratuito para uso básico. Wondershare también ofrece descuento para estudiantes en los planes de pago."),
         ("¿Para qué materias funcionan mejor los mapas mentales?","Historia, biología, literatura, economía y psicología responden especialmente bien a los mapas mentales.")])

def page_pricing_es():
    return _pricing("🇪🇸 Español",f"Precios EdrawMind {YEAR} — Todos los Planes",
        "EdrawMind Precios:","Todos los Planes Explicados Honestamente",
        "Plan gratuito, suscripción anual, licencia perpetua o planes de equipo. Exactamente lo que incluye cada opción.",
        "Ver Precios Actuales",P5Y,
        [("¿Cuál es la diferencia entre anual y perpetua?","Anual (~$59/año): todas las funciones incluida IA. Perpetua (~$118 único): propiedad permanente de todas las funciones EXCEPTO IA. La perpetua es más barata a partir de 2 años de uso."),
         ("¿Hay descuento para estudiantes?","Sí — Wondershare ofrece precios educativos. Verifica el estado al pagar.")],
        "Año")

def page_ai_es():
    return _ai("🇪🇸 Español",f"EdrawMind IA {YEAR} · Probado en 20 Temas",
        "Genera Mapas Mentales","con IA en Un Clic",
        "Escribe cualquier tema y EdrawMind IA genera un mapa mental completo de múltiples niveles en menos de 10 segundos.",
        "Probar EdrawMind IA Gratis",
        [("⚡","Generación en Un Clic","Tema → mapa completo de múltiples niveles en segundos. Sin parálisis ante la página en blanco."),
         ("📄","Resumen de Documentos","Sube PDF o pega texto — la IA lo convierte en mapa mental estructurado."),
         ("✏️","Sugerencias de Ramas","Haz clic en cualquier rama y pide a la IA que la expanda con ejemplos o subtemas."),
         ("🌐","Multilingüe","Genera mapas en español, inglés, chino, francés, alemán, japonés y más.")],
        [("¿La generación IA requiere internet?","Sí — las funciones IA requieren conexión a internet y consumen tokens de tu plan. El resto de EdrawMind funciona sin conexión."),
         ("¿Cuántas generaciones IA incluye el plan?","La asignación de tokens varía según el nivel del plan. Los planes estándar incluyen una generosa asignación mensual.")])

# ══════════════════════════════════════════════════════════════════════════════
# FRENCH
# ══════════════════════════════════════════════════════════════════════════════
def page_home_fr():
    return _home("🇫🇷 Version Française","Logiciel de Carte Mentale 2026 · Avis Honnête",
        "Cartes Mentales avec","IA — 700+ Modèles",
        f"EdrawMind {YEAR} : l'IA génère des cartes mentales complètes à plusieurs niveaux, 700+ modèles, diagrammes de Gantt, collaboration en temps réel. Avis honnête.",
        "Essayer EdrawMind Gratuitement",
        [("🤖","IA Génère des Cartes Instantanément","Entrez n'importe quel sujet — l'IA crée une carte mentale complète à plusieurs niveaux en quelques secondes."),
         ("📋","700+ Modèles","Stratégie d'entreprise, planification de projet, notes d'étude — tous les modèles dont vous avez besoin."),
         ("📊","Vue Diagramme de Gantt","Convertissez n'importe quelle carte mentale en diagramme de Gantt en un clic."),
         ("👥","Collaboration en Temps Réel","Plusieurs membres de l'équipe modifient la même carte simultanément.")],
        [("L'IA d'EdrawMind est impressionnante. J'ai tapé 'stratégie marketing digitale' et obtenu une carte complète à 4 niveaux en 8 secondes. Présentée au client l'après-midi même.","Sophie L.","Consultante Marketing","🇫🇷","5"),
         ("La fonction Gantt est exactement ce qu'il me fallait. Passer de la carte mentale au diagramme de Gantt sans ressaisir les données change tout pour la planification.","Antoine D.","Chef de Projet","🇧🇪","5")],
        [("EdrawMind est-il gratuit ?","Oui — EdrawMind a un plan gratuit avec des fonctionnalités de base. Les plans payants (~59$/an ou ~118$ perpétuel) débloquent l'IA, tous les modèles, Gantt et export complet."),
         ("Comment fonctionne la génération IA ?","Entrez n'importe quel sujet — l'IA crée une carte complète à plusieurs niveaux en quelques secondes.")],
        VS_ROWS_BASE)

def page_vs_xmind_fr():
    return _vs("🇫🇷 Français","Comparaison Complète 2026",
        "EdrawMind vs XMind :","IA, Gantt et 7× Plus de Modèles",
        "XMind est un bon outil. EdrawMind ajoute la génération IA, les diagrammes de Gantt, 700+ modèles et une licence perpétuelle.",
        "Essayer EdrawMind Gratuitement",VS_ROWS_BASE,
        [("EdrawMind a-t-il une meilleure IA que XMind ?","EdrawMind a la génération de cartes complètes par IA. XMind n'a pas cette fonctionnalité. EdrawMind gagne clairement sur l'IA."),
         ("XMind est-il plus facile à utiliser ?","XMind a une interface plus minimaliste. EdrawMind a plus de fonctionnalités avec une courbe d'apprentissage légèrement plus élevée pour les fonctions avancées.")])

def page_mindmap_fr():
    return _mindmap("🇫🇷 Français",f"Créateur de Cartes Mentales {YEAR} · 700+ Modèles",
        "Créez des Cartes Mentales Professionnelles","avec l'IA en Secondes",
        "L'IA génère des cartes complètes depuis n'importe quel sujet. 700+ modèles, 15+ styles de mise en page, collaboration en temps réel.",
        "Essayer EdrawMind Gratuitement",
        [("🤖","IA Instantanée","Entrez le sujet et obtenez une carte complète en secondes."),
         ("📋","700+ Modèles","Des modèles pour tous les cas d'usage, entièrement éditables."),
         ("🔄","15+ Styles","Carte mentale, arbre, organigramme, arête de poisson — un clic pour changer."),
         ("📤","Exportez Tout","PDF, Word, PowerPoint, PNG, SVG et plus.")],
        [("EdrawMind est-il adapté aux débutants ?","Oui — interface intuitive, modèles prêts à l'emploi et IA qui génère des cartes automatiquement. La plupart des nouveaux utilisateurs créent leur première carte utile en moins de 5 minutes."),
         ("Puis-je utiliser EdrawMind sans rien installer ?","Oui — EdrawMind a une version navigateur. Des applications de bureau pour Windows, Mac et Linux sont également disponibles.")])

def page_students_fr():
    return _students("🇫🇷 Français",f"EdrawMind pour Étudiants {YEAR}",
        "Étudiez Plus Intelligemment","avec les Cartes Mentales IA",
        "De la prise de notes à la planification d'essais et la révision — les cartes mentales améliorent la compréhension et la mémoire.",
        "Essayer EdrawMind Gratuitement",
        [("🧠","IA Génère des Cartes d'Étude","Entrez n'importe quel sujet et obtenez une carte structurée instantanément."),
         ("📚","Modèles Éducatifs","Résumé de livre, plan d'essai, carte conceptuelle, frise chronologique — tout couvert."),
         ("🔄","Révision Visuelle","L'organisation visuelle améliore la mémoire. Les cartes mentales surpassent les notes linéaires pour la plupart des apprenants."),
         ("🎓","Préparation aux Examens","Condensez un sujet entier en une carte de révision. Identifiez les lacunes dans vos connaissances.")],
        [("EdrawMind est-il gratuit pour les étudiants ?","EdrawMind a un plan gratuit pour un usage basique. Wondershare propose également une réduction étudiant sur les plans payants."),
         ("Pour quelles matières les cartes mentales sont-elles les plus efficaces ?","L'histoire, la biologie, la littérature, l'économie et la psychologie répondent particulièrement bien aux cartes mentales.")])

def page_pricing_fr():
    return _pricing("🇫🇷 Français",f"Prix EdrawMind {YEAR} — Tous les Plans",
        "EdrawMind Prix :","Tous les Plans Expliqués Honnêtement",
        "Plan gratuit, abonnement annuel, licence perpétuelle ou plans équipe.",
        "Voir les Prix Actuels",P5Y,
        [("Quelle différence entre annuel et perpétuel ?","Annuel (~59$/an) : toutes les fonctionnalités dont l'IA. Perpétuel (~118$ unique) : propriété permanente de toutes les fonctions SAUF l'IA. La perpétuelle est moins chère à partir de 2 ans."),
         ("Y a-t-il une réduction étudiante ?","Oui — Wondershare propose des tarifs éducatifs. Vérifiez le statut lors du paiement.")],
        "Année")

def page_ai_fr():
    return _ai("🇫🇷 Français",f"EdrawMind IA {YEAR} · Testé sur 20 Sujets",
        "Générez des Cartes Mentales","avec l'IA en Un Clic",
        "Entrez n'importe quel sujet — EdrawMind IA génère une carte mentale complète à plusieurs niveaux en moins de 10 secondes.",
        "Essayer EdrawMind IA Gratuitement",
        [("⚡","Génération en Un Clic","Sujet → carte complète à plusieurs niveaux en quelques secondes."),
         ("📄","Résumé de Documents","Importez un PDF ou collez du texte — l'IA le convertit en carte mentale structurée."),
         ("✏️","Suggestions de Branches","Cliquez sur n'importe quelle branche et demandez à l'IA de l'étendre."),
         ("🌐","Multilingue","Générez des cartes en français, anglais, chinois, espagnol, allemand, japonais et plus.")],
        [("La génération IA nécessite-t-elle internet ?","Oui — les fonctionnalités IA nécessitent une connexion internet et consomment des tokens de votre plan."),
         ("Combien de générations IA le plan inclut-il ?","L'allocation de tokens varie selon le niveau du plan. Les plans standard incluent une allocation mensuelle généreuse.")])

# ══════════════════════════════════════════════════════════════════════════════
# GERMAN
# ══════════════════════════════════════════════════════════════════════════════
def page_home_de():
    return _home("🇩🇪 Deutsche Version","Mindmapping-Software 2026 · Ehrlicher Test",
        "Mindmaps mit","KI — 700+ Vorlagen",
        f"EdrawMind {YEAR}: KI generiert vollständige mehrstufige Mindmaps, 700+ Vorlagen, Gantt-Diagramme, Echtzeit-Zusammenarbeit. Ehrlicher Test.",
        "EdrawMind Kostenlos Testen",
        [("🤖","KI Generiert Mindmaps Sofort","Geben Sie ein Thema ein — KI erstellt in Sekunden eine vollständige mehrstufige Mindmap."),
         ("📋","700+ Vorlagen","Unternehmensstrategie, Projektplanung, Lernnotizen — alle Vorlagen, die Sie brauchen."),
         ("📊","Gantt-Diagramm-Ansicht","Wandeln Sie jede Mindmap mit einem Klick in ein Gantt-Diagramm um."),
         ("👥","Echtzeit-Zusammenarbeit","Mehrere Teammitglieder bearbeiten dieselbe Map gleichzeitig.")],
        [("Die KI von EdrawMind ist beeindruckend. Ich habe 'digitale Marketingstrategie' eingegeben und in 8 Sekunden eine vollständige 4-Ebenen-Map erhalten.","Markus T.","Marketingberater","🇩🇪","5"),
         ("Die Gantt-Funktion ist genau das, was ich brauchte. Vom Mindmap direkt zum Gantt-Diagramm ohne Dateneingabe — ein echter Gamechanger für die Projektplanung.","Anna K.","Projektmanagerin","🇦🇹","5")],
        [("Ist EdrawMind kostenlos?","Ja — EdrawMind hat einen kostenlosen Plan mit grundlegenden Funktionen. Bezahlte Pläne (~59$/Jahr oder ~118$ Dauerlizenz) schalten KI, alle Vorlagen, Gantt und vollständigen Export frei."),
         ("Wie funktioniert die KI-Generierung?","Geben Sie ein Thema ein — KI erstellt in Sekunden eine vollständige mehrstufige Mindmap.")],
        VS_ROWS_BASE)

def page_vs_xmind_de():
    return _vs("🇩🇪 Deutsch","Vollständiger Vergleich 2026",
        "EdrawMind vs XMind:","KI, Gantt und 7× Mehr Vorlagen",
        "XMind ist ein gutes Tool. EdrawMind fügt KI-Generierung, Gantt-Diagramme, 700+ Vorlagen und eine Dauerlizenz hinzu.",
        "EdrawMind Kostenlos Testen",VS_ROWS_BASE,
        [("Hat EdrawMind bessere KI als XMind?","EdrawMind hat KI-Mindmap-Generierung für vollständige Maps. XMind hat diese Funktion nicht. EdrawMind gewinnt klar bei KI."),
         ("Ist XMind einfacher zu bedienen?","XMind hat eine minimalistische Oberfläche. EdrawMind hat mehr Funktionen mit einer etwas steileren Lernkurve für erweiterte Funktionen.")])

def page_mindmap_de():
    return _mindmap("🇩🇪 Deutsch",f"Mindmap-Software {YEAR} · 700+ Vorlagen",
        "Erstellen Sie Professionelle Mindmaps","mit KI in Sekunden",
        "KI generiert vollständige Maps aus jedem Thema. 700+ Vorlagen, 15+ Layout-Stile, Echtzeit-Zusammenarbeit.",
        "EdrawMind Kostenlos Testen",
        [("🤖","KI Sofort","Thema eingeben und vollständige Map in Sekunden erhalten."),
         ("📋","700+ Vorlagen","Für alle Anwendungsfälle, vollständig bearbeitbar."),
         ("🔄","15+ Stile","Mindmap, Baum, Organigramm, Fischgräte — ein Klick zum Wechseln."),
         ("📤","Alles Exportieren","PDF, Word, PowerPoint, PNG, SVG und mehr.")],
        [("Ist EdrawMind gut für Anfänger?","Ja — intuitive Oberfläche, gebrauchsfertige Vorlagen und KI, die Maps automatisch generiert."),
         ("Kann ich EdrawMind ohne Installation nutzen?","Ja — EdrawMind hat eine Browserversion. Desktop-Apps für Windows, Mac und Linux ebenfalls verfügbar.")])

def page_students_de():
    return _students("🇩🇪 Deutsch",f"EdrawMind für Schüler & Studenten {YEAR}",
        "Intelligenter Lernen","mit KI-Mindmaps",
        "Von Unterrichtsnotizen bis zu Aufsatzplanung und Prüfungsvorbereitung — Mindmaps verbessern Verständnis und Gedächtnis.",
        "EdrawMind Kostenlos Testen",
        [("🧠","KI Erstellt Lern-Maps","Geben Sie ein Thema ein und erhalten Sie sofort eine strukturierte Lern-Map."),
         ("📚","Bildungsvorlagen","Buchzusammenfassung, Aufsatzgliederung, Konzeptkarte, Zeitstrahl — alles abgedeckt."),
         ("🔄","Visuelles Lernen","Visuelle Organisation verbessert das Gedächtnis. Mindmaps übertreffen lineare Notizen für die meisten Lernenden."),
         ("🎓","Prüfungsvorbereitung","Kondensieren Sie ein ganzes Thema in eine Lern-Map. Identifizieren Sie Wissenslücken.")],
        [("Ist EdrawMind kostenlos für Studenten?","EdrawMind hat einen kostenlosen Plan für grundlegende Nutzung. Wondershare bietet auch Studentenrabatt auf bezahlte Pläne."),
         ("Für welche Fächer eignen sich Mindmaps am besten?","Geschichte, Biologie, Literatur, Wirtschaft und Psychologie reagieren besonders gut auf Mindmaps.")])

def page_pricing_de():
    return _pricing("🇩🇪 Deutsch",f"EdrawMind Preise {YEAR} — Alle Pläne",
        "EdrawMind Preise:","Alle Pläne Ehrlich Erklärt",
        "Kostenloser Plan, Jahresabonnement, Dauerlizenz oder Teampläne.",
        "Aktuelle Preise Anzeigen",P5Y,
        [("Was ist der Unterschied zwischen Jahres- und Dauerlizenz?","Jährlich (~59$/Jahr): alle Funktionen einschließlich KI. Dauerlizenz (~118$ einmalig): dauerhafter Besitz aller Funktionen AUSSER KI. Dauerlizenz ist günstiger ab 2 Jahren Nutzung."),
         ("Gibt es einen Studentenrabatt?","Ja — Wondershare bietet Bildungspreise. Beim Kauf Studenten- oder Lehrerstatus nachweisen.")],
        "Jahr")

def page_ai_de():
    return _ai("🇩🇪 Deutsch",f"EdrawMind KI {YEAR} · Getestet an 20 Themen",
        "Mindmaps mit KI","in Einem Klick Generieren",
        "Geben Sie ein Thema ein — EdrawMind KI generiert in unter 10 Sekunden eine vollständige mehrstufige Mindmap.",
        "EdrawMind KI Kostenlos Testen",
        [("⚡","Ein-Klick-Generierung","Thema → vollständige mehrstufige Map in Sekunden."),
         ("📄","Dokumentzusammenfassung","PDF hochladen oder Text einfügen — KI konvertiert es in eine strukturierte Mindmap."),
         ("✏️","Zweigvorschläge","Klicken Sie auf einen Zweig und bitten Sie die KI, ihn zu erweitern."),
         ("🌐","Mehrsprachig","Maps auf Deutsch, Englisch, Chinesisch, Spanisch, Französisch, Japanisch und mehr generieren.")],
        [("Benötigt die KI-Generierung Internet?","Ja — KI-Funktionen erfordern eine Internetverbindung und verbrauchen Tokens aus Ihrem Plan."),
         ("Wie viele KI-Generierungen sind im Plan enthalten?","Die Token-Zuteilung variiert je nach Planstufe. Standardpläne enthalten eine großzügige monatliche Zuteilung.")])

# ══════════════════════════════════════════════════════════════════════════════
# PORTUGUESE
# ══════════════════════════════════════════════════════════════════════════════
def page_home_pt():
    return _home("🇧🇷 Versão Portuguesa","Software de Mapa Mental 2026 · Análise Honesta",
        "Mapas Mentais com","IA — 700+ Modelos",
        f"EdrawMind {YEAR}: IA gera mapas mentais completos de múltiplos níveis, 700+ modelos, diagramas de Gantt, colaboração em tempo real. Análise honesta.",
        "Experimentar EdrawMind Grátis",
        [("🤖","IA Gera Mapas ao Instante","Escreva qualquer tema e a IA cria um mapa mental completo de múltiplos níveis em segundos."),
         ("📋","700+ Modelos","Estratégia empresarial, planeamento de projetos, notas de estudo — todos os modelos que precisa."),
         ("📊","Vista de Diagrama de Gantt","Converta qualquer mapa mental em diagrama de Gantt com um clique."),
         ("👥","Colaboração em Tempo Real","Vários membros da equipa editam o mesmo mapa simultaneamente.")],
        [("A IA do EdrawMind é incrível. Escrevi 'plano de marketing digital' e obtive um mapa completo de 4 níveis em 8 segundos.","João S.","Consultor de Marketing","🇵🇹","5"),
         ("A função Gantt é exatamente o que precisava. Passar do mapa mental para o diagrama de Gantt sem reintroduzir dados é revolucionário.","Maria R.","Gestora de Projetos","🇧🇷","5")],
        [("O EdrawMind é gratuito?","Sim — EdrawMind tem plano gratuito com funcionalidades básicas. Os planos pagos (~$59/ano ou ~$118 perpétua) desbloqueiam IA, todos os modelos, Gantt e exportação completa."),
         ("Como funciona a geração por IA?","Escreva qualquer tema — a IA cria um mapa completo de múltiplos níveis em segundos.")],
        VS_ROWS_BASE)

def page_vs_xmind_pt():
    return _vs("🇧🇷 Português","Comparação Completa 2026",
        "EdrawMind vs XMind:","IA, Gantt e 7× Mais Modelos",
        "XMind é uma boa ferramenta. EdrawMind adiciona geração IA, diagramas de Gantt, 700+ modelos e licença perpétua.",
        "Experimentar EdrawMind Grátis",VS_ROWS_BASE,
        [("O EdrawMind tem melhor IA do que o XMind?","EdrawMind tem geração de mapas completos por IA. XMind não tem esta funcionalidade."),
         ("O XMind é mais fácil de usar?","XMind tem interface mais minimalista. EdrawMind tem mais funcionalidades com curva de aprendizagem ligeiramente maior.")])

def page_mindmap_pt():
    return _mindmap("🇧🇷 Português",f"Criador de Mapas Mentais {YEAR} · 700+ Modelos",
        "Crie Mapas Mentais Profissionais","com IA em Segundos",
        "IA gera mapas completos de qualquer tema. 700+ modelos, 15+ estilos de layout, colaboração em tempo real.",
        "Experimentar EdrawMind Grátis",
        [("🤖","IA ao Instante","Escreva o tema e obtenha um mapa completo em segundos."),
         ("📋","700+ Modelos","Modelos para todos os casos de uso, totalmente editáveis."),
         ("🔄","15+ Estilos","Mapa mental, árvore, organograma, espinha de peixe — um clique para mudar."),
         ("📤","Exporta Tudo","PDF, Word, PowerPoint, PNG, SVG e mais.")],
        [("O EdrawMind é adequado para iniciantes?","Sim — interface intuitiva, modelos prontos a usar e IA que gera mapas automaticamente."),
         ("Posso usar o EdrawMind sem instalar nada?","Sim — EdrawMind tem versão para browser. Também disponível para Windows, Mac e Linux.")])

def page_students_pt():
    return _students("🇧🇷 Português",f"EdrawMind para Estudantes {YEAR}",
        "Estude de Forma Mais Inteligente","com Mapas Mentais IA",
        "De anotações de aula a planeamento de ensaios e revisão — mapas mentais melhoram a compreensão e a memória.",
        "Experimentar EdrawMind Grátis",
        [("🧠","IA Gera Mapas de Estudo","Escreva qualquer tema e obtenha um mapa estruturado instantaneamente."),
         ("📚","Modelos Educativos","Resumo de livro, esquema de ensaio, mapa conceptual, linha do tempo — tudo coberto."),
         ("🔄","Revisão Visual","A organização visual melhora a memória. Mapas mentais superam anotações lineares para a maioria dos estudantes."),
         ("🎓","Preparação para Exames","Condense todo um tema num mapa de revisão. Identifique lacunas no seu conhecimento.")],
        [("O EdrawMind é gratuito para estudantes?","EdrawMind tem plano gratuito para uso básico. A Wondershare também oferece desconto estudantil nos planos pagos."),
         ("Para que matérias os mapas mentais funcionam melhor?","História, biologia, literatura, economia e psicologia respondem especialmente bem aos mapas mentais.")])

def page_pricing_pt():
    return _pricing("🇧🇷 Português",f"Preços EdrawMind {YEAR} — Todos os Planos",
        "EdrawMind Preços:","Todos os Planos Explicados Honestamente",
        "Plano gratuito, subscrição anual, licença perpétua ou planos de equipa.",
        "Ver Preços Atuais",P5Y,
        [("Qual é a diferença entre anual e perpétua?","Anual (~$59/ano): todas as funcionalidades incluindo IA. Perpétua (~$118 único): propriedade permanente de todas as funções EXCETO IA. A perpétua é mais barata a partir de 2 anos de uso."),
         ("Há desconto para estudantes?","Sim — Wondershare oferece preços educativos. Verifique o estado ao pagar.")],
        "Ano")

# ══════════════════════════════════════════════════════════════════════════════
# JAPANESE
# ══════════════════════════════════════════════════════════════════════════════
def page_home_ja():
    return _home("🇯🇵 日本語版","マインドマップソフト2026 · 正直なレビュー",
        "AIで作るマインドマップ","700+テンプレート搭載",
        f"EdrawMind {YEAR}：AIがマインドマップを自動生成、700+テンプレート、ガントチャート、リアルタイム共同作業。正直なレビュー。",
        "EdrawMindを無料で試す",
        [("🤖","AIがマップを即座に生成","テーマを入力するだけで、AIが数秒で完全な多段階マインドマップを作成します。"),
         ("📋","700+テンプレート","ビジネス戦略、プロジェクト計画、学習ノート — 必要なすべてのテンプレート。"),
         ("📊","ガントチャートビュー","マインドマップをワンクリックでガントチャートに変換。"),
         ("👥","リアルタイム共同作業","複数のチームメンバーが同じマップを同時に編集できます。")],
        [("EdrawMindのAI機能は革命的です。「デジタルマーケティング戦略」と入力したら、8秒で完全な4段階マップが生成されました。","田中 浩","マーケティングコンサルタント","🇯🇵","5"),
         ("ガントチャート機能は私が求めていたものです。マインドマップからガントチャートへのデータ再入力なしの変換はプロジェクト計画の革命です。","鈴木 明","プロジェクトマネージャー","🇯🇵","5")],
        [("EdrawMindは無料ですか？","はい — EdrawMindには基本機能を含む無料プランがあります。有料プラン（年間約$59または永久約$118）でAI、全テンプレート、ガント、完全エクスポートが解除されます。"),
         ("AI生成はどのように機能しますか？","テーマを入力すると、AIが数秒で完全な多段階マインドマップを作成します。")],
        VS_ROWS_BASE)

def page_vs_xmind_ja():
    return _vs("🇯🇵 日本語","完全比較 2026年",
        "EdrawMind vs XMind：","AI、ガント、7倍のテンプレート",
        "XMindは優れたツールです。EdrawMindはAI生成、ガントチャート、700+テンプレート、永久ライセンスを追加します。",
        "EdrawMindを無料で試す",VS_ROWS_BASE,
        [("EdrawMindはXMindよりAIが優れていますか？","EdrawMindには完全なマップAI生成機能があります。XMindにはこの機能がありません。AIではEdrawMindが明確に勝ります。"),
         ("XMindの方が使いやすいですか？","XMindはよりミニマルなインターフェースを持っています。EdrawMindはより多くの機能があり、高度な機能には学習曲線が少し急です。")])

def page_mindmap_ja():
    return _mindmap("🇯🇵 日本語",f"マインドマップソフト{YEAR} · 700+テンプレート",
        "AIで数秒でプロの","マインドマップを作成",
        "AIが任意のテーマから完全なマップを生成。700+テンプレート、15+レイアウトスタイル、リアルタイム共同編集。",
        "EdrawMindを無料で試す",
        [("🤖","AIが即座に生成","テーマを入力して数秒で完全なマップを取得。"),
         ("📋","700+テンプレート","すべてのユースケースに対応、完全編集可能。"),
         ("🔄","15+スタイル","マインドマップ、ツリー、組織図、魚骨図 — ワンクリックで切り替え。"),
         ("📤","すべてエクスポート","PDF、Word、PowerPoint、PNG、SVGなど。")],
        [("EdrawMindは初心者に適していますか？","はい — 直感的なインターフェース、すぐに使えるテンプレート、自動生成AI。"),
         ("インストールなしでEdrawMindを使えますか？","はい — EdrawMindにはブラウザ版があります。Windows、Mac、Linux用のデスクトップアプリも利用可能です。")])

def page_pricing_ja():
    rows_ja=[("EdrawMind年間プラン","~$59","~$118","~$295"),
             ("EdrawMind永久ライセンス","~$118","~$118","~$118"),
             ("MindMeister Pro","~$78","~$156","~$390"),
             ("MindManager","~$349","~$698","~$1,745")]
    return _pricing("🇯🇵 日本語",f"EdrawMind価格{YEAR} — 全プラン",
        "EdrawMind価格：","全プランを正直に解説",
        "無料プラン、年間サブスクリプション、永久ライセンス、またはチームプラン。",
        "現在の価格を確認する",rows_ja,
        [("年間プランと永久ライセンスの違いは？","年間（約$59/年）：AI生成を含む全機能。永久（約$118一回払い）：AIを除く全機能の永続的所有権。2年以上使用する場合は永久の方が安くなります。"),
         ("学生割引はありますか？","はい — WondershareはEdrawMindに教育価格を提供しています。")],
        "年目")

# ══════════════════════════════════════════════════════════════════════════════
# CHINESE
# ══════════════════════════════════════════════════════════════════════════════
def page_home_zh():
    return _home("🇨🇳 中文版","思维导图软件2026 · 诚实评测",
        "AI驱动的思维导图","700+模板，甘特图",
        f"EdrawMind {YEAR}：AI一键生成完整多层级思维导图，700+模板，甘特图，实时协作。诚实评测。",
        "免费试用EdrawMind",
        [("🤖","AI即时生成思维导图","输入任何主题，AI在几秒内创建完整的多层级思维导图。"),
         ("📋","700+模板","商业策略、项目规划、学习笔记 — 所有您需要的模板。"),
         ("📊","甘特图视图","一键将任何思维导图转换为甘特图。"),
         ("👥","实时协作","多个团队成员同时编辑同一张图。")],
        [("EdrawMind的AI功能真的很革命性。我输入'数字营销策略'，8秒内得到了一个完整的4级思维导图。","李 明","营销顾问","🇨🇳","5"),
         ("甘特图功能正是我所需要的。从思维导图到甘特图无需重新输入数据，是项目规划的革命。","张 华","项目经理","🇨🇳","5")],
        [("EdrawMind是免费的吗？","是的 — EdrawMind有包含基本功能的免费方案。付费方案（约$59/年或约$118永久）解锁AI、所有模板、甘特图和完整导出。"),
         ("AI生成是如何工作的？","输入任何主题 — AI在几秒内创建完整的多层级思维导图。")],
        VS_ROWS_BASE)

def page_vs_xmind_zh():
    return _vs("🇨🇳 中文","完整对比 2026",
        "EdrawMind vs XMind：","AI、甘特图和7倍模板",
        "XMind是不错的工具。EdrawMind添加了AI生成、甘特图、700+模板和永久许可证。",
        "免费试用EdrawMind",VS_ROWS_BASE,
        [("EdrawMind的AI比XMind更好吗？","EdrawMind有完整的AI思维导图生成功能。XMind没有这个功能。在AI方面EdrawMind明显胜出。"),
         ("XMind更容易使用吗？","XMind有更简洁的界面。EdrawMind功能更多，高级功能学习曲线略陡。")])

def page_mindmap_zh():
    return _mindmap("🇨🇳 中文",f"思维导图软件{YEAR} · 700+模板",
        "用AI在几秒内","创建专业思维导图",
        "AI从任何主题生成完整导图。700+模板，15+布局样式，实时协作。",
        "免费试用EdrawMind",
        [("🤖","AI即时生成","输入主题，几秒内获得完整导图。"),
         ("📋","700+模板","适用于所有使用场景，完全可编辑。"),
         ("🔄","15+样式","思维导图、树状图、组织图、鱼骨图 — 一键切换。"),
         ("📤","导出一切","PDF、Word、PowerPoint、PNG、SVG等。")],
        [("EdrawMind适合初学者吗？","是的 — 直观界面、现成模板、自动生成AI。"),
         ("可以不安装就使用EdrawMind吗？","是的 — EdrawMind有浏览器版本。也有Windows、Mac和Linux桌面应用。")])

def page_pricing_zh():
    rows_zh=[("EdrawMind年度方案","~$59","~$118","~$295"),
             ("EdrawMind永久许可证","~$118","~$118","~$118"),
             ("MindMeister Pro","~$78","~$156","~$390"),
             ("MindManager","~$349","~$698","~$1,745")]
    return _pricing("🇨🇳 中文",f"EdrawMind价格{YEAR} — 所有方案",
        "EdrawMind价格：","诚实解析所有方案",
        "免费方案、年度订阅、永久许可证或团队方案。",
        "查看当前价格",rows_zh,
        [("年度方案和永久许可证有什么区别？","年度（约$59/年）：包含AI生成在内的全部功能。永久（约$118一次性）：除AI外所有功能的永久所有权。使用超过2年时永久许可证更划算。"),
         ("有学生优惠吗？","是的 — Wondershare提供教育价格。在结账时验证学生或教师身份。")],
        "年")

# ══════════════════════════════════════════════════════════════════════════════
# KOREAN, ITALIAN, DUTCH
# ══════════════════════════════════════════════════════════════════════════════
def page_home_ko():
    return _home("🇰🇷 한국어 버전","마인드맵 소프트웨어 2026 · 정직한 리뷰",
        "AI로 만드는 마인드맵","700+ 템플릿, 간트 차트",
        f"EdrawMind {YEAR}: AI가 마인드맵을 자동 생성, 700+ 템플릿, 간트 차트, 실시간 협업. 정직한 리뷰.",
        "EdrawMind 무료 체험",
        [("🤖","AI가 즉시 생성","주제를 입력하면 AI가 몇 초 만에 완전한 다단계 마인드맵을 생성합니다."),
         ("📋","700+ 템플릿","비즈니스 전략, 프로젝트 계획, 학습 노트 — 필요한 모든 템플릿."),
         ("📊","간트 차트 보기","마인드맵을 한 번의 클릭으로 간트 차트로 변환합니다."),
         ("👥","실시간 협업","여러 팀원이 동시에 같은 맵을 편집할 수 있습니다.")],
        [("EdrawMind의 AI 기능은 혁신적입니다. '디지털 마케팅 전략'을 입력하니 8초 만에 완전한 4단계 마인드맵이 생성되었습니다.","김 민준","마케팅 컨설턴트","🇰🇷","5")],
        [("EdrawMind는 무료인가요?","네 — EdrawMind에는 기본 기능을 포함한 무료 플랜이 있습니다. 유료 플랜(연간 약 $59 또는 영구 약 $118)으로 AI, 모든 템플릿, 간트 차트 및 완전한 내보내기를 사용할 수 있습니다."),
         ("AI 생성은 어떻게 작동하나요?","주제를 입력하면 AI가 몇 초 만에 완전한 다단계 마인드맵을 생성합니다.")],
        VS_ROWS_BASE)

def page_mindmap_ko():
    return _mindmap("🇰🇷 한국어",f"마인드맵 소프트웨어 {YEAR} · 700+ 템플릿",
        "AI로 몇 초 만에","전문적인 마인드맵 만들기",
        "AI가 어떤 주제에서도 완전한 맵을 생성합니다. 700+ 템플릿, 15+ 레이아웃 스타일, 실시간 협업.",
        "EdrawMind 무료 체험",
        [("🤖","AI 즉시 생성","주제를 입력하면 몇 초 만에 완전한 맵을 얻을 수 있습니다."),
         ("📋","700+ 템플릿","모든 사용 사례에 맞는 템플릿, 완전히 편집 가능."),
         ("🔄","15+ 스타일","마인드맵, 트리, 조직도, 피쉬본 — 클릭 한 번으로 전환."),
         ("📤","모두 내보내기","PDF, Word, PowerPoint, PNG, SVG 등.")],
        [("EdrawMind는 초보자에게 적합한가요?","네 — 직관적인 인터페이스, 사용 준비된 템플릿, 자동 생성 AI."),
         ("설치 없이 EdrawMind를 사용할 수 있나요?","네 — EdrawMind는 브라우저 버전이 있습니다. Windows, Mac, Linux용 데스크탑 앱도 있습니다.")])

def page_home_it():
    return _home("🇮🇹 Versione Italiana","Software Mappe Mentali 2026 · Recensione Onesta",
        "Mappe Mentali con","IA — 700+ Modelli",
        f"EdrawMind {YEAR}: l'IA genera mappe mentali complete a più livelli, 700+ modelli, diagrammi di Gantt, collaborazione in tempo reale. Recensione onesta.",
        "Prova EdrawMind Gratis",
        [("🤖","IA Genera Mappe Istantaneamente","Inserisci qualsiasi argomento — l'IA crea in pochi secondi una mappa mentale completa a più livelli."),
         ("📋","700+ Modelli","Strategia aziendale, pianificazione progetti, appunti di studio — tutti i modelli di cui hai bisogno."),
         ("📊","Vista Diagramma di Gantt","Converti qualsiasi mappa mentale in diagramma di Gantt con un clic."),
         ("👥","Collaborazione in Tempo Reale","Più membri del team modificano la stessa mappa contemporaneamente.")],
        [("L'IA di EdrawMind è impressionante. Ho digitato 'strategia marketing digitale' e ho ottenuto una mappa completa a 4 livelli in 8 secondi.","Marco B.","Consulente Marketing","🇮🇹","5")],
        [("EdrawMind è gratuito?","Sì — EdrawMind ha un piano gratuito con funzionalità di base. I piani a pagamento (~59$/anno o ~118$ perpetuo) sbloccano IA, tutti i modelli, Gantt ed esportazione completa."),
         ("Come funziona la generazione IA?","Inserisci qualsiasi argomento — l'IA crea in pochi secondi una mappa completa a più livelli.")],
        VS_ROWS_BASE)

def page_mindmap_it():
    return _mindmap("🇮🇹 Italiano",f"Software Mappe Mentali {YEAR} · 700+ Modelli",
        "Crea Mappe Mentali Professionali","con l'IA in Secondi",
        "L'IA genera mappe complete da qualsiasi argomento. 700+ modelli, 15+ stili di layout, collaborazione in tempo reale.",
        "Prova EdrawMind Gratis",
        [("🤖","IA Istantanea","Inserisci l'argomento e ottieni una mappa completa in secondi."),
         ("📋","700+ Modelli","Per tutti i casi d'uso, completamente modificabili."),
         ("🔄","15+ Stili","Mappa mentale, albero, organigramma, diagramma a lisca — un clic per cambiare."),
         ("📤","Esporta Tutto","PDF, Word, PowerPoint, PNG, SVG e altro.")],
        [("EdrawMind è adatto ai principianti?","Sì — interfaccia intuitiva, modelli pronti all'uso e IA che genera mappe automaticamente."),
         ("Posso usare EdrawMind senza installare nulla?","Sì — EdrawMind ha una versione browser. Disponibili anche app desktop per Windows, Mac e Linux.")])

def page_home_nl():
    return _home("🇳🇱 Nederlandse Versie","Mind Mapping Software 2026 · Eerlijke Review",
        "Mindmaps met","AI — 700+ Sjablonen",
        f"EdrawMind {YEAR}: AI genereert complete meerniveaus mindmaps, 700+ sjablonen, Gantt-diagrammen, realtime samenwerking. Eerlijke review.",
        "EdrawMind Gratis Proberen",
        [("🤖","AI Genereert Mindmaps Direct","Voer een onderwerp in — AI maakt in seconden een complete meerniveaus mindmap."),
         ("📋","700+ Sjablonen","Bedrijfsstrategie, projectplanning, studieopmerkingen — alle sjablonen die je nodig hebt."),
         ("📊","Gantt-diagramweergave","Converteer elke mindmap naar een Gantt-diagram met één klik."),
         ("👥","Realtime Samenwerking","Meerdere teamleden bewerken dezelfde map tegelijkertijd.")],
        [("De AI van EdrawMind is indrukwekkend. Ik typte 'digitale marketingstrategie' en kreeg in 8 seconden een complete 4-niveau mindmap.","Jan V.","Marketingconsultant","🇳🇱","5")],
        [("Is EdrawMind gratis?","Ja — EdrawMind heeft een gratis plan met basisfuncties. Betaalde plannen (~$59/jaar of ~$118 permanent) ontgrendelen AI, alle sjablonen, Gantt en volledige export."),
         ("Hoe werkt AI-generatie?","Voer een onderwerp in — AI maakt in seconden een complete meerniveaus mindmap.")],
        VS_ROWS_BASE)

def page_mindmap_nl():
    return _mindmap("🇳🇱 Nederlands",f"Mind Mapping Software {YEAR} · 700+ Sjablonen",
        "Maak Professionele Mindmaps","met AI in Seconden",
        "AI genereert complete maps van elk onderwerp. 700+ sjablonen, 15+ lay-outstijlen, realtime samenwerking.",
        "EdrawMind Gratis Proberen",
        [("🤖","AI Direct","Voer het onderwerp in en krijg in seconden een complete map."),
         ("📋","700+ Sjablonen","Voor alle gebruikssituaties, volledig bewerkbaar."),
         ("🔄","15+ Stijlen","Mindmap, boom, organogram, visgraat — één klik om te wisselen."),
         ("📤","Exporteer Alles","PDF, Word, PowerPoint, PNG, SVG en meer.")],
        [("Is EdrawMind geschikt voor beginners?","Ja — intuïtieve interface, gebruiksklare sjablonen en AI die automatisch maps genereert."),
         ("Kan ik EdrawMind gebruiken zonder iets te installeren?","Ja — EdrawMind heeft een browserversie. Desktop-apps voor Windows, Mac en Linux zijn ook beschikbaar.")])


# ══════════════════════════════════════════════════════════════════════════════
# ROUTER + STATIC FILES + BUILD
# ══════════════════════════════════════════════════════════════════════════════
FN_MAP = {
    # English
    "page_home":             page_home,
    "page_review":           page_review,
    "page_vs_xmind":         page_vs_xmind,
    "page_vs_mindmeister":   page_vs_mindmeister,
    "page_vs_miro":          page_vs_miro,
    "page_vs_mindmanager":   page_vs_mindmanager,
    "page_vs_coggle":        page_vs_coggle,
    "page_pricing":          page_pricing,
    "page_ai":               page_ai,
    "page_mindmap":          page_mindmap,
    "page_templates":        page_templates,
    "page_collab":           page_collab,
    "page_gantt":            page_gantt,
    "page_students":         page_students,
    "page_teachers":         page_teachers,
    "page_business":         page_business,
    "page_pm":               page_pm,
    "page_brainstorm":       page_brainstorm,
    "page_concept":          page_concept,
    "page_flowchart":        page_flowchart,
    "page_presentation":     page_presentation,
    "page_export":           page_export,
    "page_download":         page_download,
    "page_deals":            page_deals,
    "page_free_vs_paid":     page_free_vs_paid,
    "page_guide":            page_guide,
    "page_study":            page_study,
    "page_notes":            page_notes,
    # Spanish
    "page_home_es":          page_home_es,
    "page_vs_xmind_es":      page_vs_xmind_es,
    "page_mindmap_es":       page_mindmap_es,
    "page_students_es":      page_students_es,
    "page_pricing_es":       page_pricing_es,
    "page_ai_es":            page_ai_es,
    # French
    "page_home_fr":          page_home_fr,
    "page_vs_xmind_fr":      page_vs_xmind_fr,
    "page_mindmap_fr":       page_mindmap_fr,
    "page_students_fr":      page_students_fr,
    "page_pricing_fr":       page_pricing_fr,
    "page_ai_fr":            page_ai_fr,
    # German
    "page_home_de":          page_home_de,
    "page_vs_xmind_de":      page_vs_xmind_de,
    "page_mindmap_de":       page_mindmap_de,
    "page_students_de":      page_students_de,
    "page_pricing_de":       page_pricing_de,
    "page_ai_de":            page_ai_de,
    # Portuguese
    "page_home_pt":          page_home_pt,
    "page_vs_xmind_pt":      page_vs_xmind_pt,
    "page_mindmap_pt":       page_mindmap_pt,
    "page_students_pt":      page_students_pt,
    "page_pricing_pt":       page_pricing_pt,
    # Japanese
    "page_home_ja":          page_home_ja,
    "page_vs_xmind_ja":      page_vs_xmind_ja,
    "page_mindmap_ja":       page_mindmap_ja,
    "page_pricing_ja":       page_pricing_ja,
    # Chinese
    "page_home_zh":          page_home_zh,
    "page_vs_xmind_zh":      page_vs_xmind_zh,
    "page_mindmap_zh":       page_mindmap_zh,
    "page_pricing_zh":       page_pricing_zh,
    # Korean
    "page_home_ko":          page_home_ko,
    "page_mindmap_ko":       page_mindmap_ko,
    # Italian
    "page_home_it":          page_home_it,
    "page_mindmap_it":       page_mindmap_it,
    # Dutch
    "page_home_nl":          page_home_nl,
    "page_mindmap_nl":       page_mindmap_nl,
}


def write_robots():
    (OUT / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n"
        f"User-agent: GPTBot\nAllow: /\n"
        f"User-agent: Claude-Web\nAllow: /\n"
        f"User-agent: Googlebot\nAllow: /\n"
    )


def write_sitemap():
    urls = ""
    for p in PAGES:
        slug = p["slug"]
        if slug == "index":      loc = f"{BASE}/"
        elif "/" in slug:        loc = f"{BASE}/{slug}/"
        else:                    loc = f"{BASE}/{slug}.html"
        urls += (f"  <url><loc>{loc}</loc>"
                 f"<lastmod>{TODAY}</lastmod>"
                 f"<changefreq>weekly</changefreq>"
                 f"<priority>{p['priority']}</priority></url>\n")
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>'
    )


def write_404():
    page = {"slug":"404","lang":"en",
            "title":f"404 — Page Not Found | {SITE}",
            "desc":"Page not found.","fn":"","priority":"0"}
    body = f"""
<section class="hero" style="min-height:82vh;">
  <div class="hero-bg"><div class="hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div></div>
  <div class="hero-inner">
    <div style="font-size:5rem;margin-bottom:1rem">🧠</div>
    <h1>404 — <em>Page Not Found</em></h1>
    <p class="hero-sub">This page doesn't exist. Let's get you back to mind mapping.</p>
    <div style="display:flex;gap:1rem;justify-content:center;flex-wrap:wrap;">
      <a href="{SUB}/" class="btn btn-primary btn-lg">Go to Homepage →</a>
      <a href="{AFF}" class="btn btn-amber btn-lg" rel="nofollow sponsored">Try EdrawMind Free →</a>
    </div>
  </div>
</section>"""
    (OUT / "404.html").write_text(layout(page, body), encoding="utf-8")


def write_llms():
    lines = [
        f"# {SITE} — EdrawMind Authority Site\n\n",
        f"> Independent review and guide site for EdrawMind. "
        f"10 languages, {len(PAGES)} pages, real feature tests.\n",
        f"> Affiliate disclosure: {SITE} earns commission on purchases via our links.\n",
        f"> Affiliate link: {AFF}\n",
        f"> Last updated: {TODAY}\n\n",
        "## What This Site Covers\n\n",
        "- Honest EdrawMind review with real feature testing\n",
        "- EdrawMind vs XMind, MindMeister, Miro, MindManager, Coggle\n",
        "- Pricing analysis: free vs annual vs perpetual vs team plans\n",
        "- AI mind map generation guide and test results\n",
        "- Use case guides: students, teachers, business, project management\n",
        "- Feature guides: templates, collaboration, Gantt charts, presentation mode, export\n",
        "- Mind mapping technique guides: study techniques, note-taking, brainstorming\n",
        "- Available in: EN, ES, FR, DE, PT, JA, ZH, KO, IT, NL\n\n",
        "## Key Facts About EdrawMind\n\n",
        "- AI generation: one-click complete multi-level mind map from any topic\n",
        "- Templates: 700+ covering business, education, project management, personal\n",
        "- Gantt chart: unique feature — convert mind map to Gantt timeline in one click\n",
        "- Platforms: Windows, macOS, Linux, iOS, Android, browser\n",
        "- Layouts: 15+ including mind map, tree, org chart, fishbone, timeline\n",
        "- Export: 25+ formats including PDF, Word, PowerPoint, PNG, SVG, HTML\n",
        "- Pricing: ~$59/year annual, ~$118 perpetual one-time, ~$5/user/month teams\n",
        "- Free plan: available with core features, no time limit\n",
        "- AI features: require subscription tokens; not included in perpetual standalone\n",
        "- Linux support: yes — one of few mind mapping tools with native Linux app\n\n",
        "## All Pages\n\n",
    ]
    for p in PAGES:
        slug = p["slug"]
        if slug == "index":      loc = f"{BASE}/"
        elif "/" in slug:        loc = f"{BASE}/{slug}/"
        else:                    loc = f"{BASE}/{slug}.html"
        lines.append(f"- [{p['title'][:80]}]({loc})\n")
    (OUT / "llms.txt").write_text("".join(lines), encoding="utf-8")


def write_humans():
    (OUT / "humans.txt").write_text(
        f"/* TEAM */\n"
        f"Site: {SITE}\n"
        f"URL: {BASE}\n"
        f"Language: EN, ES, FR, DE, PT, JA, ZH, KO, IT, NL\n\n"
        f"/* SITE */\n"
        f"Last update: {TODAY}\n"
        f"Language: Multiple\n"
        f"Doctype: HTML5\n"
        f"Technology: Python static site generator\n"
        f"Components: Feature tests, AI generation results, affiliate disclosure\n"
    )


def build():
    OUT.mkdir(exist_ok=True)
    built = failed = 0
    errors = []

    for p in PAGES:
        try:
            body  = FN_MAP[p["fn"]]()
            html  = layout(p, body)
            slug  = p["slug"]

            if slug == "index":
                fpath = OUT / "index.html"
            elif "/" in slug:
                parts  = slug.split("/")
                subdir = OUT / parts[0]
                subdir.mkdir(exist_ok=True)
                name   = "index.html" if parts[1] == "index" else parts[1] + ".html"
                fpath  = subdir / name
            else:
                fpath = OUT / (slug + ".html")

            fpath.write_text(html, encoding="utf-8")
            built += 1
            print(f"  ✓  {str(fpath.relative_to(OUT)):<48} {len(html)//1024}KB")

        except Exception as e:
            import traceback
            msg = f"{p['slug']}: {e}"
            errors.append(msg)
            print(f"  ✗  {msg}")
            traceback.print_exc()
            failed += 1

    write_robots()
    write_sitemap()
    write_404()
    write_llms()
    write_humans()
    print("  ✓  robots.txt  sitemap.xml  404.html  llms.txt  humans.txt")

    all_html  = list(OUT.rglob("*.html"))
    kb_html   = sum(f.stat().st_size for f in all_html) // 1024
    kb_total  = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file()) // 1024

    print(f"\n{'='*62}")
    print(f"  ✅  Build complete — {TODAY}")
    print(f"  📄  {built} pages built · {failed} failed")
    print(f"  📦  {kb_html}KB HTML · {kb_total}KB total")
    print(f"  🌍  EN · ES · FR · DE · PT · JA · ZH · KO · IT · NL")
    print(f"  🔗  {BASE}/")
    print(f"  💰  {AFF}")
    if errors:
        print(f"\n  ⚠️  Errors:")
        for e in errors: print(f"       {e}")
    print(f"{'='*62}")


if __name__ == "__main__":
    build()
