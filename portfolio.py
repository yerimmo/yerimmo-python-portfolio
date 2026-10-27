import streamlit as st
from html import escape

st.set_page_config(page_title="Yerim Mo | Strategy, Analytics & AI", page_icon="💠", layout="wide", initial_sidebar_state="collapsed")

NAVY = "#0B1120"
CARD = "#111827"
BORDER = "#243247"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"
TEAL = "#5EEAD4"

st.markdown("""
<style>
:root {color-scheme:dark;}
html {scroll-behavior:smooth;}
.stApp, [data-testid="stAppViewContainer"] {background:#0B1120;color:#E2E8F0;}
[data-testid="stHeader"] {background:rgba(11,17,32,.75);backdrop-filter:blur(14px);}
[data-testid="stToolbar"] {opacity:.65;}
.block-container {max-width:1180px;padding-top:1.2rem;padding-bottom:5rem;}
section[data-testid="stSidebar"] {background:#111827;}
#MainMenu, footer {visibility:hidden;}
.hero {padding:5rem 0 3rem;position:relative;}
.eyebrow {font-size:.77rem;letter-spacing:.15em;text-transform:uppercase;font-weight:750;color:#5EEAD4;margin-bottom:1.1rem;}
.hero-title {font-size:clamp(3.1rem,7vw,5.5rem);letter-spacing:-.065em;line-height:1.06;font-weight:820;color:#F8FAFC;margin:0 0 1.1rem;}
.hero-title span {color:#5EEAD4;}
.hero-lede {max-width:790px;font-size:clamp(1.13rem,2.2vw,1.55rem);line-height:1.6;color:#CBD5E1;margin-bottom:1.7rem;}
.nav {position:relative;display:flex;justify-content:space-between;align-items:center;gap:1rem;border-bottom:1px solid #263449;padding:1.2rem 0;flex-wrap:wrap;background:rgba(11,17,32,.96);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);}
/* Make the Streamlit wrapper sticky, not just the HTML nav. */
[data-testid="stElementContainer"]:has(.nav) {
  position: sticky !important;
  top: 0 !important;
  z-index: 999 !important;
  background: #0B1120 !important;
}
.brand {font-weight:850;letter-spacing:-.05em;font-size:1.5rem;color:#5EEAD4;}
.nav-links {display:flex;gap:1.55rem;flex-wrap:wrap;}
.nav-links a {color:#CBD5E1;text-decoration:none;font-size:.89rem;font-weight:650;}
.nav-links a:hover {color:#5EEAD4;}
.pill-row {display:flex;gap:.7rem;flex-wrap:wrap;margin:1.3rem 0;}
.cta {display:inline-block;text-decoration:none!important;padding:.83rem 1.2rem;border-radius:9px;font-weight:750;font-size:.93rem;transition:transform .2s,border-color .2s;}
.cta:hover {transform:translateY(-2px);}
.cta.primary {background:#5EEAD4;color:#0B1120!important;}
.cta.secondary {border:1px solid #42556B;color:#E2E8F0!important;background:#111827;}
.section {padding-top:3.7rem;margin-top:2.2rem;border-top:1px solid #263449;scroll-margin-top:6rem;}
.section-title {font-size:clamp(1.8rem,3vw,2.35rem);letter-spacing:-.04em;color:#F8FAFC;font-weight:800;margin:.3rem 0 1.1rem;}
.section-desc {color:#A7B5C8;max-width:790px;line-height:1.7;margin-bottom:1.7rem;}
.stat-grid {display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:1rem;margin-top:2.6rem;}
.stat {border:1px solid #263449;background:linear-gradient(145deg,#111E30,#111827);padding:1.4rem;border-radius:15px;min-height:165px;}
.stat .value {color:#5EEAD4;font-size:2.35rem;font-weight:850;letter-spacing:-.055em;line-height:1.25;}
.stat .name {font-size:.89rem;font-weight:700;color:#F1F5F9;margin:.55rem 0 .35rem;}
.stat .note {font-size:.78rem;color:#94A3B8;line-height:1.45;}
.about-grid {display:grid;grid-template-columns:1.7fr 1fr;gap:3rem;}
.about-copy p {font-size:1.03rem;line-height:1.85;color:#CBD5E1;margin:0 0 1.1rem;}
.skill-group {margin-bottom:1.5rem;}
.skill-label {font-size:.76rem;letter-spacing:.11em;color:#5EEAD4;font-weight:800;margin-bottom:.6rem;}
.tags {display:flex;flex-wrap:wrap;gap:.45rem;}
.tag {display:inline-block;border:1px solid #2B4650;color:#A7E9DE;background:#122C35;padding:.35rem .68rem;border-radius:999px;font-size:.76rem;font-weight:600;}
.timeline {border-left:1px solid #2B4C56;margin-left:.55rem;padding-left:1.6rem;}
.job {position:relative;padding:0 0 2.3rem;}
.job:before {content:'';position:absolute;left:-2.03rem;top:.35rem;width:11px;height:11px;background:#5EEAD4;border-radius:50%;box-shadow:0 0 0 5px #12313B;}
.job-date {color:#94A3B8;font-size:.78rem;letter-spacing:.08em;font-weight:650;}
.job-title {font-size:1.2rem;color:#F1F5F9;font-weight:750;margin:.55rem 0 .25rem;}
.job-company {color:#5EEAD4;font-weight:650;font-size:.92rem;}
.job ul {padding-left:1.2rem;margin:.8rem 0 0;}
.job li {color:#C4D0DF;line-height:1.72;margin-bottom:.48rem;font-size:.92rem;}
.featured {border:1px solid #27615F;background:linear-gradient(120deg,#12303D 0%,#111827 72%);padding:2rem;border-radius:18px;margin:1.3rem 0 1.6rem;}
.featured .project-title {font-size:1.7rem;}
.project-grid {display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;}
.project {border:1px solid #263449;background:#111827;padding:1.5rem;border-radius:15px;display:flex;flex-direction:column;min-height:270px;}
.project-meta {color:#94A3B8;font-size:.73rem;letter-spacing:.055em;font-weight:650;text-transform:uppercase;}
.project-title {color:#F1F5F9;font-size:1.17rem;font-weight:780;line-height:1.35;margin:.8rem 0;}
.project-desc {color:#BBC8D8;line-height:1.7;font-size:.9rem;margin-bottom:1.1rem;}
.project-actions {display:flex;flex-wrap:wrap;gap:.7rem;margin-top:auto;padding-top:1.2rem;}
.project-actions a {text-decoration:none!important;color:#5EEAD4!important;font-weight:720;font-size:.88rem;}
.project-actions a:hover {text-decoration:underline!important;}
.planned {opacity:.76;border-style:dashed;}
.contact-panel {border:1px solid #285459;background:linear-gradient(125deg,#102C38,#111827);padding:2.3rem;border-radius:18px;}
.contact-panel p {color:#CBD5E1;line-height:1.7;max-width:760px;}
.site-footer {margin-top:3rem;padding-top:1.5rem;border-top:1px solid #263449;color:#94A3B8;font-size:.83rem;}
[data-testid="stSegmentedControl"] button {border-color:#2C4253!important;}
[data-testid="stSegmentedControl"] button[aria-checked="true"], [data-testid="stSegmentedControl"] button[aria-pressed="true"], [data-testid="stSegmentedControl"] button[data-state="active"] {background:#164C4A!important;color:#5EEAD4!important;border-color:#5EEAD4!important;box-shadow:inset 0 0 0 1px #5EEAD4!important;}
[data-testid="stSegmentedControl"] button:focus-visible {outline:2px solid #5EEAD4!important;outline-offset:2px;}
[data-testid="stSegmentedControl"] button:hover {border-color:#5EEAD4!important;color:#5EEAD4!important;}
@media(max-width:760px) {.nav{padding:.9rem 0}.nav-links{gap:.8rem}.hero{padding:3.2rem 0 1.6rem}.stat-grid{grid-template-columns:repeat(2,1fr)}.about-grid,.project-grid{grid-template-columns:1fr}.nav-links{gap:.8rem}.featured{padding:1.4rem}.contact-panel{padding:1.4rem}}
</style>
""", unsafe_allow_html=True)

