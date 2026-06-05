employees = [{"ID": 101, "Name": "Asha", "Salary": 30000},{"ID": 102, "Name": "Hansi", "Salary": 31000},{"ID": 103, "Name": "Sona", "Salary": 32000}]
def add_employee():
    emp_id = int(input("Enter Employee ID : "))
    name = input("Enter Employee Name : ")
    salary = int(input("Enter Basic Salary : "))
    new_employee = {"ID": emp_id,"Name": name,"Salary": salary}
    employees.append(new_employee)
    print("Employee Added Successfully")
def monthly_salary():
    for employee in employees:
        employee["Monthly Salary"] = employee["Salary"]
    print("Monthly Salary Calculated")
def bonus():
    for employee in employees:
        employee["Bonus"] = employee["Salary"] * 5 / 100
    print("Bonus Calculated")
def payslip():
    print("\n---------------- PAYSLIP ----------------")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print(f"{'ID':<10}{'Name':<15}{'Salary':<15}{'Monthly Salary':<20}{'Bonus':<10}{'Total Pay':<10}")
    print("-------------------------------------------------------------------------------------------------------------------------")
    for new_employee in employees:
        total_pay = new_employee["Monthly Salary"] + new_employee["Bonus"]
        print(f"{new_employee['ID']:<10}{new_employee['Name']:<15}{new_employee['Salary']:<15}{new_employee['Monthly Salary']:<20}{new_employee['Bonus']:<10}{total_pay:<10}")
    print("-------------------------------------------------------------------------------------------------------------------------")
while True:
    print("\n------ PAYSLIP MANAGEMENT SYSTEM ------\n")
    print("1. Add Employee")
    print("2. Calculate Monthly Salary")
    print("3. Calculate Bonus")
    print("4. Generate Payslip")
    print("5. Exit")
    option = input("Enter Your Option : ")
    if option == "1":
        add_employee()
    elif option == "2":
        monthly_salary()
    elif option == "3":
        bonus()
    elif option == "4":
        payslip()
    elif option == "5":
        print("Successfully Completed")
        break
    else:
        print("Invalid Option")
