# Define a dictionary of electronics products with their prices
products = {"Laptop": 800, "Headphones": 50, "Smartphone": 600}

# Print all products
print("Products:", products)

# Print specific product price
print("Price of Laptop:", products["Laptop"])

# Print specific product price using get method
print("Price of Smartphone:", products.get("Smartphone"))

# Find all the keys (product names) from the dictionary
print("Product Names:", products.keys())

# Update a product's price
products.update({"Headphones": 55})
print("Updated Products:", products)

# Add a new product
products.update({"Tablet": 300})
print("Added Tablet:", products)

# Add another new product
products["Smartwatch"] = 200
print("Added Smartwatch:", products)

# Remove the last added product from the dictionary
print("Removing item:", products.popitem())
print("After removal:", products)

# Looping over the dictionary keys (product names)
for product_name in products:
    print("Product Name:", product_name)
for product_name in products.keys():
    print("Product Name:", product_name)

# Looping over the dictionary values (product prices)
for product_price in products.values():
    print("Product Price:", product_price)

# Traversing the dictionary to display product names and their prices
for product_name, product_price in products.items():
    print("Product Name:", product_name, "Price:", product_price)

# Remove a specific product and handle potential errors
removed_product = products.pop("Tablet", None)
if removed_product is not None:
    print("Removed Product Tablet:", removed_product)
else:
    print("Product Tablet not found.")

# Print final data of products dictionary
print("Final Products:", products)