ABOUT = ['My career connects communication, business strategy, and analytics. After studying Journalism and '
 'Public Relations at Boston University, I joined Hyundai Department Store, where I used Excel and '
 'internal analytics platforms to turn customer insights into loyalty strategies, operational '
 'decisions, and measurable business outcomes.',
 'I also collaborated with IT and CRM teams to validate eligibility lists and troubleshoot tier '
 "assignments during a VIP program launch. Now at Emory Goizueta, I'm developing deeper skills in "
 'Python, SQL, R, and AI-assisted development to solve complex business problems.']
SKILLS = [('LANGUAGES', ['SQL', 'Python', 'R']),
 ('VISUALIZATION & BI', ['Tableau', 'Power BI', 'Excel']),
 ('ANALYTICS & CLOUD', ['RapidMiner', 'AWS']),
 ('GENERATIVE AI & CODING ASSISTANTS', ['ChatGPT', 'Claude', 'Gemini', 'OpenAI Codex'])]
EXPERIENCE = [{'date': 'NOV 2024 - FEB 2026',
  'role': 'Assistant Manager, VIP Marketing',
  'company': 'Hyundai Department Store · Seoul',
  'bullets': ['Analyzed VIP customer trends using Excel and internal analytics platforms to inform '
              'forecasts, tier thresholds, and resource allocation, contributing to 23% VIP revenue '
              'growth',
              'Redesigned VIP loyalty rewards, reducing inefficient program spend by 37%',
              'Developed targeted international VIP programs based on customer spend and visit trends, '
              'contributing to a 39% increase in international sales',
              'Partnered with IT and CRM teams to validate eligibility lists, resolve classification '
              'errors, and support the Jasmine Signature VIP tier launch']},
 {'date': 'SEP 2023 - NOV 2024',
  'role': 'Assistant Manager, Branch Marketing Strategy',
  'company': 'Hyundai Department Store · Seoul',
  'bullets': ['Analyzed customer segments by trade area, spending, and visit frequency using Excel and '
              'internal analytics platforms to guide targeted campaigns',
              'Built monthly revenue and acquisition forecasts to set benchmarks and align marketing '
              'spend',
              'Evaluated floorplan and tenant changes using pre/post analysis to quantify revenue '
              'impact and inform operational decisions']},
 {'date': 'JUL 2022 - DEC 2022',
  'role': 'Marketing Intern, Brand Activations',
  'company': 'Vistaprint · Waltham, MA',
  'bullets': ['Consolidated cross-channel KPIs across NA, UK, and France to guide media allocation',
              'Built UTM tracking across 20+ influencer partners to measure true partner ROI']}]
