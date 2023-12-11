import pandas as pd
from datetime import datetime

# Function to validate if a string is a valid date
def is_valid_date_ddmmyyyy(date_str):
    try:
        datetime.strptime(date_str, '%d-%m-%Y')
        return True
    except ValueError:
        return False

# Initialize variables
today_date = input("What is the date today? (DD-MM-YYYY): ")

if not is_valid_date_ddmmyyyy(today_date):
    print("Invalid date format. Please enter the date in YYYY-MM-DD format.")
    exit()

trades_today = input("Did you scalp today, take long trades, or both? ")
profit_loss = float(input("What is your final profit/loss today? "))
findings = input("What are the findings of chart analysis? ")
deployed_capital = float(input("What is your deployed capital today? "))

# Function to calculate ROI

roi = (profit_loss / deployed_capital) * 100

print(f"ROI: {roi:.2f}%")

return_percentage = roi
expected_charges = float(input("How many trades & charges today? "))
patience_level = input("How was your patience level today? ")
learned_new = input("What did you learn Today, Mistakes, findings or strategy? ")
Video_Link = input("Any Video link of Analysis or mistakes ? ")

# Create a DataFrame with the collected information
data = {
    "Date Today": [today_date],
    "Trade Types": [trades_today],
    "Profit/Loss Today": [profit_loss],
    "Findings of Chart Analysis": [findings],
    "Deployed Capital": [deployed_capital],
    "Return Percentage": [return_percentage],
    "Trades & Charges": [expected_charges],
    "Patience Level": [patience_level],
    "Learned New": [learned_new],
    "Video Link" : [Video_Link]
}

df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
file_name = "Tradingjournal.xlsx"
sheet_name = "November"


# Read the existing Excel file
existing_df = pd.read_excel(file_name, sheet_name=sheet_name)

# Concatenate the existing and new data
combined_df = pd.concat([existing_df, df], ignore_index=True)

# Write the combined data back to the Excel file
with pd.ExcelWriter(file_name, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    combined_df.to_excel(writer, sheet_name=sheet_name, index=False)

print(f"Data has been stored in {file_name}, sheet: {sheet_name}")
