"""
==========================================================================
  LAS Collateral Basket - Corporate Actions CSV Extractor
  Extracts ALL types of corporate actions from NSE and saves to CSV
==========================================================================

HOW TO USE:
  1. Change the FROM_DATE and TO_DATE below to your desired date range
  2. Uncomment/comment (#) the action types you want/don't want
  3. Run the script: click the Play button in VS Code
  4. CSV files will be saved in the OUTPUT_FOLDER path below

NOTE: Each action type is on a separate line so you can easily
      comment out (add #) any type you don't need.
==========================================================================
"""

import NseUtility
import pandas as pd
import os
from datetime import datetime

# ======================= CHANGE DATES HERE ==============================
FROM_DATE = "01-01-2026"    # Start date (DD-MM-YYYY)
TO_DATE   = "31-03-2026"    # End date   (DD-MM-YYYY)
# ========================================================================

# ======================= OUTPUT FOLDER ==================================
OUTPUT_FOLDER = r"D:\OneDrive - Neo Group\Vihaan Vora - Work\Arvesta NBFC\Code\CSV output"
# ========================================================================

# Create NSE connection
print("Connecting to NSE...")
nse = NseUtility.NseUtils()
print("Connected!\n")

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# ======================= ACTION TYPES ===================================
# Comment out (add # at start) any line you DON'T need
# Uncomment (remove #) any line you DO need
# The filter keyword is what NSE searches for in the 'subject' column
# ========================================================================

actions = {
    # --- DIVIDENDS ---
    "Dividend":             nse.get_corporate_action(FROM_DATE, TO_DATE, "Dividend"),
    "Interim_Dividend":     nse.get_corporate_action(FROM_DATE, TO_DATE, "Interim Dividend"),
    "Special_Dividend":     nse.get_corporate_action(FROM_DATE, TO_DATE, "Special Dividend"),

    # --- SHARE CHANGES ---
    "Bonus":                nse.get_corporate_action(FROM_DATE, TO_DATE, "Bonus"),
    "Face_Value_Split":     nse.get_corporate_action(FROM_DATE, TO_DATE, "Split"),
    "Rights":               nse.get_corporate_action(FROM_DATE, TO_DATE, "Rights"),
    "Consolidation":        nse.get_corporate_action(FROM_DATE, TO_DATE, "Consolidation"),

    # --- CORPORATE RESTRUCTURING ---
    "Buyback":              nse.get_corporate_action(FROM_DATE, TO_DATE, "Buy Back"),
    "Demerger":             nse.get_corporate_action(FROM_DATE, TO_DATE, "Demerger"),
    "Amalgamation":         nse.get_corporate_action(FROM_DATE, TO_DATE, "Amalgamation"),
    "Scheme_of_Arrangement":nse.get_corporate_action(FROM_DATE, TO_DATE, "Scheme"),
    "Capital_Reduction":    nse.get_corporate_action(FROM_DATE, TO_DATE, "Capital Reduction"),
    "Delisting":            nse.get_corporate_action(FROM_DATE, TO_DATE, "Delisting"),

    # --- DEBT / FIXED INCOME ---
    "Distribution":         nse.get_corporate_action(FROM_DATE, TO_DATE, "Distribution"),
    "Interest_Payment":     nse.get_corporate_action(FROM_DATE, TO_DATE, "Interest Payment"),
    "Redemption":           nse.get_corporate_action(FROM_DATE, TO_DATE, "Redemption"),

    # --- MEETINGS ---
    "AGM":                  nse.get_corporate_action(FROM_DATE, TO_DATE, "Annual General Meeting"),
    "EGM":                  nse.get_corporate_action(FROM_DATE, TO_DATE, "Extra"),
}

# ======================= SAVE TO CSV ====================================
print("=" * 60)
print(f"  Date Range: {FROM_DATE} to {TO_DATE}")
print(f"  Output:     {OUTPUT_FOLDER}")
print("=" * 60)

total_saved = 0

for name, data in actions.items():
    if data is not None and not data.empty:
        file_path = os.path.join(OUTPUT_FOLDER, f"{name}.csv")
        data.to_csv(file_path, index=False)
        print(f"  Saved  {name}: {len(data)} rows")
        total_saved += 1
    else:
        print(f"  Empty  {name}: no data found")

# Also save one combined file with ALL corporate actions (unfiltered)
print("\nFetching all actions combined...")
all_data = nse.get_corporate_action(FROM_DATE, TO_DATE)
if all_data is not None and not all_data.empty:
    all_file = os.path.join(OUTPUT_FOLDER, "All_Corporate_Actions.csv")
    all_data.to_csv(all_file, index=False)
    print(f"  Saved  All_Corporate_Actions: {len(all_data)} rows")

print("\n" + "=" * 60)
print(f"  Done! {total_saved} CSV files saved.")
print("=" * 60)