PROJECTS = [{'meta': 'INDEPENDENT PROJECT · LIVE APPLICATION · 2026',
  'title': 'VIP Loyalty Copilot',
  'desc': 'Built and deployed an interactive decision-support dashboard using 10,000 synthetic customer '
          'records to explore VIP tier projections, membership transitions, and at-risk customers. '
          'Includes customer-level lookup and interactive filtering; forecasts are scenario estimates, '
          'not observed outcomes.',
  'tags': ['Python', 'Streamlit', 'pandas', 'Plotly', 'Customer Analytics'],
  'url': 'https://github.com/yerimmo/vip-loyalty-copilot',
  'live': 'https://yerimmo-vip-loyalty-copilot.streamlit.app',
  'planned': False},
 {'meta': 'EMORY HEALTHCARE · FALL 2026',
  'title': 'Accounts Payable and Working Capital Optimization',
  'desc': 'Built Python pipelines to clean and validate 2.4M+ ERP invoice records, standardized '
          'inconsistent payment codes, and reconciled vendor and transaction data to surface routing '
          'errors. Focus: reliable reporting and operational improvement.',
  'tags': ['Python', 'Data Cleaning', 'ERP Data'],
  'url': None,
  'planned': False},
 {'meta': 'ISOM 675 · DATA VISUALIZATION · FALL 2026',
  'title': 'Does Trust in Automation Change How People Drive?',
  'desc': 'Used a public driving-simulator study (33 drivers, 794 obstacle encounters) to test whether '
          'beliefs about automation show up in real driving. Trust made take-over feel easier and '
          'positive views of automation predicted faster manual driving, but trust did not predict lane '
          "errors once outliers were checked. Replicated the source paper's correlations before "
          'building a 5-chart Altair poster.',
  'tags': ['Python', 'Altair', 'pandas', 'EDA'],
  'url': 'https://github.com/yerimmo/trust-in-automation-driving',
  'planned': False},
 {'meta': 'ISOM 672 · TEAM PROJECT · FALL 2026',
  'title': 'Who Should We Call First?',
  'desc': 'Built a call-list ranking model on 41,176 bank marketing records for a campaign with limited '
          'call capacity. Logistic Regression found 550 subscribers in the top 10% of the test set, a '
          '2.17x lift over random calling, outperforming k‑NN and Decision Tree. I led business '
          'understanding, EDA, and data preparation, including removing call-duration leakage and '
          'recoding pdays.',
  'tags': ['Python', 'Logistic Regression', 'k-NN', 'Decision Tree', 'Data Preparation'],
  'url': 'https://github.com/yerimmo/bank-marketing-call-prioritization',
  'planned': False},
 {'meta': 'IN DEVELOPMENT · INDEPENDENT PROJECT',
  'title': 'AI-Assisted Marketing Operations Workflow',
  'desc': 'Planned: use synthetic campaign data, Python KPI validation, and generative AI to draft '
          'human-reviewed stakeholder summaries. This is not a completed project.',
  'tags': ['Python', 'Workflow Design', 'Generative AI'],
  'url': None,
  'planned': True}]


