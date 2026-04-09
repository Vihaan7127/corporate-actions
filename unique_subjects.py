import NseUtility
import pandas as pd
import os

nse = NseUtility.NseUtils()
output_path = r"D:\OneDrive - Neo Group\Vihaan Vora - Work\Arvesta NBFC\Code\CSV output"
os.makedirs(output_path, exist_ok=True)

all_actions = nse.get_corporate_action('01-01-2016', '31-03-2026')

if all_actions is not None and not all_actions.empty:
    subjects = all_actions['subject'].dropna().unique()
    subject_df = pd.DataFrame(sorted(subjects), columns=["Subject_Keywords"])
    file = os.path.join(output_path, "all_subject_keywords.csv")
    subject_df.to_csv(file, index=False)