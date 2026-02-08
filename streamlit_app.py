import streamlit as st
import pandas as pd

st.set_page_config(page_title="Warframe Damage Lab", layout="wide")

st.title("🏹 The Warframe Damage Lab")
st.write("""
Welcome, Tenno! Ever wondered why your weapon feels like a wet noodle despite having three damage mods? 
It's all about **The Buckets**. 
""")

# --- PART 1: THE RECTANGLE (2 Multipliers) ---
st.header("1. The 2D Rectangle (Base vs Elemental)")
st.info("Analogy: If you have 20m of fencing, a 10x10 square (100m²) beats a 19x1 rectangle (19m²).")

col1, col2 = st.columns([1, 2])

with col1:
    base_dmg_mod = st.slider("Base Damage % (e.g., Serration)", 0, 330, 165)
    elem_dmg_mod = st.slider("Elemental % (e.g., Infected Clip)", 0, 330, 90)

# The Math: (1 + Mod1) * (1 + Mod2)
total_mult_2d = (1 + base_dmg_mod/100) * (1 + elem_dmg_mod/100)

with col2:
    st.metric("Total Damage Multiplier", f"{total_mult_2d:.2f}x")
    st.write(f"**Formula:** `(1 + {base_dmg_mod/100}) × (1 + {elem_dmg_mod/100})`")
    # Small visual representation
    st.write(f"Imagine a rectangle that is {1 + base_dmg_mod/100:.2f} units long and {1 + elem_dmg_mod/100:.2f} units wide.")

# --- PART 2: THE CUBE (3 Multipliers) ---
st.header("2. The 3D Cube (Adding Multishot)")
st.write("Now we add **Multishot**. This isn't just a bigger rectangle; it's a 3D box.")

col3, col4 = st.columns([1, 2])

with col3:
    ms_mod = st.slider("Multishot % (e.g., Split Chamber)", 0, 240, 90)

total_mult_3d = total_mult_2d * (1 + ms_mod/100)

with col4:
    st.metric("New Total Multiplier", f"{total_mult_3d:.2f}x")
    st.write(f"**The 'N' Growth:** Adding a third dimension (depth) makes the volume explode.")

# --- PART 3: THE N-DIMENSIONAL TESSERACT ---
st.header("3. The 'N' Multipliers (The Full Build)")
st.write("Real Warframe builds use 5 or 6 buckets. Stacking one to the moon is almost always worse than spreading them out.")

c1, c2, c3 = st.columns(3)
with c1:
    crit_c = st.slider("Crit Chance %", 0, 200, 50)
    crit_m = st.slider("Crit Multiplier", 1.0, 10.0, 2.0)
with c2:
    faction = st.selectbox("Faction Mod (Bane/Smite)", [0, 30, 55], format_func=lambda x: f"+{x}%" if x > 0 else "None")
with c3:
    fire_rate = st.slider("Fire Rate (per second)", 1.0, 20.0, 5.0)

# Average Crit Multiplier = 1 + [CritChance * (CritMult - 1)]
avg_crit = 1 + (crit_c/100 * (crit_m - 1))
final_dps = total_mult_3d * avg_crit * (1 + faction/100) * fire_rate

st.divider()
st.subheader(f"Final Sustained Force: {final_dps:.2f} Damage Units")

st.write("### The Golden Rule of Modding")
st.success("""
**Don't double up on the same bucket.** Adding a second 'Base Damage' mod (like Heavy Caliber) to a build that already has Serration is like making your rectangle slightly longer but much narrower. 
You're almost always better off adding a **new dimension** (Elemental, Multishot, Crit, or Faction).
""")
