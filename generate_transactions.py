import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Seed for reproducibility
np.random.seed(42)
random.seed(42)

# Generate synthetic transaction dataset
n_records = 1000
start_date = datetime(2026, 1, 1)

account_ids = [f"ACC_{1000 + i}" for i in range(50)]
categories = ['Groceries', 'Electronics', 'Travel', 'Dining', 'Utilities', 'Entertainment']
locations = ['Mumbai', 'Pune', 'Delhi', 'Bangalore', 'International_Online']

data = []
for i in range(n_records):
    txn_id = f"TXN_{10000 + i}"
    acc_id = random.choice(account_ids)
    category = random.choice(categories)
    location = random.choice(locations)
    
    # Generate timestamp within 90 days
    txn_time = start_date + timedelta(
        days=random.randint(0, 90),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59)
    )
    
    # Base amount with occasional high-value anomalies (fraud candidates)
    if random.random() < 0.05:
        amount = round(random.uniform(50000, 250000), 2)  # Unusually high transaction
    else:
        amount = round(random.uniform(100, 15000), 2)
        
    data.append([txn_id, acc_id, txn_time, category, location, amount])

df_txns = pd.DataFrame(data, columns=['transaction_id', 'account_id', 'timestamp', 'category', 'location', 'amount'])
df_txns.to_csv('financial_transactions.csv', index=False)
print("✅ Generated financial_transactions.csv with 1,000 records successfully!")