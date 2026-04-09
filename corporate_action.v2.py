import NseUtility
import pandas as pd
import os

# Create an instance of NSEUtility
nse = NseUtility.NseUtils()

# Output folder
output_path = r"D:\OneDrive - Neo Group\Vihaan Vora - Work\Arvesta NBFC\Code\CSV output"
os.makedirs(output_path, exist_ok=True)

# Fetch corporate actions and save to CSV
actions = {
    # "Bonus": nse.get_corporate_action('01-01-2026', '31-03-2026', "Bonus"),
    # "Dividend": nse.get_corporate_action('01-01-2026', '31-03-2026', "Dividend"),
    # "Split": nse.get_corporate_action('01-01-2026', '31-03-2026', "Split"),
    # "Buy_Back": nse.get_corporate_action('01-01-2026', '31-03-2026', "Buy Back"),
    # "Rights": nse.get_corporate_action('01-01-2026', '31-03-2026', "Rights"),
    # "Demerger": nse.get_corporate_action('01-01-2026', '31-03-2026', "Demerger"),
    # "Amalgamation": nse.get_corporate_action('01-01-2020', '31-03-2026', "Amalgamation"),
    # "Redemption": nse.get_corporate_action('01-01-2025', '31-03-2026', "Redemption"),
    # "Distribution": nse.get_corporate_action('01-01-2025', '31-03-2026', "Distribution"),
    # "Interest Payment": nse.get_corporate_action('01-01-2025', '31-03-2026', "Interest Payment"),
    "Delisting": nse.get_corporate_action('01-01-2020', '31-03-2026', "Delisting"),
}

for name, data in actions.items():
    if data is not None and not data.empty:
        file = os.path.join(output_path, f"{name}.csv")
        data.to_csv(file, index=False)
        print(f"Saved {name}: {len(data)} rows → {file}")
    else:
        print(f"No {name} data found.")