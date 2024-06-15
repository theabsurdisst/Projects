import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load dataset
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx'
data = pd.read_excel(url)

# Removed rows with missing values
data.dropna(inplace=True)

# Removed duplicate rows
data.drop_duplicates(inplace=True)

# Removed rows with negative or zero quantity and price
data = data[(data['Quantity'] > 0) & (data['UnitPrice'] > 0)]

# Converted InvoiceDate to datetime
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])

# Created 'TotalPrice' feature
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Extracted date features
data['InvoiceYear'] = data['InvoiceDate'].dt.year
data['InvoiceMonth'] = data['InvoiceDate'].dt.month
data['InvoiceDay'] = data['InvoiceDate'].dt.day
data['InvoiceHour'] = data['InvoiceDate'].dt.hour

# Defined the current date as the day after the last invoice date in the dataset
current_date = data['InvoiceDate'].max() + dt.timedelta(days=1)

# Calculated RFM values
rfm = data.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (current_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'TotalPrice': 'sum'
}).reset_index()

# Renamed columns
rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# Scaled RFM values
scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm[['Recency', 'Frequency', 'Monetary']])

# Determined the optimal number of clusters using the elbow method
inertia = []
for n in range(1, 11):
    kmeans = KMeans(n_clusters=n, random_state=42)
    kmeans.fit(rfm_scaled)
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker='o')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method')
plt.show()

# Applied K-means with the optimal number of clusters
optimal_clusters = 4
kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# the first few rows
print("RFM table with clusters assigned:")
print(rfm.head())

# function to recommend top N products for each cluster
def recommend_products(data, rfm, cluster, top_n=5):
    cluster_customers = rfm[rfm['Cluster'] == cluster]['CustomerID']
    cluster_data = data[data['CustomerID'].isin(cluster_customers)]
    
    top_products = cluster_data.groupby('StockCode')['TotalPrice'].sum().sort_values(ascending=False).head(top_n)
    return top_products

# Recommended top 5 products for each cluster
for cluster in range(optimal_clusters):
    print(f"\nTop 5 products for cluster {cluster}:")
    top_products = recommend_products(data, rfm, cluster=cluster, top_n=5)
    print(top_products)
    
    # Plotting
    plt.figure(figsize=(10, 6))
    top_products.plot(kind='bar')
    plt.title(f'Top 5 Products for Cluster {cluster}')
    plt.xlabel('Product StockCode')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.show()
