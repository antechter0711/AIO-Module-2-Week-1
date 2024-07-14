

!gdown 1iA0WmVfW88HyJvTBSQDI5vesf-pgKabq

import pandas as pd

# Đọc tệp CSV vào pandas DataFrame
df = pd.read_csv('/content/advertising.csv')

data = df.to_numpy()

data = data[:5]
data

import numpy as np
sales_data = data[:, 3]
sales_max = np.max(sales_data)

sales_idx = np.argmax(sales_data)
sales_max, sales_idx

tv_mean = data[:, 0].mean()
tv_mean

sale_cond = data[:, 3] >= 15.0
radio_data = data[:, 1]

radio_cond = radio_data * sale_cond
radio_mean = np.sum(radio_cond) / np.sum(sale_cond)

radio_mean

newspaper_data = data[:, 2]
newspaper_mean = newspaper_data.mean()

newspaper_cond = newspaper_data > newspaper_mean
sales_data = data[:, 3]

sales_cond = sales_data * newspaper_cond
sales_sum = np.sum(sales_cond)

sales_sum

sales_data = data[:, 3]
sales_mean = sales_data.mean()
score_sales = np.where(
    sales_data < sales_mean,
    "Bad",
    np.where(sales_data > sales_mean, "Good", "Average")
)
score_sales

sale_cond = data[:, 3] >= 15.0
radio_data = data[:, 1]

radio_cond = radio_data * sale_cond
radio_mean = np.sum(radio_cond) / np.sum(sale_cond)

radio_mean

sales_data = data[:, 3]
sales_mean = sales_data.mean()
sub_mean = sales_data - sales_mean
sub_abs = abs(sales_data - sales_mean)
average_idx = np.argmin(sub_abs)
sales_average = sales_data[average_idx]
score_sales = np.where(
    sales_data < sales_mean,
    "Bad",
    np.where(sales_data > sales_average, "Good", "Average")
)
score_sales
