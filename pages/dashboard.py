import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ReWater AI | Dashboard",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Demo data — not real university measurements
if "university" not in st.session_state:
    st.session_state.university = "Umm Al-Qura University"

if "campus_name" not in st.session_state:
    st.session_state.campus_name = "Main Campus"

if "language" not in st.session_state:
    st.session_state.language = "English"

# Design
st.markdown("""
<style>
.stApp {
    background:
        radial-gradient(ellipse at 85% 10%, #25184a 0%, transparent 38%),
        radial-gradient(ellipse at 10% 90%, #10364c 0%, transparent 35%),
        #090d1a;
    color: #f8fafc;
}

header[data-testid="stHeader"] {
    background: transparent;
}

section[data-testid="stSidebar"] {
    background: #111629;
    border-right: 1px solid #30274f;
}

.block-container {
    padding-top: 2rem;
    max-width: 1450px;
}

.dashboard-title {
    font-size: 42px;
    font-weight: 800;
    color: white;
    margin-bottom: 8px;
}

.dashboard-subtitle {
    color: #a8b3c9;
    font-size: 16px;
    margin-bottom: 30px;
}

.section-title {
    color: #c4b5fd;
    font-size: 23px;
    font-weight: 700;
    margin-top: 28px;
    margin-bottom: 18px;
}

.insight-card {
    background: rgba(21, 27, 46, 0.85);
    border: 1px solid rgba(167, 139, 250, 0.2);
    border-radius: 18px;
    padding: 24px;
    min-height: 150px;
}

.insight-card h3 {
    color: #a8b3c9;
    font-size: 15px;
    margin-bottom: 15px;
}

.insight-card h2 {
    color: #f8fafc;
    font-size: 29px;
    margin-bottom: 10px;
}

.insight-card p {
    color: #67e8f9;
    font-size: 12px;
}

div.stButton > button {
    background: linear-gradient(90deg, #7c3aed, #4f46e5);
    color: white;
    border: none;
    border-radius: 12px;
    width: 100%;
}

div.stButton > button:hover {
    background: #8b5cf6;
    color: white;
}
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("## 💧 ReWater AI")
    st.caption("SAMA SIGNATURE EDITION")
    st.divider()

    page = st.radio(
        "Navigation",
        [
            "🏠 Overview",
            "🔬 Water Quality",
            "🌿 Smart Allocation",
            "📊 Scenario Lab",
            "💰 Cost Insights",
            "📈 Reports"
        ]
    )

    st.divider()
    st.caption("DEMO ENVIRONMENT")
    st.write(st.session_state.university)

# Main dashboard
if page == "🏠 Overview":

    st.markdown(
        '<div class="dashboard-title">Water Intelligence Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="dashboard-subtitle">'
        f'{st.session_state.university} | '
        f'{st.session_state.campus_name}'
        f'</div>',
        unsafe_allow_html=True
    )

    st.info(
        "Educational prototype using simulated data. "
        "No real university water measurements are represented."
    )

    col1, col2, col3, col4 = st.columns(4)

    metrics = [
        ("Available Treated Water", "100 m³", "Daily supply"),
        ("Campus Irrigation Demand", "120 m³", "Daily demand"),
        ("Potential Coverage", "83.3%", "Demand coverage"),
        ("Water Shortage", "20 m³", "Daily deficit")
    ]

    for col, metric in zip(
        [col1, col2, col3, col4],
        metrics
    ):
        with col:
            st.markdown(f"""
            <div class="insight-card">
                <h3>{metric[0]}</h3>
                <h2>{metric[1]}</h2>
                <p>{metric[2]}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<div class="section-title">Water Distribution Overview</div>',
        unsafe_allow_html=True
    )

    data = pd.DataFrame({
        "Campus Zone": [
            "Garden A",
            "Garden B",
            "Garden C"
        ],
        "Water Demand": [40, 50, 30],
        "Allocated Water": [33.33, 41.67, 25]
    })

    st.bar_chart(
        data.set_index("Campus Zone")
    )

    st.markdown(
        '<div class="section-title">Campus Water Insights</div>',
        unsafe_allow_html=True
    )

    left, right = st.columns(2)

    with left:
        st.warning(
            "Irrigation demand exceeds available treated water "
            "by 20 m³/day."
        )

    with right:
        st.info(
            "Current demonstration allocation uses proportional "
            "distribution, not machine learning."
        )

    st.markdown(
        '<div class="section-title">Quick Actions</div>',
        unsafe_allow_html=True
    )

    a, b, c = st.columns(3)

    with a:
        if st.button("Analyze Water Quality"):
            st.session_state.quick_page = "water"

    with b:
        if st.button("Explore Allocation"):
            st.session_state.quick_page = "allocation"

    with c:
        if st.button("Run Simulation"):
            st.session_state.quick_page = "simulation"

    if "quick_page" in st.session_state:
        st.info(
            "Select the corresponding section from the sidebar "
            "to continue."
        )

