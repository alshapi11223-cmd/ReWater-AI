import streamlit as st
# Language and navigation settings
if "language" not in st.session_state:
    st.session_state.language = "English"

if "page" not in st.session_state:
    st.session_state.page = "home"

translations = {
    "English": {
        "welcome": "Welcome to ReWater AI",
        "subtitle": "Your intelligent campus water workspace starts here.",
        "demo": "Enter Demo Workspace →",
        "signin": "Sign In",
        "back": "← Back to Home",
        "email": "Email Address",
        "password": "Password",
        "login": "Continue",
        "demo_note": "Explore the platform without creating an account.",
    },
    "العربية": {
        "welcome": "مرحبًا بك في ReWater AI",
        "subtitle": "مساحة عمل ذكية لإدارة المياه داخل الحرم الجامعي.",
        "demo": "الدخول إلى النسخة التجريبية ←",
        "signin": "تسجيل الدخول",
        "back": "العودة للرئيسية →",
        "email": "البريد الإلكتروني",
        "password": "كلمة المرور",
        "login": "متابعة",
        "demo_note": "استكشف المنصة دون الحاجة إلى إنشاء حساب.",
    }
}

t = translations[st.session_state.language]

st.set_page_config(
    page_title="ReWater AI | Smart Water Intelligence",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Design system
st.markdown("""
<style>
    .stApp {
        background:
            radial-gradient(ellipse at 75% 15%, #30205b 0%, transparent 42%),
            radial-gradient(ellipse at 15% 80%, #10364c 0%, transparent 38%),
            #090d1a;
        color: #f8fafc;
    }

    header[data-testid="stHeader"] {
        background: transparent;
    }

    .block-container {
        max-width: 1250px;
        padding-top: 2rem;
    }

    .brand {
        color: #c4b5fd;
        font-size: 24px;
        font-weight: 800;
        letter-spacing: 1px;
        margin-bottom: 85px;
    }

    .badge {
        display: inline-block;
        background: rgba(139, 92, 246, 0.13);
        border: 1px solid rgba(167, 139, 250, 0.35);
        border-radius: 30px;
        padding: 9px 18px;
        color: #c4b5fd;
        font-size: 13px;
        letter-spacing: 1px;
    }

    .hero {
        text-align: center;
        padding: 35px 10px 65px;
    }

    .hero h1 {
        font-size: clamp(42px, 6vw, 76px);
        font-weight: 850;
        line-height: 1.15;
        letter-spacing: -2px;
        color: #ffffff;
        margin-top: 25px;
    }

    .gradient-text {
        background: linear-gradient(90deg, #c4b5fd, #67e8f9);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        color: #a8b3c9;
        font-size: 18px;
        max-width: 670px;
        margin: 24px auto;
        line-height: 1.8;
    }

    .feature-card {
        background: rgba(21, 27, 46, 0.75);
        border: 1px solid rgba(167, 139, 250, 0.17);
        border-radius: 22px;
        padding: 30px;
        min-height: 210px;
        transition: 0.3s;
    }

    .feature-card:hover {
        border-color: #a78bfa;
        transform: translateY(-5px);
    }

    .feature-card h3 {
        color: #f8fafc;
        font-size: 21px;
        margin-top: 15px;
    }

    .feature-card p {
        color: #94a3b8;
        font-size: 14px;
        line-height: 1.7;
    }

    div.stButton > button {
        background: linear-gradient(90deg, #7c3aed, #4f46e5);
        color: white;
        border: none;
        border-radius: 13px;
        padding: 13px 35px;
        font-weight: 700;
        width: 100%;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #8b5cf6, #6366f1);
        color: white;
        border: none;
    }

    .footer {
        text-align: center;
        color: #64748b;
        font-size: 12px;
        padding: 55px 0 15px;
    }
</style>
""", unsafe_allow_html=True)
# Language selector
language = st.selectbox(
    "🌐 Language / اللغة",
    ["English", "العربية"],
    index=0 if st.session_state.language == "English" else 1
)

if language != st.session_state.language:
    st.session_state.language = language
    st.rerun()
ar = st.session_state.language == "العربية"

def tr(english, arabic):
    return arabic if ar else english
# Brand
st.markdown(
    '<div class="brand">💧 ReWater <span style="color:#67e8f9">AI</span></div>',
    unsafe_allow_html=True
)

# Hero
badge = tr(
    "✦ THE NEXT GENERATION OF WATER INTELLIGENCE",
    "✦ الجيل القادم من ذكاء إدارة المياه"
)

title1 = tr("The Future of", "مستقبل")
title2 = tr("Water Intelligence.", "ذكاء المياه.")

description = tr(
    "Transforming treated water data into smarter decisions. "
    "Explore intelligent water management, sustainable allocation, "
    "and scenario-driven insights for modern campuses.",
    "نحوّل بيانات المياه المعالجة إلى قرارات أكثر ذكاءً. "
    "اكتشف إدارة المياه الذكية والتوزيع المستدام "
    "وتحليل السيناريوهات لدعم المدن الجامعية الحديثة."
)

hero_html = f"""
<div class="hero">
    <div class="badge">{badge}</div>
    <h1>{title1}<br><span class="gradient-text">{title2}</span></h1>
    <p>{description}</p>
</div>
"""

st.markdown(hero_html, unsafe_allow_html=True)

# Buttons
left, middle, right = st.columns([1.3, 1, 1.3])

with middle:
 if st.button("Launch Platform ➜"):
    st.switch_page("pages/login.py")

st.write("")
st.write("")
st.write("")

# Feature cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:32px;">🔬</div>
        <h3>Water Intelligence</h3>
        <p>Analyze water quality indicators and support informed reuse decisions.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:32px;">🌿</div>
        <h3>Smart Allocation</h3>
        <p>Explore optimized water distribution across campus green spaces.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <div style="font-size:32px;">📊</div>
        <h3>Scenario Intelligence</h3>
        <p>Simulate changing conditions and evaluate potential outcomes.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown(
    '<div class="footer">ReWater AI © 2026 | Smart Campus Water Intelligence</div>',
    unsafe_allow_html=True
)