employees = [{"ID": 101, "Name": "Asha", "Salary": 30000, "Projects": 0},{"ID": 102, "Name": "Hansi", "Salary": 31000, "Projects": 0},{"ID": 103, "Name": "Sona", "Salary": 32000, "Projects": 0}]
# Function to Add Employee
def add_employee():
    emp_id = int(input("Enter Employee ID : "))
    name = input("Enter Employee Name : ")
    salary = int(input("Enter Basic Salary : "))
    new_employee = {"ID": emp_id,"Name": name,"Salary": salary,"Projects": 0}
    employees.append(new_employee)
    print("Employee Added Successfully")
# Function to Calculate Monthly Salary
def monthly_salary():
    for new_employee in employees:
        basic_salary = new_employee["Salary"]
        house_rent = basic_salary * 10 / 100
        food_allowance = 2000
        travel_allowance = 1500
        monthly = basic_salary + house_rent + food_allowance + travel_allowance
        new_employee["HRA"] = house_rent
        new_employee["Food"] = food_allowance
        new_employee["Travel"] = travel_allowance
        new_employee["Monthly Salary"] = monthly
    print("Monthly Salary Calculated")
# Function to Calculate Bonus Based on Projects
def bonus():
    for new_employee in employees:
        projects = int(input(f"Enter Projects Completed by {new_employee['Name']} : "))
        new_employee["Projects"] = projects
        salary = new_employee["Salary"]
        if projects >= 6:
            bonus_amount = salary * 6 / 100
        elif projects >= 4:
            bonus_amount = salary * 4 / 100
        else:
            bonus_amount = salary * 2 / 100
        new_employee["Bonus"] = bonus_amount
    print("Bonus Calculated")
# Function to Generate Payslip
def payslip():
    print("\n---------------- PAYSLIP ----------------")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    print(f"{'ID':<8}"f"{'Name':<12}"f"{'Projects':<10}"f"{'Basic':<10}"f"{'HRA':<10}"f"{'Food':<10}"f"{'Travel':<10}"f"{'Monthly':<12}"f"{'Bonus':<10}"f"{'Total':<10}")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
    for new_employee in employees:
        monthly = new_employee["Monthly Salary"]
        bonus_amt = new_employee["Bonus"]
        total_pay = monthly + bonus_amt
        print(f"{new_employee['ID']:<8}"f"{new_employee['Name']:<12}"f"{new_employee['Projects']:<10}"f"{new_employee['Salary']:<10}"f"{new_employee['HRA']:<10}"f"{new_employee['Food']:<10}"f"{new_employee['Travel']:<10}"f"{monthly:<12}"f"{bonus_amt:<10}"f"{total_pay:<10}")
    print("---------------------------------------------------------------------------------------------------------------------------------------")
# Menu Driven Program
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