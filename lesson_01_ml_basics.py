import pandas as pd

# Create a dataset
data = {
    "house_size": [1000, 1500, 2000, 2500, 3000],
    "bedrooms": [2, 3, 3, 4, 4],
    "price": [10, 15, 20, 25, 30]
}

print(type(data))

# Convert data into a DataFrame
df = pd.DataFrame(data)

# Display the dataset
print(df)

# Display basic information
print(df.info())

# Display statistical summary
print(df.describe())