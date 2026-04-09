import NseUtility

# Create an instance of NSEUtility
nse = NseUtility.NseUtils()

# Fetch corporate actions for the last one month
# print(nse.get_corporate_action().head())

# Fetch corporate actions for a specific date range
# print(nse.get_corporate_action('01-01-2025', '31-01-2025').head())

# Fetch only Bonus data
# print(nse.get_corporate_action('01-01-2026', '31-03-2026', "Bonus"))

# Fetch only Dividend data
# print(nse.get_corporate_action('01-01-2025', '31-01-2025', "Dividend"))

# Fetch only Split data
# print(nse.get_corporate_action('01-01-2025', '31-01-2025', "Split"))

# Fetch only Buyback data
# print(nse.get_corporate_action('01-01-2025', '31-03-2025', "Buy Back"))