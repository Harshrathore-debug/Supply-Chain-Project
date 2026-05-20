# config.py
# ─────────────────────────────────────────────────────────────────────────────
# Central configuration — AtliQ Mart Supply Chain Decision Intelligence
# All business constants live here. Change once → applies everywhere.
# ─────────────────────────────────────────────────────────────────────────────

import os

# ── PATHS ─────────────────────────────────────────────────────────────────────
BASE_DIR      = os.path.dirname(os.path.abspath(__file__))
RAW_DIR       = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DIR = os.path.join(BASE_DIR, "data", "processed")

# Raw AtliQ Mart CSVs (download from Kaggle)
RAW_TABLES = {
    "order_lines":  os.path.join(RAW_DIR, "fact_order_lines.csv"),
    "orders_agg":   os.path.join(RAW_DIR, "fact_orders_aggregate.csv"),
    "customers":    os.path.join(RAW_DIR, "dim_customers.csv"),
    "products":     os.path.join(RAW_DIR, "dim_products.csv"),
    "date":         os.path.join(RAW_DIR, "dim_date.csv"),
    "targets":      os.path.join(RAW_DIR, "dim_targets_orders.csv"),
}

# Processed outputs
MASTER_DATA   = os.path.join(PROCESSED_DIR, "atliq_master.csv")
FORECAST_OUT  = os.path.join(PROCESSED_DIR, "forecast_output.csv")
DECISION_LOG  = os.path.join(PROCESSED_DIR, "decision_log.csv")


# ── COMPANY CONTEXT ───────────────────────────────────────────────────────────
COMPANY       = "AtliQ Mart"
INDUSTRY      = "FMCG — India"
FISCAL_YEAR   = "FY 2024–25"
CITIES        = ["Surat", "Ahmedabad", "Vadodara"]
CHANNELS      = ["Modern Trade", "General Trade"]
DIVISIONS     = ["Dairy", "Beverages", "Food"]


# ── KPI TARGETS (real AtliQ Mart targets from dataset) ────────────────────────
# These are the exact service level targets the company set for itself.
# Your decision engine fires when actuals fall below these.
KPI_TARGETS = {
    "otif_pct":    66.0,   # On-Time In-Full %  ← PRIMARY KPI
    "ot_pct":      86.0,   # On-Time %
    "if_pct":      76.0,   # In-Full %
    "vofr_pct":    96.5,   # Volume Fill Rate %
    "lifr_pct":    65.0,   # Line Item Fill Rate %
}


# ── DECISION ENGINE THRESHOLDS ────────────────────────────────────────────────
# Rules that trigger recommendations. Tied directly to KPI targets above.
OTIF_CRITICAL_THRESHOLD  = 50.0   # below this → customer churn risk
OTIF_WARNING_THRESHOLD   = KPI_TARGETS["otif_pct"]  # below target → alert
IF_CRITICAL_SKU_DAYS     = 3      # IF% below target for N consecutive days → emergency reorder
SUPPLIER_DELAY_TRIGGER   = 2      # delay > N days → switch supplier
WAREHOUSE_CAPACITY_MAX   = 0.85   # above 85% → reroute recommendation
DELAY_RATE_THRESHOLD     = 0.20   # above 20% delay rate → escalate


# ── FINANCIAL CONSTANTS (₹) ───────────────────────────────────────────────────
HOLDING_COST_PER_UNIT_DAY  = 2.0    # ₹/unit/day
STOCKOUT_PENALTY_PER_UNIT  = 45.0   # lost margin per unit not delivered
EXPEDITE_PREMIUM_PCT       = 0.18   # 18% extra cost for rush orders
CONTRACT_VALUE_AT_RISK     = 3_200_000  # ₹3.2Cr annual contract value at risk


# ── DECISION ACTIONS ──────────────────────────────────────────────────────────
ACTIONS = {
    "REORDER":   "Trigger emergency reorder",
    "REROUTE":   "Reroute to alternate city warehouse",
    "REBALANCE": "Rebalance stock across cities",
    "SWITCH":    "Switch to backup supplier",
    "ESCALATE":  "Escalate to operations manager",
    "HOLD":      "No action required — system stable",
}


# ── UI COLOURS (used by Streamlit pages) ──────────────────────────────────────
COLORS = {
    "primary":  "#0D9488",
    "navy":     "#0A1931",
    "success":  "#10B981",
    "warning":  "#F59E0B",
    "danger":   "#EF4444",
    "neutral":  "#64748B",
}


# ── SCENARIO DEFAULTS (Streamlit sliders start here) ─────────────────────────
SCENARIO_DEFAULTS = {
    "demand_change_pct":    0,
    "supplier_delay_days":  0,
    "cost_change_pct":      0,
    "warehouse_util_pct":   72,
}
