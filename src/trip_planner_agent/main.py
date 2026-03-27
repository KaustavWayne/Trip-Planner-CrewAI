import streamlit as st
from datetime import datetime

from trip_planner_agent.crew import run_crew
from trip_planner_agent.tools.currency_tool import convert_currency

st.set_page_config(page_title="VoyageAI", page_icon="✈️", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
.card {
    background: white;
    padding: 18px;
    border-radius: 12px;
    margin-bottom: 15px;
    border: 1px solid #eee;
    box-shadow: 0px 2px 6px rgba(0,0,0,0.05);
}
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.title("✈️ VoyageAI")
st.markdown("**Intelligent Trip Planner powered by CrewAI + Groq**")

# ---------- SESSION ----------
if "trip_plan" not in st.session_state:
    st.session_state.trip_plan = None

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("Plan Your Trip")

    destination = st.text_input("Destination", "Tokyo")
    days = st.slider("Days", 1, 15, 5)
    travelers = st.number_input("Travelers", 1, 10, 2)
    budget_level = st.selectbox("Budget Level", ["budget", "moderate", "luxury"], index=1)
    travel_date = st.date_input("Travel Date", datetime.now().date())

    generate = st.button("🚀 Generate Trip Plan", use_container_width=True)

# ---------- GENERATE ----------
if generate:
    with st.spinner(f"Planning your trip to {destination}..."):
        try:
            result = run_crew({
                "user_query": f"{days}-day {budget_level} trip to {destination} for {travelers} people in {travel_date.strftime('%B %Y')}",
                "destination": destination,
                "days": days,
                "budget": budget_level,
                "travelers": travelers
            })

            st.session_state.trip_plan = result.raw

        except Exception as e:
            st.error(f"Error: {e}")

# ---------- DISPLAY ----------
if st.session_state.trip_plan:

    st.success(f"✅ Trip Ready for {destination}")

    plan = st.session_state.trip_plan.replace("**", "")

    # ---------- WEATHER ----------
    if "## 🌤️ Weather" in plan:
        try:
            weather = plan.split("## 🌤️ Weather")[1].split("##")[0]
            st.markdown("<div class='section-title'>🌤 Weather</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'>{weather}</div>", unsafe_allow_html=True)
        except:
            pass

    # ---------- BUDGET ----------
    if "## 💰 Budget" in plan:
        try:
            budget = plan.split("## 💰 Budget")[1].split("##")[0]
            st.markdown("<div class='section-title'>💰 Budget</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'>{budget}</div>", unsafe_allow_html=True)
        except:
            pass

    # ---------- PLACES ----------
    if "## 📍 Places" in plan:
        try:
            places = plan.split("## 📍 Places")[1].split("##")[0]
            st.markdown("<div class='section-title'>📍 Top Places</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'>{places}</div>", unsafe_allow_html=True)
        except:
            pass

    # ---------- HOTELS ----------
    if "## 🏨 Hotels" in plan:
        try:
            hotels = plan.split("## 🏨 Hotels")[1].split("##")[0]
            st.markdown("<div class='section-title'>🏨 Hotels</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='card'>{hotels}</div>", unsafe_allow_html=True)
        except:
            pass

    # ---------- ITINERARY (FIXED ✅) ----------
    if "## 🗓️ Itinerary" in plan:
        try:
            # 🔥 FIX: Stop before Travel Tips
            itinerary = plan.split("## 🗓️ Itinerary")[1].split("## 🚗 Travel Tips")[0]

            st.markdown("<div class='section-title'>🗓️ Day-wise Itinerary</div>", unsafe_allow_html=True)

            days_data = itinerary.split("###")

            for d in days_data:
                if "Day" in d:
                    title = d.split("\n")[0].strip()

                    with st.expander(f"📅 {title}", expanded=True):
                        st.markdown(d)

        except:
            st.markdown("Itinerary not available")

    # ---------- TRAVEL TIPS (FIXED ✅) ----------
    if "## 🚗 Travel Tips" in plan:
        try:
            tips = plan.split("## 🚗 Travel Tips")[1]

            st.markdown("<div class='section-title'>🚗 Travel Tips</div>", unsafe_allow_html=True)

            # 🔥 Proper bullet rendering (NO HTML breaking markdown)
            st.markdown(tips)

        except:
            pass

    # ---------- CURRENCY CONVERTER ----------
    st.markdown("---")
    st.subheader("💱 Currency Converter")

    col1, col2, col3 = st.columns(3)

    amount = col1.number_input("Amount", value=50000.0)
    from_curr = col2.selectbox("From", ["INR", "USD", "JPY", "EUR"])
    to_curr = col3.selectbox("To", ["INR", "USD", "JPY", "EUR"])

    if st.button("Convert"):
        try:
            result = convert_currency(amount, from_curr, to_curr)
            st.success(f"{amount:,.2f} {from_curr} = {result:,.2f} {to_curr}")
        except Exception as e:
            st.error(e)

else:
    st.info("👈 Fill details and generate trip")

# ---------- FOOTER ----------
st.caption("CrewAI • Groq • Tavily • ExchangeRate API")