import streamlit as st

st.set_page_config(
    page_title="ReWater AI | Welcome",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

if "language" not in st.session_state:
    st.session_state.language = "English"

if "access_page" not in st.session_state:
    st.session_state.access_page = "welcome"

translations = {
    "English": {
        "welcome": "Welcome to ReWater AI",
        "subtitle": "Your intelligent campus water workspace starts here.",
        "demo": "Enter Demo Workspace →",
        "signin": "Sign In",
        "back": "← Back",
        "email": "Email Address",
        "password": "Password",
        "continue": "Continue",
        "note": "Explore the platform without creating an account.",
        "demo_ready": "Demo access selected! Campus setup is our next step.",
        "login_note": "Demo interface only. Do not enter real credentials."
    },
    "العربية": {
        "welcome": "مرحبًا بك في ReWater AI",
        "subtitle": "مساحة عمل ذكية لإدارة المياه داخل الحرم الجامعي.",
        "demo": "الدخول إلى النسخة التجريبية ←",
        "signin": "تسجيل الدخول",
        "back": "العودة",
        "email": "البريد الإلكتروني",
        "password": "كلمة المرور",
        "continue": "متابعة",
        "note": "استكشف المنصة دون الحاجة إلى إنشاء حساب.",
        "demo_ready": "تم اختيار الدخول التجريبي! الخطوة القادمة إعداد الجامعة.",
        "login_note": "واجهة تجريبية فقط. لا تُدخل بيانات دخول حقيقية."
    }
}

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
    max-width: 1100px;
    padding-top: 2rem;
}

.access-card {
    background: rgba(21, 27, 46, 0.82);
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 26px;
    padding: 45px 35px;
    text-align: center;
    margin-top: 45px;
    margin-bottom: 25px;
}

.access-card h1 {
    color: #f8fafc;
    font-size: 43px;
    margin-bottom: 18px;
}

.access-card p {
    color: #a8b3c9;
    font-size: 17px;
}

.brand {
    color: #c4b5fd;
    font-size: 24px;
    font-weight: 800;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 13px;
    padding: 12px 20px;
    font-weight: 700;
    width: 100%;
}

div.stButton > button:hover {
    background: #8b5cf6;
    color: white;
}

[data-testid="stTextInput"] input {
    background-color: #151b2e;
    color: white;
}
</style>
""", unsafe_allow_html=True)

language = st.selectbox(
    "🌐 Language / اللغة",
    ["English", "العربية"],
    index=0 if st.session_state.language == "English" else 1
)

if language != st.session_state.language:
    st.session_state.language = language
    st.rerun()

t = translations[st.session_state.language]

st.markdown(
    '<div class="brand">💧 ReWater <span style="color:#67e8f9">AI</span></div>',
    unsafe_allow_html=True
)

left, center, right = st.columns([1, 2, 1])

with center:
    st.markdown(f"""
    <div class="access-card">
        <div style="font-size:42px;">💧</div>
        <h1>{t["welcome"]}</h1>
        <p>{t["subtitle"]}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.session_state.access_page == "welcome":

        if st.button(t["demo"], key="demo"):
         st.switch_page("pages/campus.py")
        if st.button(t["signin"], key="signin"):
            st.session_state.access_page = "signin"
            st.rerun()

        st.caption(t["note"])

    elif st.session_state.access_page == "demo":

        st.success(t["demo_ready"])

        if st.button(t["back"], key="back_demo"):
            st.session_state.access_page = "welcome"
            st.rerun()

    elif st.session_state.access_page == "signin":

        st.info(t["login_note"])

        st.text_input(t["email"], disabled=True)
        st.text_input(t["password"], type="password", disabled=True)

        st.button(t["continue"], disabled=True)

        if st.button(t["back"], key="back_signin"):
            st.session_state.access_page = "welcome"
            st.rerun()

st.markdown(
    '<p style="text-align:center;color:#64748b;margin-top:65px;">'
    'ReWater AI © 2026 | Sama Signature Edition'
    '</p>',
    unsafe_allow_html=True
)
# Login page readability improvements
st.markdown("""
<style>
/* Input labels */
.stApp [data-testid="stWidgetLabel"] p {
    color: #FFFFFF !important;
    font-size: 17px !important;
    font-weight: 600 !important;
}

/* Disabled input text */
.stApp input:disabled {
    color: #E2E8F0 !important;
    -webkit-text-fill-color: #E2E8F0 !important;
    opacity: 1 !important;
}

/* Disabled buttons */
.stApp button:disabled {
    color: #FFFFFF !important;
    opacity: 0.65 !important;
}

/* Input backgrounds */
.stApp input {
    background-color: #1E254B !important;
}
</style>
""", unsafe_allow_html=True)