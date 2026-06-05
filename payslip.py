employees = [{"ID": 101, "Name": "asha", "Salary": 30000},{"ID": 102, "Name": "Hansi", "Salary": 31000},{"ID": 103, "Name": "sona", "Salary": 32000}]
def add_employee():
    emp_id = input("Enter Employee ID : ")
    name = input("Enter Employee Name : ")
    salary = int(input("Enter Basic Salary : "))
    new_employee = {"ID": emp_id,"Name": name,"Salary": salary}
    employees.append(new_employee)
    print("Employee Added Successfully")
def monthly_salary():
    for new_employee in employees:
        new_employee["Monthly Salary"] = new_employee["Salary"]
    print("Monthly Salary Calculated")
def bonus():
    for new_employee in employees:
        bonus_amount = new_employee["Salary"] * 5 / 100
        new_employee["Bonus"] = bonus_amount
    print("Bonus Calculated")
# Function to Generate Payslip
def payslip():
    print("\n------Payslip------")
    print("\n---------------------------------------------------------------------------------------------------------------")
    print("ID\t\tName\t\tSalary\t\tMonthly Salary\t\tBonus\t\t\tTotal Pay")
    print("-----------------------------------------------------------------------------------------------------------------")
    for new_employee in employees:
        total_pay = new_employee["Monthly Salary"] + new_employee["Bonus"]
        print(new_employee["ID"], "\t\t",new_employee["Name"], "\t\t",new_employee["Salary"], "\t\t",new_employee["Monthly Salary"], "\t\t\t",new_employee["Bonus"], "\t\t",total_pay)
    print("-----------------------------------------------------------------------------------------------------------------")
while True:
    print("\n-----Playslip Management System------\n")
    print("1. Add Employee")
    print("2. Calculate Monthly Salary")
    print("3. Calculate Bonus")
    print("4. Generate Payslip")
    print("5. Exit")
    option = input("Enter Your option : ")
    if option == "1":
        add_employee()
    elif option == "2":
        monthly_salary()
    elif option == "3":
        bonus()
    elif option == "4":
        payslip()
    elif option == "5":
        print("Sucessfully Created")
        break
    else:
        print("Invalid Option")