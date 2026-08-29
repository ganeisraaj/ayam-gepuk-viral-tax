# 🍗 The Ayam Gepuk Viral Tax Report
**Berapa yang kau bayar untuk hype?**

---

## 🚀 Live App

👉 **[The Ayam Gepuk Viral Tax Report — Live App](https://ganeisraaj-ayam-gepuk-viral-tax.streamlit.app/)**

Pick any brand and instantly see its viral tax, hype score, rating, and outlet breakdown.

---

## Overview

Ayam gepuk has taken Malaysia by storm. From humble warungs charging RM8.90 to mall concepts at RM16.90, the price gap between brands is enormous — and it doesn't always reflect quality.

This project quantifies the **viral tax**: how much more you pay for a brand simply because it went viral on TikTok or Instagram. Data covers 24 brands and 53 outlets across Klang Valley, collected August 2026.

---

## Key Findings

- **Median market price: RM12.90**
- **Ayam Gepuk Hut** charges the highest viral tax at **+RM4.00** (31% above median) — mall concept with salted egg extras
- **Gepuklah** charges **+RM2.70** (21% premium) — influencer-founded, boneless, nasi lemak base
- **Ayam Gepuk Pak Gembus** has the highest hype score (100/100) but charges only **+RM1.00** above median — big brand, fair price
- **Ayam Getok Mantul** is the best value: **RM11.50**, rated **4.33** — below median and better rated than most premium brands
- **Ayam Gepuk Citarasa** is the cheapest at **RM8.90** — RM8.00 cheaper than Gepuk Hut for essentially the same dish
- Price and rating correlate at **0.65** — pricier brands are mostly better, but not always

---

## The Viral Tax Formula

Viral Tax (RM) = Brand Price − Median Market Price (RM12.90)
Price Premium (%) = (Brand Price − Median) / Median × 100
Hype Score = Normalized average of: Google reviews + IG followers + TikTok views + outlet count


---

## Data

| Field | Description |
|---|---|
| Brand | Ayam gepuk brand name |
| Outlet | Specific branch |
| Area | Neighbourhood / city |
| Dine-in price | Standard ayam gepuk set, RM |
| Delivery price | GrabFood / Foodpanda price, RM |
| Google rating | Out of 5.0 |
| Google reviews | Total review count |
| IG followers | Brand Instagram following |
| TikTok views | Estimated total brand TikTok views |
| Outlets | Total number of branches nationwide |
| Boneless | Whether brand offers boneless option |
| Sambal options | Number of sambal heat levels |
| Viral | Whether brand is considered viral |

---

## Methods

- Viral tax and price premium computed against the dataset median (RM12.90)
- Hype score: min-max normalised sum of four social/scale metrics, scaled 0–100
- Correlation between price premium and Google rating: **r = 0.65**
- Data collected manually from Google Maps, brand websites, foodpanda, and food review articles

---

## Software

Python 3.12 · `pandas` · `numpy` · `matplotlib` · `streamlit`


This project is part of a portfolio targeting data science roles, with a focus on Malaysian and Southeast Asian topics.

👉 [HDB Resale Price Predictor](https://ganeisraaj-hdb-resale-predictor.streamlit.app/)
👉 [Malaysia Petrol Price Tracker](https://ganeisraaj-my-petrol-prices.streamlit.app/)
👉 [Diabetes Risk Predictor](https://ganeisraaj-diabetes-logistic.streamlit.app/)
👉 [Ruhr Climate Analysis](https://ganeisraaj-ruhr-climate.streamlit.app/)