elif page == "🔬 Water Quality":
    st.title("🔬 Water Quality")
    st.write("### 💧 Water Quality Analysis")
    st.caption("Educational screening only — not an official water safety assessment.")

    col1, col2 = st.columns(2)

    with col1:
        ph = st.number_input(
            "pH Level",
            min_value=0.0,
            max_value=14.0,
            value=7.2,
            step=0.1
        )

    with col2:
        turbidity = st.number_input(
            "Turbidity (NTU)",
            min_value=0.0,
            value=3.0,
            step=0.5
        )

    if st.button("🔬 Analyze Water Quality"):
        ph_ok = 6.5 <= ph <= 8.5
        turbidity_ok = turbidity <= 5.0

        st.write("### Analysis Results")

        if ph_ok:
            st.success(f"pH: {ph} — Within illustrative range")
        else:
            st.warning(f"pH: {ph} — Outside illustrative range")

        if turbidity_ok:
            st.success(f"Turbidity: {turbidity} NTU — Within illustrative range")
        else:
            st.warning(f"Turbidity: {turbidity} NTU — Outside illustrative range")

        if ph_ok and turbidity_ok:
            st.info(
                "Both indicators meet the illustrative screening criteria. "
                "This does NOT confirm that the water is safe for reuse."
            )
        else:
            st.error(
                "One or more indicators require further review. "
                "Reuse suitability cannot be confirmed."
            )

        st.caption(
            "Illustrative thresholds: pH 6.5–8.5 and turbidity ≤ 5 NTU. "
            "These are NOT presented as official Saudi regulatory limits. "
            "Additional laboratory parameters and applicable standards "
            "are required before any real reuse decision."
        )

