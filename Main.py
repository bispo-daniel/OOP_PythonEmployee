from Employee import Employee

employeesList = []

def getEmployeeId():
    print("\nType the employee's id to proceed...")
    id = int(input())

    return id

def createEmployee():
    print("Type the employee's id...")
    id = int(input())
    
    print("Type the employee's name...")
    name = input()
    
    print("Type the employee's salary...")
    salary = float(input())
    
    employeesList.append(Employee(id, name, salary))

    main()
    
def listEmployees():
    for yee in employeesList:
        print("\nId: ", yee.employeeId, " Name: ", yee.employeeName, " Salary: ", yee.employeeSalary)
        
    main()

def updateEmployee():
    theOne = getEmployeeId()
    
    for yee in employeesList:
        if yee.employeeId == theOne:

            print("\nWhat do you want to change? \n 1) Employee's Id \n 2) Employee's name \n 3) Employee's salary")
            op = int(input())

            print("\nType the new value: ")
            newValue = input()

            if op == 1:
                yee.employeeId = int(newValue)
            elif op == 2:
                yee.employeeName = newValue
            elif op == 3:
                yee.employeeSalary = float(newValue)

    main()


def deleteEmployee():
    theOne = getEmployeeId()

    for yee in employeesList:
        if yee.employeeId == theOne:
            employeesList.remove(yee)
            print("\nSuccessfully deleted...")
    
    main()

    
def main():
    try:
        operations = "\n 1) Create employee \n 2) List employees \n 3) Update employee \n 4) Delete employee \n 0) Exit"
        print("\nChoose the operation: \n", operations)
        op = int(input())
    
        if op == 0:
            SystemExit(0)
        elif op == 1:
            createEmployee()
        elif op == 2:
            listEmployees()
        elif op == 3:
            updateEmployee()
        elif op == 4:
            deleteEmployee()
        else:
            print("\nYou probably typed a letter wwhere a number is expected. Try again...")
            main()
    except:
        print("\nYou probably typed a letter wwhere a number is expected. Try again...")
        main()
main()