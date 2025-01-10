# Pandas DataFrame Methods Cheatsheet

## Reading Data
Reading and inspecting data is typically the first step in any data analysis workflow.

```python
# Reading from different sources
df = pd.read_csv('sales_data.csv')
df = pd.read_excel('financial_report.xlsx')
df = pd.read_sql('SELECT * FROM customers', connection)

# Quick inspection
df.head()        # First 5 rows
df.info()        # DataFrame info (dtypes, non-null values)
df.describe()    # Statistical summary of numeric columns
```

## Data Cleaning
Clean data is essential for accurate analysis. Here are common cleaning operations:

```python
# Handling missing values
sales_df.dropna()                    # Remove rows with any missing values
sales_df.fillna({
    'revenue': 0,                    # Fill missing revenues with 0
    'customer_name': 'Unknown'       # Fill missing names with 'Unknown'
})

# Removing duplicates
customer_df.drop_duplicates(subset=['email'], keep='first')  # Keep first occurrence
```

## Data Transformation
Transform your data into the right format for analysis:

```python
# Date handling
orders_df['order_date'] = pd.to_datetime(orders_df['order_date'])
orders_df['month'] = orders_df['order_date'].dt.month
orders_df['year'] = orders_df['order_date'].dt.year

# String operations
customer_df['name'] = customer_df['name'].str.upper()
customer_df['email_domain'] = customer_df['email'].str.split('@').str[1]

# Categorical encoding
df['status'] = pd.Categorical(df['status'])
status_dummies = pd.get_dummies(df['status'], prefix='status')
```

## Data Analysis
Core analysis operations to extract insights from your data:

```python
# Grouping and aggregation
# Sales by product category and month
sales_summary = df.groupby(['category', 'month']).agg({
    'revenue': ['sum', 'mean'],
    'quantity': 'sum',
    'customer_id': 'count'  # Number of transactions
}).round(2)

# Filtering
# High-value transactions
high_value = df[df['amount'] > 1000]
# Recent customers
recent_customers = df[df['purchase_date'] > '2024-01-01']

# Sorting
# Top selling products
top_products = df.sort_values('quantity_sold', ascending=False).head(10)
```

## Combining DataFrames
Merge and concatenate data from different sources:

```python
# Merging customer and order data
merged_df = pd.merge(
    customers_df,
    orders_df,
    on='customer_id',
    how='left'  # Keep all customers even without orders
)

# Concatenating monthly reports
annual_report = pd.concat([jan_report, feb_report, mar_report], ignore_index=True)
```

## Feature Engineering
Create new features to enhance your analysis:

```python
# Creating new columns
df['profit'] = df['revenue'] - df['cost']
df['profit_margin'] = (df['profit'] / df['revenue'] * 100).round(2)

# Time-based features
df['days_since_last_purchase'] = (df['current_date'] - df['last_purchase']).dt.days
```

## Pivoting and Reshaping
Reorganize your data for different perspectives:

```python
# Creating a pivot table of sales by product and region
pivot_table = df.pivot_table(
    values='sales_amount',
    index='product_category',
    columns='region',
    aggfunc='sum',
    fill_value=0
)
```

## Export Data
Save your processed data:

```python
# Exporting processed data
df.to_csv('processed_sales.csv', index=False)
df.to_excel('quarterly_report.xlsx', sheet_name='Q1_2024')
```

## Performance Analysis
Analyze trends and performance metrics:

```python
# YoY (Year over Year) growth
df['yoy_growth'] = df.groupby('product')['sales'].pct_change(periods=12) * 100

# Rolling metrics
df['3_month_avg_sales'] = df.groupby('product')['sales'].rolling(window=3).mean()
```

## Common Data Quality Checks
Ensure data quality throughout your analysis:

```python
# Check for outliers using IQR
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)
IQR = Q3 - Q1
outliers = df[(df['price'] < (Q1 - 1.5 * IQR)) | (df['price'] > (Q3 + 1.5 * IQR))]

# Value counts and distributions
df['customer_segment'].value_counts(normalize=True) * 100  # Distribution in %
```

These examples cover the most common operations you'll encounter in daily data analysis tasks. Each method can be customized further based on specific requirements and data structures.
