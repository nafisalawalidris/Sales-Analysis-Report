#!/usr/bin/env python
# coding: utf-8

# ## Step 1: Merge data from each month into one DataFrame ##
# 
# - Read the CSV files for each month using pandas' read_csv() function.
# - Concatenate the DataFrames vertically using pd.concat() to create a single DataFrame containing data for all 12 months.

# In[13]:


import pandas as pd

# Read CSV files for each month
df1 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_January_2019.csv')
df2 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_February_2019.csv')
df3 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_March_2019.csv')
df4 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_April_2019.csv')
df5 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_May_2019.csv')
df6 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_June_2019.csv')
df7 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_July_2019.csv')
df8 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_August_2019.csv')
df9 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_September_2019.csv')
df10 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_October_2019.csv')
df11 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_November_2019.csv')
df12 = pd.read_csv(r'C:\Users\USER\Desktop\Sales_Data\Sales_December_2019.csv')

# Concatenate DataFrames vertically
all_data = pd.concat([df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12], ignore_index=True)

# Display the first few rows of the merged DataFrame
all_data.head(10)


# ## Step 2: Clean up the data ##
# 
# - Drop any rows containing NaN values using dropna().
# - Remove rows based on a condition using boolean indexing.
# - Change the data type of columns using to_numeric(), to_datetime(), or astype() as required.

# In[15]:


# Drop NaN values
all_data.dropna(inplace=True)

# Removing rows based on a condition
all_data = all_data[all_data['Quantity Ordered'] != 'Quantity Ordered']

# Change the data type of columns
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# Display the cleaned-up data
print(all_data.head(10))


# ## Step 3: Create new columns ##
# 
# - Add a month column by extracting the month from the 'Order Date' column.
# - Add a city column by extracting the city from the 'Purchase Address' column.

# In[16]:


# Add month column
all_data['Month'] = all_data['Order Date'].dt.month

# Add city column
def get_city(address):
    return address.split(',')[1].strip()

all_data['City'] = all_data['Purchase Address'].apply(get_city)

# Display the updated DataFrame with new columns
print(all_data)


# ## Step 4: Answer the questions ##
# 
# ### Question 1: What was the best month for sales? How much was earned that month? ###
# 
# - Group the data by month and sum the 'Quantity Ordered' and 'Price Each' columns to calculate the total sales for each month.
# - Visualize the results using a bar graph.

# In[18]:


import matplotlib.pyplot as plt

months = range(1, 13)
plt.bar(months, monthly_sales, color='steelblue')

# Customizing the plot
plt.xlabel('Month')
plt.ylabel('Sales in USD')
plt.title('Total Sales per Month')
plt.xticks(months)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding colors to the bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'cornflowerblue', 'palegreen',
          'salmon', 'khaki', 'lightskyblue', 'palegoldenrod', 'powderblue', 'lightpink']
for i, bar in enumerate(plt.bar(months, monthly_sales)):
    bar.set_color(colors[i])

plt.show()


# ### Question 2: What city sold the most products? ###
# 
# - Group the data by city and sum the 'Quantity Ordered' column to calculate the total products sold in each city.
# - Visualize the results using a bar graph.

# In[21]:


import matplotlib.pyplot as plt

# Calculate total products sold per city
city_products = all_data.groupby('City')['Quantity Ordered'].sum()

# Visualize city-wise product sales
plt.bar(city_products.index, city_products, color='lightblue')

# Customizing the plot
plt.xlabel('City')
plt.ylabel('Total Products Sold')
plt.title('Product Sales by City')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding colors to the bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'cornflowerblue']
for i, bar in enumerate(plt.bar(city_products.index, city_products)):
    bar.set_color(colors[i % len(colors)])

plt.show()


# ### Question 3: What time should we display advertisements to maximize the likelihood of customers buying a product? ###
# 
# - Extract the hour from the 'Order Date' column.
# - Group the data by hour and count the number of orders in each hour.
# - Visualize the results using a line graph.

# In[22]:


import matplotlib.pyplot as plt

# Extract hour from Order Date
all_data['Hour'] = all_data['Order Date'].dt.hour

# Count orders by hour
hourly_orders = all_data.groupby('Hour')['Order ID'].count()

# Visualize hourly order counts
plt.plot(hourly_orders.index, hourly_orders, color='lightgreen', marker='o', linestyle='--')

# Customizing the plot
plt.xlabel('Hour')
plt.ylabel('Number of Orders')
plt.title('Order Distribution by Hour')
plt.xticks(range(0, 24))
plt.grid(linestyle='--', alpha=0.5)

# Adding colors to the line and markers
plt.plot(hourly_orders.index, hourly_orders, color='lightgreen', marker='o', linestyle='--', markersize=5)

plt.show()


# ### Question 4: What products are most often sold together? ###
# 
# - Identify rows with the same 'Order ID' and create a new column 'Grouped' that contains the products sold together for each order.
# - Group the data by the 'Grouped' column and count the frequency of different combinations of products.
# - Visualize the results using a bar graph.

# In[25]:


import matplotlib.pyplot as plt

# Create a new column 'Grouped' with products sold together in each order
grouped_data = all_data.groupby('Order ID')['Product'].transform(lambda x: ', '.join(x))

# Count frequency of product combinations
product_combinations = grouped_data.value_counts().head(10)

# Visualize product combinations
plt.bar(product_combinations.index, product_combinations, color='skyblue')

# Customizing the plot
plt.xlabel('Product Combination')
plt.ylabel('Frequency')
plt.title('Most Frequently Sold Product Combinations')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding colors to the bars
colors = ['lightblue', 'lightgreen', 'lightcoral', 'gold', 'cornflowerblue']
for i, bar in enumerate(plt.bar(product_combinations.index, product_combinations)):
    bar.set_color(colors[i % len(colors)])

plt.show()


# ### Question 5: What product sold the most? Why do you think it sold the most? ###
# 
# - Group the data by product and sum the 'Quantity Ordered' column to calculate the total quantity sold for each product.
# - Visualize the results using a bar graph.

# In[26]:


import matplotlib.pyplot as plt

# Calculate total quantity sold per product
product_quantity = all_data.groupby('Product')['Quantity Ordered'].sum()

# Visualize product-wise sales
plt.bar(product_quantity.index, product_quantity, color='lightblue')

# Customizing the plot
plt.xlabel('Product')
plt.ylabel('Total Quantity Sold')
plt.title('Product Sales')
plt.xticks(rotation=90)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Adding colors to the bars
colors = ['skyblue', 'lightgreen', 'lightcoral', 'gold', 'cornflowerblue']
for i, bar in enumerate(plt.bar(product_quantity.index, product_quantity)):
    bar.set_color(colors[i % len(colors)])

# Adding value labels to the bars
for bar in plt.bar(product_quantity.index, product_quantity):
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2, height, height, ha='center', va='bottom')

plt.show()


# In[ ]:




