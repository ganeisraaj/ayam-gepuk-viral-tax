import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

@st.cache_data
def load_data():
    df = pd.read_csv("streamlit/ayam_gepuk_full.csv")
    df["boneless"] = df["boneless"].map({"Yes": 1, "No": 0})
    df["viral"] = df["viral"].map({"Yes": 1, "No": 0})
    return df

df = load_data()

brand_summary = df.groupby("brand").agg(
    avg_price=("dine_in_price_rm", "mean"),
    avg_rating=("google_rating", "mean"),
    total_reviews=("google_reviews", "sum"),
    ig_followers=("ig_followers", "first"),
    tiktok_views=("tiktok_views_est", "first"),
    num_outlets=("num_outlets", "first"),
    viral_tax=("viral_tax_rm", "mean"),
    price_premium_pct=("price_premium_pct", "mean"),
    hype_score=("hype_score", "max"),
    viral=("viral", "first"),
    boneless=("boneless", "first"),
).round(2)

MEDIAN_PRICE = df["dine_in_price_rm"].median()

st.title("🍗 The Ayam Gepuk Viral Tax Report")
st.markdown(
    f"How much are you paying for hype? Analysis of **{df['brand'].nunique()} brands** "
    f"and **{len(df)} outlets** across Klang Valley. "
    f"Median market price: **RM{MEDIAN_PRICE:.2f}**. Data collected August 2026."
)

st.divider()

## Brand Explorer
st.header("🔍 Brand Explorer")
selected = st.selectbox("Pick a brand to inspect", sorted(df["brand"].unique()))
brand_data = df[df["brand"] == selected]
row = brand_summary.loc[selected]

#verdict
if row["viral_tax"] > 2:
    verdict = "🔴 Heavy viral tax — you're paying a significant hype premium"
elif row["viral_tax"] > 0.5:
    verdict = "🟡 Mild viral tax — slightly above market"
elif row["viral_tax"] > -0.5:
    verdict = "🟢 Fair price — right at market rate"
else:
    verdict = "💚 Below market — solid value pick"

st.markdown(f"### {selected}")
st.info(verdict)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Dine-in price", f"RM{row['avg_price']:.2f}")
col2.metric("Viral tax", f"RM{row['viral_tax']:+.2f}",
            f"{row['price_premium_pct']:+.1f}% vs median")
col3.metric("Rating", f"{row['avg_rating']:.1f} ⭐")
col4.metric("Hype score", f"{row['hype_score']:.0f}/100")

col5, col6, col7, col8 = st.columns(4)
col5.metric("Outlets", int(row["num_outlets"]))
col6.metric("IG followers", f"{row['ig_followers']:,}")
col7.metric("TikTok views", f"{row['tiktok_views']/1e6:.1f}M")
col8.metric("Boneless?", "Yes ✓" if row["boneless"] else "No ✗")

st.dataframe(
    brand_data[["outlet", "area", "dine_in_price_rm", "delivery_price_rm",
                "google_rating", "google_reviews", "sambal_options"]].rename(columns={
        "outlet": "Outlet",
        "area": "Area",
        "dine_in_price_rm": "Dine-in (RM)",
        "delivery_price_rm": "Delivery (RM)",
        "google_rating": "Rating",
        "google_reviews": "Reviews",
        "sambal_options": "Sambal options",
    }),
    hide_index=True,
    use_container_width=True
)

st.divider()

## Market Overview
st.header("📊 Market Overview")

st.markdown("""
| | Brand | Price | Note |
|---|---|---|---|
| 🏆 Most expensive | Ayam Gepuk Hut | RM16.90 | Mall premium, +RM4.00 viral tax |
| 💚 Best value | Ayam Getok Mantul | RM11.50 | Rated 4.33, below median |
| 🔥 Most hyped | Ayam Gepuk Pak Gembus | RM13.90 | Hype score 100/100 |
| 🤩 Most viral | Gepuklah | RM15.60 | Influencer-founded, boneless |
| 💰 Cheapest | Ayam Gepuk Citarasa | RM8.90 | RM8 cheaper than Gepuk Hut |
""")

st.divider()

## Chart 1 — Viral tax
st.subheader("Who charges the most above market?")
fig1, ax1 = plt.subplots(figsize=(10, 7))
bs = brand_summary.sort_values("viral_tax", ascending=True)
colors = ["tomato" if v > 0 else "steelblue" for v in bs["viral_tax"]]
ax1.barh(bs.index, bs["viral_tax"], color=colors)
ax1.axvline(0, color="black", linewidth=0.8)
ax1.set_xlabel("Viral tax (RM vs median market price)")
red_patch = mpatches.Patch(color="tomato", label="Above median")
blue_patch = mpatches.Patch(color="steelblue", label="Below median")
ax1.legend(handles=[red_patch, blue_patch])
plt.tight_layout()
st.pyplot(fig1)

## Chart 2 — Hype vs price scatter
st.subheader("Hype vs price premium")
fig2, ax2 = plt.subplots(figsize=(10, 7))
scatter = ax2.scatter(
    brand_summary["hype_score"],
    brand_summary["viral_tax"],
    s=brand_summary["avg_rating"] * 30,
    c=brand_summary["viral"],
    cmap="RdYlGn",
    alpha=0.8,
    edgecolors="grey",
    linewidth=0.5
)

notable = [
    "Ayam Gepuk Pak Gembus", "Gepuklah", "Ayam Gepuk Hut",
    "Ayam Gepuk Top Global", "Ayam Gepuk Citarasa",
    "Ayam Getok Mantul", "Ayam Gepuk Tok Mat", "Ayam Gepuk Papa Jon"
]

for brand, row2 in brand_summary.iterrows():
    if brand in notable:
        ax2.annotate(brand, (row2["hype_score"], row2["viral_tax"]),
                    fontsize=8, fontweight="bold",
                    xytext=(6, 6), textcoords="offset points")

ax2.axhline(0, color="black", linewidth=0.8, linestyle="--")
ax2.set_xlabel("Hype score (reviews + IG + TikTok + outlets)")
ax2.set_ylabel("Viral tax (RM vs median)")
plt.colorbar(scatter, label="Viral brand")
plt.tight_layout()
st.pyplot(fig2)

## Chart 3 — Rating vs viral tax
st.subheader("Are pricier brands actually better rated?")
st.caption("Correlation: 0.65 — yes, mostly, but not always")
fig3, ax3 = plt.subplots(figsize=(10, 6))
ax3.scatter(brand_summary["viral_tax"], brand_summary["avg_rating"],
            s=100, color="steelblue", edgecolors="grey", alpha=0.8)
for brand, row2 in brand_summary.iterrows():
    ax3.annotate(brand, (row2["viral_tax"], row2["avg_rating"]),
                fontsize=7, xytext=(4, 4), textcoords="offset points")
ax3.axvline(0, color="grey", linestyle="--", linewidth=0.8)
ax3.set_xlabel("Viral tax (RM vs median)")
ax3.set_ylabel("Average Google rating")
plt.tight_layout()
st.pyplot(fig3)

st.divider()
st.caption("Data collected August 2026 | Built by Ganeisraaj Kathiravan | github.com/ganeisraaj")
