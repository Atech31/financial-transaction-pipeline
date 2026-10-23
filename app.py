import streamlit as st
import pandas as pd
import sqlite3
import os

st.set_page_config(page_title="Financial Transactions & Fraud Detection Pipeline", page_icon="💳", layout="wide")

st.title("💳 Real-Time Financial Transactions & Fraud Detection Dashboard")
st.markdown("Pipeline monitoring transaction logs, category-wise spend, and high-value fraud risk flags using SQLite & Python.")

if os.path.exists('financial_analytics.db'):
    conn = sqlite3.connect('financial_analytics.db')
    
    # Query 1: Overview Summary & High-Value Anomalies (Fraud Detection threshold > 50,000)
    query_fraud = """
    SELECT 
        transaction_id,
        account_id,
        timestamp,
        category,
        location,
        amount,
        CASE 
            WHEN amount > 50000 THEN 'HIGH RISK 🚨'
            ELSE 'NORMAL ✅'
        END as risk_status
    FROM transactions
    ORDER BY amount DESC
    """
    df_txns = pd.read_sql_query(query_fraud, conn)
    
    # Query 2: Category-wise Total Spend
    query_category = """
    SELECT 
        category,
        COUNT(transaction_id) as total_transactions,
        ROUND(SUM(amount), 2) as total_spend,
        ROUND(AVG(amount), 2) as avg_spend
    FROM transactions
    GROUP BY category
    ORDER BY total_spend DESC
    """
    df_cat = pd.read_sql_query(query_category, conn)
    
    conn.close()

    # Tabs layout
    tab1, tab2 = st.tabs(["🚨 Fraud & Risk Transaction Log", "📊 Category Spend Analytics"])

    with tab1:
        st.subheader("All Transactions & Automated Risk Flagging")
        st.dataframe(df_txns, use_container_width=True)
        
        high_risk_count = len(df_txns[df_txns['risk_status'] == 'HIGH RISK 🚨'])
        st.warning(f"⚠️ Total High-Risk Transactions Flagged: {high_risk_count}")

    with tab2:
        st.subheader("Category-wise Spending Breakdown")
        st.dataframe(df_cat, use_container_width=True)
        st.bar_chart(df_cat.set_index('category')['total_spend'])

else:
    st.error("Database `financial_analytics.db` not found. Please run `load_transactions_to_sqlite.py` first.")