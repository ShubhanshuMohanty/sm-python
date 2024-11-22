# Dictionary of customers
customers = {
    101: "Rajesh Kumar",
    102: "Amit Sharma",
    103: "Vikram Singh"
}

# Print all customers
print("Customers:", customers)

# Print a specific customer by ID
print("Customer 101:", customers[101])

# Print a specific customer by ID using get method
print("Customer 103:", customers.get(103))

# Print all customer IDs
print("Customer IDs:", customers.keys())

# Update a customer's name
customers.update({101: "Rajesh"})
print("Updated Customers:", customers)

# Add a new customer
customers.update({104: "Manoj Verma"})
print("Added Manoj Verma:", customers)

# Add another new customer
customers[105] = "Ravi Patel"
print("Added Ravi Patel:", customers)

# Remove the last added customer
print("Removed last customer:", customers.popitem())
print("After removing last customer:", customers)

# Loop through all customer IDs
for customer_id in customers:
    print("Customer ID:", customer_id)
for customer_id in customers.keys():
    print("Customer ID:", customer_id)

# Loop through all customer names
for customer_name in customers.values():
    print("Customer Name:", customer_name)

# Loop through all customers and their names
for customer_id, customer_name in customers.items():
    print("Customer ID:", customer_id, "Customer Name:", customer_name)

# Remove a specific customer by ID
removed_customer = customers.pop(104, None)
if removed_customer is not None:
    print("Removed Customer ID 104:", removed_customer)
else:
    print("Customer ID 104 not found.")

# Print final list of customers
print("Final Customers:", customers)