elif page == "🌿 Smart Allocation":
    st.title("🌿 Smart Allocation")
    st.write("### 🌱 Smart Water Allocation")
    st.caption("Proportional allocation using simulated data.")

    supply = st.number_input(
        "Available treated water (m³/day)",
        min_value=0.0,
        value=100.0
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        garden_a = st.number_input(
            "Garden A demand (m³/day)", min_value=0.0, value=40.0
        )

    with col2:
        garden_b = st.number_input(
            "Garden B demand (m³/day)", min_value=0.0, value=50.0
        )

    with col3:
        garden_c = st.number_input(
            "Garden C demand (m³/day)", min_value=0.0, value=30.0
        )

    if st.button("🌱 Calculate Allocation"):
        demands = {
            "Garden A": garden_a,
            "Garden B": garden_b,
            "Garden C": garden_c
        }

        total_demand = sum(demands.values())
        usable_water = min(supply, total_demand)

        if total_demand == 0:
            st.warning("Enter at least one garden demand.")
        else:
            st.write("### Allocation Results")

            for name, demand in demands.items():
                allocation = usable_water * demand / total_demand
                st.success(f"{name}: {allocation:.2f} m³/day")

            shortage = max(0.0, total_demand - supply)
            excess = max(0.0, supply - total_demand)

            st.metric("Total Demand", f"{total_demand:.2f} m³/day")
            st.metric("Water Shortage", f"{shortage:.2f} m³/day")
            st.metric("Unused Water", f"{excess:.2f} m³/day")

            st.caption(
                "This demonstration uses proportional distribution, "
                "not a trained AI model."
            )

elif page == "📊 Scenario Lab":
    st.title("📊 Scenario Lab")
    st.write("### 📊 Water Supply Scenario Simulator")
    st.caption("Explore simulated irrigation supply and demand scenarios.")

    scenario_supply = st.slider(
        "Available treated water (m³/day)",
        min_value=0,
        max_value=250,
        value=100,
        step=10
    )

    scenario_demand = st.slider(
        "Campus irrigation demand (m³/day)",
        min_value=0,
        max_value=250,
        value=120,
        step=10
    )

    if st.button("▶️ Run Scenario"):
        used_water = min(scenario_supply, scenario_demand)
        shortage = max(0, scenario_demand - scenario_supply)
        surplus = max(0, scenario_supply - scenario_demand)

        coverage = (
            used_water / scenario_demand * 100
            if scenario_demand > 0 else 100
        )

        c1, c2, c3 = st.columns(3)

        c1.metric("Demand Coverage", f"{coverage:.1f}%")
        c2.metric("Water Shortage", f"{shortage} m³/day")
        c3.metric("Unused Water", f"{surplus} m³/day")

        if shortage > 0:
            st.warning(
                f"Supply is insufficient by {shortage} m³/day."
            )
        else:
            st.success(
                "Available supply can cover the simulated demand."
            )

        st.caption(
            "Scenario results are calculated from user inputs. "
            "They do not predict future water availability."
        )

elif page == "💰 Cost Insights":
    st.title("💰 Cost Insights")
    st.write("### 💧 Water Reuse Financial Calculator")

    st.caption(
        "Educational cost estimation using simulated data. "
        "Enter your own assumptions to explore potential savings."
    )

    col1, col2 = st.columns(2)

    with col1:
        daily_water = st.number_input(
            "Reused Water (m³/day)",
            min_value=0.0,
            value=100.0,
            step=10.0
        )

        fresh_water_cost = st.number_input(
            "Alternative Water Cost (SAR/m³)",
            min_value=0.0,
            value=5.0,
            step=0.5
        )

    with col2:
        treatment_cost = st.number_input(
            "Treatment Cost (SAR/m³)",
            min_value=0.0,
            value=2.0,
            step=0.5
        )

        operating_days = st.number_input(
            "Operating Days per Year",
            min_value=1,
            max_value=365,
            value=365
        )

    if st.button("💰 Calculate Savings"):

        annual_water = daily_water * operating_days

        alternative_cost = annual_water * fresh_water_cost

        reuse_cost = annual_water * treatment_cost

        net_savings = alternative_cost - reuse_cost

        st.write("### 📊 Financial Results")

        a, b, c = st.columns(3)

        a.metric(
            "Annual Reused Water",
            f"{annual_water:,.0f} m³"
        )

        b.metric(
            "Annual Reuse Cost",
            f"{reuse_cost:,.0f} SAR"
        )

        c.metric(
            "Estimated Net Savings",
            f"{net_savings:,.0f} SAR"
        )

        if net_savings > 0:
            st.success(
                f"Potential annual savings: {net_savings:,.0f} SAR"
            )

        elif net_savings == 0:
            st.info(
                "Estimated reuse and alternative water costs are equal."
            )

        else:
            st.warning(
                "Under these assumptions, reuse costs more "
                "than the alternative water source."
            )

        st.caption(
            "Results exclude capital investment, maintenance, "
            "distribution infrastructure, and other unentered costs. "
            "Values are illustrative and are not official Saudi tariffs."
        )

elif page == "📈 Reports":
    st.title("📈 Reports")
    st.write("### 📄 Campus Water Intelligence Report")

    st.caption(
        "Generate a downloadable report using simulated "
        "campus water data and your selected assumptions."
    )

    from datetime import datetime
    import pandas as pd

    university = st.session_state.get(
        "university", "Demo University"
    )

    campus_name = st.session_state.get(
        "campus_name", "Main Campus"
    )

    water_source = st.session_state.get(
        "water_source", "Treated Wastewater"
    )

    st.write("### 🏫 Campus Information")
    st.write(f"**University:** {university}")
    st.write(f"**Campus:** {campus_name}")
    st.write(f"**Water Source:** {water_source}")

    st.divider()

    st.write("### 💧 Water Data")

    daily_supply = st.number_input(
        "Daily Available Water (m³)",
        min_value=0.0,
        value=100.0,
        key="report_supply"
    )

    daily_demand = st.number_input(
        "Daily Irrigation Demand (m³)",
        min_value=0.0,
        value=120.0,
        key="report_demand"
    )

    coverage = (
        min(daily_supply / daily_demand * 100, 100)
        if daily_demand > 0 else 0
    )

    shortage = max(daily_demand - daily_supply, 0)
    unused = max(daily_supply - daily_demand, 0)

    a, b, c = st.columns(3)

    a.metric("Demand Coverage", f"{coverage:.1f}%")
    b.metric("Water Shortage", f"{shortage:.1f} m³")
    c.metric("Unused Water", f"{unused:.1f} m³")

    st.divider()

    st.write("### 📥 Export Report")

    report_data = {
        "Metric": [
            "University",
            "Campus",
            "Water Source",
            "Daily Available Water (m³)",
            "Daily Irrigation Demand (m³)",
            "Demand Coverage (%)",
            "Water Shortage (m³)",
            "Unused Water (m³)"
        ],
        "Value": [
            university,
            campus_name,
            water_source,
            daily_supply,
            daily_demand,
            round(coverage, 1),
            round(shortage, 1),
            round(unused, 1)
        ]
    }

    report_df = pd.DataFrame(report_data)

    st.dataframe(
        report_df,
        use_container_width=True,
        hide_index=True
    )

    csv = report_df.to_csv(index=False).encode("utf-8-sig")

    st.download_button(
        label="📥 Download CSV Report",
        data=csv,
        file_name="ReWaterAI_Campus_Report.csv",
        mime="text/csv"
    )

    st.info(
        "This report is generated from simulated or "
        "user-entered values. It does not certify water "
        "quality or regulatory compliance."
    )

    st.caption(
        f"Report generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}"
    )

st.divider()

st.caption(
    "ReWater AI © 2026 | Sama Signature Edition | "
    "Simulated Educational Prototype"
)
# Accessibility and readability improvements
st.markdown("""
<style>

/* Main text */
.stApp,
.stApp p,
.stApp label {
    color: #F1F5F9 !important;
    font-size: 16px;
}

/* Sidebar */
section[data-testid="stSidebar"] * {
    color: #F1F5F9 !important;
}

section[data-testid="stSidebar"] label {
    font-size: 17px !important;
    font-weight: 600 !important;
}

/* Dashboard cards */
.insight-card h3 {
    color: #CBD5E1 !important;
    font-size: 17px !important;
    font-weight: 600;
}

.insight-card h2 {
    color: #FFFFFF !important;
    font-size: 34px !important;
}

.insight-card p {
    color: #A5F3FC !important;
    font-size: 14px !important;
}

/* University name */
.dashboard-subtitle {
    color: #E2E8F0 !important;
    font-size: 18px !important;
}

/* Section headings */
.section-title {
    color: #DDD6FE !important;
    font-size: 26px !important;
}

/* Radio options */
div[role="radiogroup"] label {
    padding: 7px 4px;
}

</style>
""", unsafe_allow_html=True)