def safe(s):
    return escape(str(s), quote=True)

def html(content):
    st.markdown(content, unsafe_allow_html=True)

def tag_html(tags):
    return '<div class="tags">' + ''.join(f'<span class="tag">{safe(t)}</span>' for t in tags) + '</div>'

def project_html(p, featured=False):
    cls = 'featured' if featured else 'project'
    if p.get('planned'):
        cls += ' planned'
    actions = []
    if p.get('live'):
        actions.append(f'<a href="{safe(p["live"])}" target="_blank" rel="noopener noreferrer">Explore Live Dashboard ↗</a>')
    if p.get('url'):
        label = 'View GitHub Code ↗' if p.get('live') else 'View Project ↗'
        actions.append(f'<a href="{safe(p["url"])}" target="_blank" rel="noopener noreferrer">{label}</a>')
    return f'''<article class="{cls}">
      <div class="project-meta">{safe(p['meta'])}</div>
      <div class="project-title">{safe(p['title'])}</div>
      <div class="project-desc">{safe(p['desc'])}</div>
      {tag_html(p['tags'])}
      <div class="project-actions">{' '.join(actions)}</div>
    </article>'''

html('''<nav class="nav">
    <span class="brand">YM<span style="color:#F8FAFC">.</span></span>
    <div class="nav-links">
      <a href="#about">About</a><a href="#experience">Experience</a>
      <a href="#projects">Projects</a><a href="#contact">Contact</a>
    </div>
</nav>''')

html('''<section class="hero">
  <div class="eyebrow">Strategy · Analytics · AI · Emory MSBA 2027</div>
  <h1 class="hero-title">Hi, I'm Yerim Mo<span>.</span></h1>
  <div class="hero-lede">I connect business strategy, analytical problem-solving, and technology to turn complex data into practical decisions.</div>
  <div class="pill-row">
    <a class="cta primary" href="#projects">Explore my work ↗</a>
    <a class="cta secondary" href="#contact">Let's connect</a>
  </div>
</section>''')

