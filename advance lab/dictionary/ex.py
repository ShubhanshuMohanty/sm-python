#Q.1) You have a list of employee records, and you need to create a new list that contains the names of employees who work in the 'Sales' department, all in uppercase. Hint:Create Dictionary with name, department and salary field

employee_records = [
    {"name": "Omkar", "department": "Sales", "salary": 50000},
    {"name": "Shubhanshu", "department": "HR", "salary": 60000},
    {"name": "Neeraj", "department": "Sales", "salary": 70000}
]

sales_employees = [emp["name"].upper() for emp in employee_records if emp["department"] == "Sales"]
print(sales_employees)