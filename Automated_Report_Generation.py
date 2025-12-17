import pandas as pd

# Step 1: Read data from file
data = pd.read_csv("data.csv")

# Step 2: Analyze data
total_sales = data["Sales"].sum()
average_sales = data["Sales"].mean()
highest_sales = data.loc[data["Sales"].idxmax()]
lowest_sales = data.loc[data["Sales"].idxmin()]

# Step 3: Generate report
report = f"""
AUTOMATED SALES REPORT
----------------------
Total Sales: {total_sales}
Average Sales: {average_sales:.2f}

Top Performer:
Name: {highest_sales['Name']}
Sales: {highest_sales['Sales']}

Lowest Performer:
Name: {lowest_sales['Name']}
Sales: {lowest_sales['Sales']}
"""

# Step 4: Save report to file
with open("sales_report.txt", "w") as file:
    file.write(report)

print("Report generated successfully!")
