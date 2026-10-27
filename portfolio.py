import streamlit as st

st.set_page_config(page_title="Yerim Mo | Strategy, Analytics & AI", page_icon="💠", layout="wide", initial_sidebar_state="collapsed")

NAVY = "#0B1120"
CARD = "#111827"
BORDER = "#1F2937"
TEXT = "#E2E8F0"
MUTED = "#94A3B8"
TEAL = "#5EEAD4"

st.markdown("""
<style>
:root {color-scheme: dark;}
.stApp, [data-testid="stAppViewContainer"] {background: #0B1120; color: #E2E8F0;}
[data-testid="stHeader"] {background: rgba(11,17,32,.85);}
.block-container {max-width: 1050px; padding-top: 3rem; padding-bottom: 5rem;}
h1, h2, h3, p, li {color: #E2E8F0;}
h1 {font-size: 3.35rem !important; font-weight: 800 !important; letter-spacing: -0.04em;}
h2 {font-size: 1.65rem !important; font-weight: 700 !important;}
h3 {font-size: 1.08rem !important;}
[data-testid="stMetric"] {background:#111827; border:1px solid #1F2937; border-radius:12px; padding:20px;}
[data-testid="stMetricValue"] {color:#5EEAD4; font-weight:800;}
[data-testid="stMetricLabel"] {color:#E2E8F0;}
[data-testid="stVerticalBlockBorderWrapper"] > div {border-color:#1F2937 !important; background:#111827 !important;}
.stButton > button, .stLinkButton > a {border-radius:8px; font-weight:600;}
.stLinkButton > a:hover {border-color:#5EEAD4; color:#5EEAD4;}
[data-testid="stMultiSelect"] {color:#E2E8F0;}
section[data-testid="stSidebar"] {background:#111827;}
hr {border-color:#1F2937;}
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

with st.sidebar:
    st.title("Yerim Mo")
    st.caption("STRATEGY · ANALYTICS · AI")
    st.link_button("VIP Loyalty Copilot", "https://yerimmo-vip-loyalty-copilot.streamlit.app")
    st.link_button("GitHub Profile", "https://github.com/yerimmo")

st.caption(":green[STRATEGY · ANALYTICS · AI · EMORY MSBA 2027]")
st.title("Hi, I'm Yerim Mo 👋")
st.markdown("#### I connect business strategy, analytical problem-solving, and technology to turn complex data into practical decisions.")
st.write("")

kpis = [("VIP Revenue", "+23%", "VIP analysis and tier optimization"),
        ("Program Spend", "−37%", "Redesigned VIP loyalty rewards"),
        ("International Sales", "+39%", "Targeted overseas VIP programs"),
        ("Invoice Records", "2.4M+", "Python ERP data pipelines")]
for col, (label, value, note) in zip(st.columns(4), kpis):
    with col:
        st.metric(label, value)
        st.caption(note)

st.divider()
st.caption(":green[ABOUT]")
left, right = st.columns([2, 1], gap="large")
with left:
    for paragraph in ABOUT:
        st.write(paragraph)
with right:
    for category, tags in SKILLS:
        st.markdown(f"**{category}**")
        st.caption(" · ".join(tags))

st.divider()
st.caption(":green[EXPERIENCE]")
for job in EXPERIENCE:
    with st.container(border=True):
        st.caption(job["date"])
        st.markdown(f'### {job["role"]}')
        st.markdown(f':green[{job["company"]}]')
        for bullet in job["bullets"]:
            st.markdown(f'- {bullet}')

st.divider()
st.caption(":green[SELECTED ANALYTICS PROJECTS]")
st.write("Business questions, analytical approaches, and decisions supported by data. Public repositories are linked where available.")
filter_options = ["All", "Python", "SQL", "Streamlit", "Machine Learning", "Visualization"]
selected = st.segmented_control("Explore by focus", filter_options, default="All")

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
if not visible:
    st.info("No projects match this filter yet.")
for idx in range(0, len(visible), 2):
    for col, p in zip(st.columns(2, gap="medium"), visible[idx:idx+2]):
        with col:
            with st.container(border=True):
                st.caption(p["meta"])
                st.markdown(f'### {p["title"]}')
                st.write(p["desc"])
                st.caption(" · ".join(p["tags"]))
                if p.get("live"):
                    st.link_button("Explore Live Dashboard ↗", p["live"], use_container_width=True)
                if p.get("url"):
                    st.link_button("View GitHub Code ↗" if p.get("live") else "View Project ↗", p["url"], use_container_width=True)

st.divider()
st.caption(":green[CONTACT]")
st.header("Let's connect")
st.write("Interested in strategy and operations, business analytics, and responsible AI-assisted workflows. I enjoy translating analysis into clear recommendations and action.")
col1, col2, col3 = st.columns(3)
with col1:
    st.link_button("Email me", "mailto:yerimmo.atl@gmail.com", use_container_width=True)
with col2:
    st.link_button("LinkedIn", "https://www.linkedin.com/in/yerimmo/", use_container_width=True)
with col3:
    st.link_button("GitHub", "https://github.com/yerimmo", use_container_width=True)
st.caption("© 2026 Yerim Mo · Built with Python + Streamlit")
