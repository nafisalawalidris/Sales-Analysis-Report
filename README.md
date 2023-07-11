<!DOCTYPE html>
<html>
<head>
</head>
<body>
  <h1>Sales Analysis Repository</h1>

  <h2>Project Overview</h2>
  <p>
    This repository contains the analysis of sales data for Company XYZ. The objective of the analysis is to understand the reasons behind the decline in sales performance and suggest strategies for improvement. The analysis is based on a dataset that includes 12 months of sales transactions.
  </p>

  <h2>File Structure</h2>
  <pre><code>
sales_analysis/
├── data/
│   ├── month_1.csv
│   ├── month_2.csv
│   ├── ...
│   └── month_12.csv
├── notebooks/
│   ├── data_preparation.ipynb
│   ├── sales_analysis.ipynb
│   └── ...
└── README.html
  </code></pre>

  <h2>Data Preparation</h2>
  <p>
    To perform the analysis, the individual CSV files for each month were merged into a single DataFrame. The data was cleaned by dropping NaN values, removing rows with invalid quantities or prices and converting column data types. New columns were created to represent the month and city of each transaction.
  </p>
  <pre><code>
# Merge data from each month into one DataFrame
all_data = pd.concat([df1, df2, ..., df12], ignore_index=True)

# Clean up the data
all_data.dropna(inplace=True)
all_data = all_data[all_data['Quantity Ordered'] != 'Quantity Ordered']
all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'])
all_data['Price Each'] = pd.to_numeric(all_data['Price Each'])
all_data['Order Date'] = pd.to_datetime(all_data['Order Date'])

# Create new columns
all_data['Month'] = all_data['Order Date'].dt.month
all_data['City'] = all_data['Purchase Address'].apply(get_city)
  </code></pre>

  <h2>Analysis and Insights</h2>
  <p>
    The analysis aims to answer the following business-level questions:
  </p>
  <ul>
    <li>What was the best month for sales? How much was earned that month?</li>
    <li>What city sold the most products?</li>
    <li>What time should we display advertisements to maximize the likelihood of customer's buying a product?</li>
    <li>What products are most often sold together?</li>
    <li>What product sold the most? Why do you think it sold the most?</li>
  </ul>
  <p>
    To answer these questions, various techniques such as grouping, aggregation, and data visualization were employed. Bar graphs and line graphs were used to present the insights in an easily understandable manner.
  </p>

  <h2>Conclusion</h2>
  <p>
    Based on the analysis, recommendations can be made to improve sales performance. These may include targeted marketing campaigns in high-performing cities, optimizing the timing of advertisements, and bundling frequently sold together products. By implementing these strategies, Company XYZ can aim to increase its sales and overall business performance.
  </p>

</body>
</html>
