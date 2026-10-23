import pandas as pd
import sqlite3

# Load generated CSV dataset
df = pd.read_csv('financial_transactions.csv')

# Connect to SQLite database (creates financial_analytics.db)
conn = sqlite3.connect('financial_analytics.db')

# Load DataFrame into SQLite table named 'transactions'
df.to_sql('transactions', conn, if_exists='replace', index=False)

conn.close()
print("✅ Financial transactions successfully loaded into financial_analytics.db!")