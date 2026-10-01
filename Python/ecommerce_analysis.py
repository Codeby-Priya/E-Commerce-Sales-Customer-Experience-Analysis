import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# E-COMMERCE SALES & CUSTOMER EXPERIENCE ANALYSIS
# ============================================================

# ============================================================
# 1. LOAD DATASET
# ============================================================

df = pd.read_csv("Data/ecommerce_sales_analytics_5000.csv")

# Convert order_date to datetime
df["order_date"] = pd.to_datetime(df["order_date"])


# ============================================================
# 2. DATA UNDERSTANDING
# ============================================================

print("\nDATA TYPES")
print("--------------------------------")
print(df.dtypes)

print("\nUNIQUE PRODUCT CATEGORIES")
print("--------------------------------")
print(df["product_category"].unique())

print("\nUNIQUE REGIONS")
print("--------------------------------")
print(df["region"].unique())

print("\nUNIQUE PAYMENT METHODS")
print("--------------------------------")
print(df["payment_method"].unique())

print("\nQUANTITY RANGE")
print("--------------------------------")
print(df["quantity"].min(), "to", df["quantity"].max())

print("\nDISCOUNT RANGE")
print("--------------------------------")
print(df["discount"].min(), "to", df["discount"].max())

print("\nCUSTOMER RATING RANGE")
print("--------------------------------")
print(df["customer_rating"].min(), "to", df["customer_rating"].max())

print("\nDELIVERY DAYS RANGE")
print("--------------------------------")
print(df["delivery_days"].min(), "to", df["delivery_days"].max())

print("\nUNIT PRICE RANGE")
print("--------------------------------")
print(df["unit_price"].min(), "to", df["unit_price"].max())

print("\nREVENUE RANGE")
print("--------------------------------")
print(df["revenue"].min(), "to", df["revenue"].max())


# ============================================================
# 3. KEY BUSINESS KPIs
# ============================================================

total_revenue = df["revenue"].sum()
total_orders = df["order_id"].nunique()
total_customers = df["customer_id"].nunique()
total_quantity = df["quantity"].sum()

average_order_value = total_revenue / total_orders
average_rating = df["customer_rating"].mean()
average_delivery = df["delivery_days"].mean()

print("\nKEY BUSINESS KPIs")
print("--------------------------------")
print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Order Value: ₹{average_order_value:,.2f}")
print(f"Average Customer Rating: {average_rating:.2f}/5")
print(f"Average Delivery Time: {average_delivery:.2f} days")


# ============================================================
# 4. REVENUE BY PRODUCT CATEGORY
# ============================================================

