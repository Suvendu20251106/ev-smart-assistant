
import streamlit as st

# Title
st.title("🔋 EV Smart Assistant – Charge or Swap")

# Sidebar for inputs
st.sidebar.header("Enter Vehicle & Trip Info")

battery_percentage = st.sidebar.slider("Battery %", 0, 100, 40)
battery_capacity_kwh = st.sidebar.number_input("Battery Capacity (kWh)", 10, 100, 50)
efficiency = st.sidebar.number_input("Vehicle Efficiency (km/kWh)", 1.0, 10.0, 6.0)
distance_to_travel = st.sidebar.number_input("Trip Distance (km)", 1, 1000, 356)
user_prefers_time = st.sidebar.selectbox("Prefer to save time?", ["Yes", "No"]) == "Yes"

# Calculate
current_energy_kwh = (battery_percentage / 100) * battery_capacity_kwh
max_possible_km = current_energy_kwh * efficiency

st.markdown(f"### Battery Status: **{battery_percentage}%**")
st.markdown(f"### Trip Distance: **{distance_to_travel} km**")
st.markdown("---")

if max_possible_km >= distance_to_travel:
    st.success("✅ You can continue your journey without charging.")
else:
    st.warning("⚠️ Battery insufficient for full trip.")

    recommendation = "Swap" if user_prefers_time else "Charge"
    station = "Greenpoint EV Hub"
    distance = "5 km"
    eta_swap = "10 min"
    eta_charge = "45 min"

    st.markdown(f"### Recommendation: **{recommendation} battery** at **{station}**")

    st.markdown("#### 📍 Nearest Station:")
    st.markdown(f"- **Name:** {station}\n- **Distance:** {distance}")

    if recommendation == "Swap":
        st.button(f"🚗 Swap Battery (ETA {eta_swap})")
    else:
        st.button(f"⚡ Charge Battery (ETA {eta_charge})")

    st.info(f"Charge ETA: {eta_charge} | Swap ETA: {eta_swap}")
