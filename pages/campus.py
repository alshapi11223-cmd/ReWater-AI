import streamlit as st

st.set_page_config(
    page_title="ReWater AI | Campus Setup",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Session settings
if "language" not in st.session_state:
    st.session_state.language = "English"

if "campus_ready" not in st.session_state:
    st.session_state.campus_ready = False

translations = {
    "English": {
        "title": "Let's Set Up Your Smart Campus",
        "subtitle": "Personalize your water intelligence workspace.",
        "university": "University",
        "campus": "Campus Name",
        "source": "Water Source",
        "goal": "Management Goal",
        "create": "Create Workspace →",
        "success": "Your campus workspace is ready!",
        "next": "Dashboard integration is coming next.",
        "note": "Demo configuration only. No university affiliation is implied."
    },
    "العربية": {
        "title": "لنجهّز حرمك الجامعي الذكي",
        "subtitle": "خصّص مساحة العمل لإدارة المياه.",
        "university": "الجامعة",
        "campus": "اسم الحرم الجامعي",
        "source": "مصدر المياه",
        "goal": "هدف الإدارة",
        "create": "إنشاء مساحة العمل ←",
        "success": "مساحة العمل الجامعية جاهزة!",
        "next": "الخطوة القادمة ربط لوحة التحكم.",
        "note": "إعدادات تجريبية، ولا تعني ارتباط المنصة بأي جامعة."
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

.setup-heading {
    text-align: center;
    margin: 35px 0 40px;
}

.setup-heading h1 {
    color: #f8fafc;
    font-size: 43px;
}

.setup-heading p {
    color: #a8b3c9;
    font-size: 17px;
}

.setup-card {
    background: rgba(21, 27, 46, 0.82);
    border: 1px solid rgba(167, 139, 250, 0.3);
    border-radius: 24px;
    padding: 25px;
    margin-bottom: 20px;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
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
    '<h3 style="color:#c4b5fd;">💧 ReWater <span style="color:#67e8f9;">AI</span></h3>',
    unsafe_allow_html=True
)

st.markdown(f"""
<div class="setup-heading">
    <h1>{t["title"]}</h1>
    <p>{t["subtitle"]}</p>
</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 2.5, 1])

with center:
    with st.container(border=True):

        universities = [
            "Umm Al-Qura University",
            "King Abdulaziz University",
            "King Saud University",
            "Other University"
        ]

        university = st.selectbox(
            "🏛️ " + t["university"],
            universities
        )

        campus_name = st.text_input(
            "📍 " + t["campus"],
            value="Main Campus"
        )

        sources = [
            "Treated Wastewater",
            "Greywater",
            "AC Condensate"
        ]

        water_source = st.selectbox(
            "💧 " + t["source"],
            sources
        )

        goals = [
            "Optimize Irrigation",
            "Reduce Water Waste",
            "Analyze Water Quality",
            "Explore Scenarios"
        ]

        goal = st.selectbox(
            "🎯 " + t["goal"],
            goals
        )

        st.write("")

        if st.button(t["create"]):
            if campus_name.strip():
                st.session_state.university = university
                st.session_state.campus_name = campus_name.strip()
                st.session_state.water_source = water_source
                st.session_state.goal = goal
                st.session_state.campus_ready = True
                st.switch_page("pages/dashboard.py")
            else:
                st.warning("Please enter a campus name.")

        if st.session_state.campus_ready:
            st.success(t["success"])

            st.info(t["next"])

            st.write("**University:**", st.session_state.university)
            st.write("**Campus:**", st.session_state.campus_name)
            st.write("**Water Source:**", st.session_state.water_source)
            st.write("**Goal:**", st.session_state.goal)

st.caption(t["note"])
# Campus Setup — readability improvements
st.markdown("""
<style>

/* All form labels */
.stApp label,
.stApp [data-testid="stWidgetLabel"] p {
    color: #F1F5F9 !important;
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Input and dropdown text */
.stApp [data-testid="stSelectbox"] div[data-baseweb="select"],
.stApp [data-testid="stTextInput"] input {
    font-size: 17px !important;
}

/* Input text */
.stApp [data-testid="stTextInput"] input {
    color: #FFFFFF !important;
}

/* Page subtitle */
.setup-heading p {
    color: #E2E8F0 !important;
    font-size: 19px !important;
}

/* Form helper text */
.stApp [data-testid="stCaptionContainer"] {
    color: #CBD5E1 !important;
    font-size: 14px !important;
}

/* Dropdown arrows and field borders */
.stApp [data-testid="stSelectbox"] div[data-baseweb="select"] {
    border-radius: 12px;
}

</style>
""", unsafe_allow_html=True)