category_revenue = (
    df.groupby("product_category")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

print("\nREVENUE BY PRODUCT CATEGORY")
print("--------------------------------")
print(category_revenue)


# ============================================================
# 5. SALES BY PRODUCT CATEGORY
# ============================================================

category_sales = (
    df.groupby("product_category")
    .agg(
        orders=("order_id", "nunique"),
        quantity_sold=("quantity", "sum")
    )
    .sort_values("orders", ascending=False)
)

print("\nSALES BY PRODUCT CATEGORY")
print("--------------------------------")
print(category_sales)


# ============================================================
# 6. AVERAGE ORDER VALUE BY CATEGORY
# ============================================================

category_aov = (
    df.groupby("product_category")["revenue"]
    .mean()
    .sort_values(ascending=False)
)

print("\nAVERAGE ORDER VALUE BY CATEGORY")
print("--------------------------------")
print(category_aov.round(2))


# ============================================================
# 7. REVENUE TREND
# ============================================================

monthly_revenue = (
    df.groupby(df["order_date"].dt.to_period("M"))["revenue"]
    .sum()
)

print("\nMONTHLY REVENUE")
print("--------------------------------")
print(monthly_revenue)

print("\nDATE RANGE")
print("--------------------------------")
print("First Order Date:", df["order_date"].min())
print("Last Order Date:", df["order_date"].max())
print("Number of Months:", df["order_date"].dt.to_period("M").nunique())


yearly_data = df[df["order_date"] < "2035-01-01"]

yearly_revenue = (
    yearly_data.groupby(yearly_data["order_date"].dt.year)["revenue"]
    .sum()
    .sort_index()
)

print("\nYEARLY REVENUE")
print("--------------------------------")
print(yearly_revenue)


# ============================================================
# 8. REGIONAL PERFORMANCE
# ============================================================

region_analysis = (
    df.groupby("region")
    .agg(
        orders=("order_id", "nunique"),
        quantity_sold=("quantity", "sum"),
        revenue=("revenue", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\nREGIONAL PERFORMANCE")
print("--------------------------------")
print(region_analysis)


# ============================================================
# 9. DISCOUNT ANALYSIS
# ============================================================

discount_analysis = (
    df.groupby("discount")
    .agg(
        orders=("order_id", "nunique"),
        quantity_sold=("quantity", "sum"),
        revenue=("revenue", "sum")
    )
)

discount_analysis["avg_order_value"] = (
    discount_analysis["revenue"] / discount_analysis["orders"]
)

print("\nDISCOUNT ANALYSIS")
print("--------------------------------")
print(discount_analysis.round(2))


# ============================================================
# 10. CUSTOMER ANALYSIS
# ============================================================

customer_analysis = (
    df.groupby("customer_id")
    .agg(
        orders=("order_id", "nunique"),
        quantity_sold=("quantity", "sum"),
        revenue=("revenue", "sum")
    )
    .sort_values("revenue", ascending=False)
)

print("\nTOP 10 CUSTOMERS BY REVENUE")
print("--------------------------------")
print(customer_analysis.head(10))


# ============================================================
# 11. DELIVERY TIME VS CUSTOMER RATING
# ============================================================

delivery_rating_analysis = (
    df.groupby("delivery_days")["customer_rating"]
    .mean()
)

print("\nAVERAGE CUSTOMER RATING BY DELIVERY DAYS")
print("--------------------------------")
print(delivery_rating_analysis.round(2))

correlation = df["delivery_days"].corr(df["customer_rating"])

print("\nDELIVERY TIME VS CUSTOMER RATING")
print("--------------------------------")
print(f"Correlation: {correlation:.3f}")


# ============================================================
# 12. PAYMENT METHOD ANALYSIS
# ============================================================

payment_analysis = (
    df.groupby("payment_method")
    .agg(
        orders=("order_id", "nunique"),
        quantity_sold=("quantity", "sum"),
        revenue=("revenue", "sum")
    )
    .sort_values("orders", ascending=False)
)

print("\nPAYMENT METHOD ANALYSIS")
print("--------------------------------")
print(payment_analysis)

# ============================================================
# END OF PYTHON ANALYSIS
# ============================================================

print("\n========================================")
print("PYTHON ANALYSIS COMPLETED SUCCESSFULLY")
print("========================================")

# Revenue by Product Category

category_revenue = df.groupby("product_category")["revenue"].sum().sort_values(ascending=False)

category_revenue.plot(kind="bar", title="Revenue by Product Category")

plt.xlabel("Product Category")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("Charts/revenue_by_category.png")
plt.close()

# Revenue by Region

region_revenue = df.groupby("region")["revenue"].sum().sort_values(ascending=False)

region_revenue.plot(kind="bar", title="Revenue by Region")

plt.xlabel("Region")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("Charts/revenue_by_region.png")
plt.close()

# Revenue by Year

yearly_data = df[df["order_date"] < "2035-01-01"]

yearly_revenue = yearly_data.groupby(
    yearly_data["order_date"].dt.year
)["revenue"].sum()

yearly_revenue.plot(
    kind="line",
    marker="o",
    title="Revenue Trend by Year"
)

plt.xlabel("Year")
plt.ylabel("Revenue")
plt.tight_layout()

plt.savefig("Charts/revenue_trend_by_year.png")
plt.close()

# Discount vs Average Order Value

discount_analysis = df.groupby("discount")["revenue"].mean()

discount_analysis.index = discount_analysis.index * 100

discount_analysis.plot(
    kind="line",
    marker="o",
    title="Discount vs Average Order Value"
)

plt.xlabel("Discount (%)")
plt.ylabel("Average Order Value")
plt.tight_layout()

plt.savefig("Charts/discount_vs_aov.png")
plt.close()

# Top 10 Customers by Revenue

top_customers = (
    df.groupby("customer_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

top_customers.plot(
    kind="bar",
    title="Top 10 Customers by Revenue"
)

plt.xlabel("Customer ID")
plt.ylabel("Total Revenue")
plt.tight_layout()

plt.savefig("Charts/top_10_customers.png")
plt.close()

# Delivery Time vs Customer Rating

delivery_rating = df.groupby("delivery_days")["customer_rating"].mean()

delivery_rating.plot(
    kind="line",
    marker="o",
    title="Delivery Time vs Customer Rating"
)

plt.xlabel("Delivery Days")
plt.ylabel("Average Customer Rating")
plt.tight_layout()

plt.savefig("Charts/delivery_vs_rating.png")
plt.close()

# Payment Method Usage

payment_counts = df["payment_method"].value_counts()

payment_counts.plot(
    kind="bar",
    title="Payment Method Usage"
)

plt.xlabel("Payment Method")
plt.ylabel("Number of Orders")
plt.tight_layout()

plt.savefig("Charts/payment_method_usage.png")
plt.close()