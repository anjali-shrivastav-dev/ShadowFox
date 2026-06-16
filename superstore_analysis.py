# Superstore Sales Analysis Project


import pandas as pd
import plotly.express as px

# -----------------------
# 1. Load & Clean Data
# -----------------------
df = pd.read_csv("Superstore.csv", encoding="ISO-8859-1")

# Convert to datetime
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

# Handle missing values
df = df.dropna()

# Remove outliers (extreme high sales values)
df = df[df["Sales"] < df["Sales"].quantile(0.99)]

# -----------------------
# 2. Sales & Profit by Category / Sub-Category
# -----------------------
category_sales = df.groupby("Category")["Sales"].sum().reset_index()
fig1 = px.bar(category_sales, x="Category", y="Sales", title="Sales by Category", text_auto=True)
fig1.show()

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().reset_index()
fig2 = px.bar(subcategory_sales, x="Sub-Category", y="Sales",
              title="Sales by Sub-Category", text_auto=True)
fig2.show()

# -----------------------
# 3. Profit by Region
# -----------------------
region_profit = df.groupby("Region")["Profit"].sum().reset_index()
fig3 = px.bar(region_profit, x="Region", y="Profit", title="Profit by Region", text_auto=True,
              color="Profit", color_continuous_scale="Viridis")
fig3.show()

# -----------------------
# 4. Discount Impact on Profit
# -----------------------
fig4 = px.scatter(df, x="Discount", y="Profit",
                  title="Discount Impact on Profit",
                  color="Category", size="Sales", hover_data=["Sub-Category"])
fig4.show()

# -----------------------
# 5. Sales vs Profit Scatter
# -----------------------
fig5 = px.scatter(df, x="Sales", y="Profit", color="Category",
                  title="Sales vs Profit Analysis",
                  size="Quantity", hover_data=["Sub-Category"])
fig5.show()

# -----------------------
# 6. Time-based Sales & Profit Trends
# -----------------------
monthly_sales = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
monthly_sales["Order Date"] = monthly_sales["Order Date"].astype(str)

fig6 = px.line(monthly_sales, x="Order Date", y="Sales", title="Monthly Sales Trend")
fig6.show()

monthly_profit = df.groupby(df["Order Date"].dt.to_period("M"))["Profit"].sum().reset_index()
monthly_profit["Order Date"] = monthly_profit["Order Date"].astype(str)

fig7 = px.line(monthly_profit, x="Order Date", y="Profit", title="Monthly Profit Trend")
fig7.show()

# -----------------------
# 7. Customer Segment Analysis
# -----------------------
segment_perf = df.groupby("Segment")[["Sales", "Profit"]].sum().reset_index()
fig8 = px.bar(segment_perf, x="Segment", y=["Sales","Profit"],
              barmode="group", title="Sales vs Profit by Customer Segment")
fig8.show()

# -----------------------
# 8. Sales-to-Profit Ratio
# -----------------------
category_ratio = (df.groupby("Category")["Profit"].sum() /
                  df.groupby("Category")["Sales"].sum()).reset_index()
category_ratio.columns = ["Category", "Sales-to-Profit Ratio"]
print("\nSales-to-Profit Ratio by Category:")
print(category_ratio)

# -----------------------
# 9. Numerical Insights
# -----------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_discount = df["Discount"].sum()

best_category = category_sales.sort_values("Sales", ascending=False).iloc[0]["Category"]
worst_category = category_sales.sort_values("Sales").iloc[0]["Category"]

best_region = region_profit.sort_values("Profit", ascending=False).iloc[0]["Region"]
worst_region = region_profit.sort_values("Profit").iloc[0]["Region"]

print("\n--- Numerical Insights ---")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Total Discount Given: {total_discount:,.2f}")
print(f"Best Performing Category (Sales): {best_category}")
print(f"Worst Performing Category (Sales): {worst_category}")
print(f"Most Profitable Region: {best_region}")
print(f"Least Profitable Region: {worst_region}")

# -----------------------
# 10. Written Recommendations
# -----------------------
print("\n--- Recommendations ---")
print("1. Increase focus on high-sales categories like Technology and Office Supplies.")
print("2. Reduce discounts in categories where it negatively impacts profit margins.")
print("3. Target underperforming regions with marketing or supply chain improvements.")
print("4. Consider optimizing shipping strategies to reduce losses in low-profit regions.")
print("5. Explore strategies to improve profitability in the Corporate segment.")
print("6. Leverage growth periods from time-series trends for promotional campaigns.")
