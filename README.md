# 🍗 The Ayam Gepuk Viral Tax Report
**Berapa yang kau bayar untuk hype?**

---

## 🚀 Live App

👉 **[The Ayam Gepuk Viral Tax Report — Live App](https://ganeisraaj-ayam-gepuk-viral-tax.streamlit.app/)**

Pick any brand and instantly see its viral tax, hype score, rating, and outlet breakdown.

---

## Overview

Ayam gepuk has taken Malaysia by storm. But does going viral mean charging more? This project quantifies the **viral tax**: how much more you pay for a brand simply because it went viral on TikTok or Instagram.

Data covers **8 brands and 18 outlets** across Klang Valley, collected August 2026. Only brands with verified dine-in prices from official websites, physical menu evidence, or reliable food journalism sources are included. Brands where prices could only be confirmed via delivery apps are excluded to avoid delivery markup distortion.

---

## Key Findings

- **Brand-level median dine-in price: RM14.93**
- **Gepuklah** charges the highest viral tax at **+RM4.98** (33% above median) — 1 outlet, influencer-founded, boneless, nasi lemak base
- **Ayam Gepuk Pak Gembus** has the highest hype score (100/100) with 70 outlets, yet charges only **+RM1.48** above median (~10%) — the biggest brand is not the most expensive
- **Ayam Gepuk Top Global** with 40 outlets is actually **below the median at RM14.25** — scale does not mean premium pricing
- **Gepuklah** also has the highest Google rating in the dataset at **4.6** — price and rating correlate strongly (r = 0.87) in this sample, suggesting the premium may be partially justified
- **Gesek Geprek** is the most affordable verified brand at **RM10.50**, followed by **Ayam Gepuk Artisan** at **RM10.99**

---

## The Viral Tax Formula

Viral Tax (RM) = Brand Price − Brand-level Median (RM14.93)
Price Premium (%) = (Brand Price − Median) / Median × 100
Hype Score = Normalised average of: Google reviews + IG followers + TikTok views + outlet count


---

## Data

| Field | Description |
|---|---|
| Brand | Ayam gepuk brand name |
| Outlet | Specific branch |
| Area | Neighbourhood / city |
| Dine-in price | Standard ayam gepuk set, RM — verified dine-in only |
| Delivery price | GrabFood / Foodpanda listed price, RM |
| Google rating | Out of 5.0 |
| Google reviews | Total review count |
| IG followers | Brand Instagram following |
| TikTok views | Estimated total brand TikTok views |
| Outlets | Total number of branches nationwide |
| Boneless | Whether brand offers boneless option |
| Sambal options | Number of sambal heat levels |
| Price source | Where the dine-in price was verified from |

---

## Methods

- Only brands with verified dine-in prices are included — official brand websites, confirmed physical menu evidence, or multiple consistent food journalism sources
- Delivery platform prices excluded due to typical 20-35% markup above dine-in
- Viral tax and price premium computed against the brand-level median (RM14.93)
- Hype score: min-max normalised sum of four social/scale metrics, scaled 0-100
- Pearson correlation between price and Google rating across 8 brands: **r = 0.87** (small sample, interpret with caution)
- Data collected August 2026

---

## Price Verification Sources

| Brand | Source |
|---|---|
| Gepuklah | says.com + ayampanas.com — permanent store opening coverage, Aug 2026 |
| Ayam Gepuk Pak Gembus | pricelisto.com — official menu prices, Aug 22 2026 |
| Ayam Gepuk Hut | trip.com + ioicitymall.com.my |
| King Ayam Gepuk | sethlui.com — physical visit 2026 |
| Ayam Gepuk Top Global | sethlui.com — physical visit 2026 |
| Ayam Gepuk Macet | makan.buddy Threads 2026 |
| Ayam Gepuk Artisan | ayamgepukartisan.my — official website |
| Gesek Geprek | gesekgeprek.com — official website |

---

## Software

Python 3.12 · `pandas` · `numpy` · `matplotlib` · `streamlit`

---

👉 [HDB Resale Price Predictor](https://ganeisraaj-hdb-resale-predictor.streamlit.app/)
👉 [Malaysia Petrol Price Tracker](https://ganeisraaj-my-petrol-prices.streamlit.app/)
👉 [Diabetes Risk Predictor](https://ganeisraaj-diabetes-logistic.streamlit.app/)
👉 [Ruhr Climate Analysis](https://ganeisraaj-ruhr-climate.streamlit.app/)