kpis = [("+23%", "VIP Revenue", "VIP analysis and tier optimization"),
        ("−37%", "Program Spend", "Redesigned VIP loyalty rewards"),
        ("+39%", "International Sales", "Targeted overseas VIP programs"),
        ("2.4M+", "Invoice Records", "Python ERP data pipelines")]
html('<div class="stat-grid">' + ''.join(
    f'<div class="stat"><div class="value">{safe(value)}</div><div class="name">{safe(label)}</div><div class="note">{safe(note)}</div></div>'
    for value, label, note in kpis) + '</div>')

about_copy = ''.join(f'<p>{safe(paragraph)}</p>' for paragraph in ABOUT)
skills_html = ''.join(f'<div class="skill-group"><div class="skill-label">{safe(category)}</div>{tag_html(tags)}</div>' for category,tags in SKILLS)
html(f'''<section class="section" id="about">
  <div class="eyebrow">01 / About</div><h2 class="section-title">A business mindset. An analytical toolkit.</h2>
  <div class="about-grid"><div class="about-copy">{about_copy}</div><div>{skills_html}</div></div>
</section>''')

jobs = []
for job in EXPERIENCE:
    bullets = ''.join(f'<li>{safe(b)}</li>' for b in job['bullets'])
    jobs.append(f'''<div class="job"><div class="job-date">{safe(job['date'])}</div>
      <div class="job-title">{safe(job['role'])}</div><div class="job-company">{safe(job['company'])}</div>
      <ul>{bullets}</ul></div>''')
html('<section class="section" id="experience"><div class="eyebrow">02 / Experience</div><h2 class="section-title">Where strategy meets execution.</h2><div class="timeline">' + ''.join(jobs) + '</div></section>')

html('''<section class="section" id="projects"><div class="eyebrow">03 / Selected Analytics Projects</div>
<h2 class="section-title">Built to answer real business questions.</h2>
<p class="section-desc">From customer analytics to operational improvement, explore the problems, tools, and decisions behind my work.</p></section>''')

filter_options = ["All", "Python", "SQL", "Streamlit", "Machine Learning", "Visualization"]
selected = st.segmented_control("Explore by focus", filter_options, default="All", key="project_focus")

def matches(project):
    if selected == "All":
        return True
    content = " ".join([project["title"], project["desc"], *project["tags"]]).lower()
    if selected == "Machine Learning":
        return any(term in content for term in ("logistic regression", "decision tree", "k-nn"))
    if selected == "Visualization":
        return any(term in content for term in ("altair", "plotly", "visualization", "poster"))
    return selected.lower() in content

visible = [p for p in PROJECTS if matches(p)]
featured = next((p for p in visible if p['title'] == 'VIP Loyalty Copilot'), None)
others = [p for p in visible if p is not featured]
if featured:
    html(project_html(featured, featured=True))
if others:
    html('<div class="project-grid">' + ''.join(project_html(p) for p in others) + '</div>')
if not visible:
    st.info('No projects match this filter yet.')

html('''<section class="section" id="contact">
<div class="eyebrow">04 / Contact</div>
<div class="contact-panel"><h2 class="section-title">Let's build something meaningful.</h2>
<p>Interested in strategy and operations, business analytics, and responsible AI-assisted workflows. I enjoy translating analysis into clear recommendations and action.</p>
<div class="pill-row">
  <a class="cta primary" href="mailto:yerimmo.atl@gmail.com">Email me ↗</a>
  <a class="cta secondary" href="https://www.linkedin.com/in/yerimmo/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a>
  <a class="cta secondary" href="https://github.com/yerimmo" target="_blank" rel="noopener noreferrer">GitHub ↗</a>
</div></div></section>
<div class="site-footer">© 2026 Yerim Mo · Built with Python + Streamlit</div>''')
