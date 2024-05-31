def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours"))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hourly rate: "))
    return hourlyRate 

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, taxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printinfo(empName, hours, hourlyRate, gPay, taxRate, incomeTax, netPay):
    print(empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
    
def PrintTotals(totalEmployees, totalHours, totalGrossPay, totalTax, totalNetPay):
    print(f"Total number of employees: {totalEmployees}") 
    print(f"Total hours: {totalHours:,.2f}")
    print(f"Total gross pay: {totalGrossPay:,.2f}")
    print(f"Total tax: {totalTax:,.2f}")
    print(f"Total net pay: {totalNetPay:,.2f}")  
    
if __name__ == "__main__":
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalTax = 0.00
    totalNetPay = 0.00
    
while True:
    empName = getEmpName() 
    if (empName.upper() == "END"):
        break
    hours = getHoursWorked() 
    hourlyRate = getHourlyRate() 
    taxRate = getTaxRate()
    gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
    
    printinfo(empName, hours, hourlyRate, gPay, netPay, incomeTax, netPay)

    totalEmployees += 1
    totalHours += hours 
    totalGrossPay += gPay
    totalTax += incomeTax
    totalNetPay += netPay
    
    PrintTotals(totalEmployees,totalHours,totalGrossPay,totalTax,totalNetPay) 
    
def getdatesWorked():
    fromDate = input("Please enter start date in the following format MM/DD/YYYY: ")
    endDate = input("Please enter the end date in the following format MM/DD/YYYY: ")
    return fromDate, endDate

def getEmpName():
    empName = input("Enter employee name: ")
    return empName

def getHoursWorked():
    hours = float(input("Enter hours: "))
    return hours

def getHourlyRate():
    hourlyRate = float(input("Enter hpourly rate: "))
    return hourlyRate

def getTaxRate():
    taxRate = float(input("Enter tax rate: "))
    taxRate = taxRate / 100
    return taxRate

def CalcTaxAndNetPay(hours, hourlyRate, TaxRate):
    gPay = hours * hourlyRate
    incomeTax = gPay * taxRate
    netPay = gPay - incomeTax
    return gPay, incomeTax, netPay

def printInfo(empDetailList):
    totalEmployees = 0
    totalHours = 0.00
    totalGrossPay = 0.00
    totalNetpay = 0.00
    for emplist in empDetailList:
        fromDate = emplist[0]
        endDate = emplist[1]
        empName = emplist[2]
        hours = emplist[3]
        hourlyRate = emplist[4]
        taxRate = emplist[5]
        
        gPay, incomeTax, netPay = CalcTaxAndNetPay(hours, hourlyRate, taxRate)
        print(fromDate, endDate, empName, f"{hours:,.2f}", f"{hourlyRate:,.2f}", f"{gPay:,.2f}", f"{taxRate:,.1%}", f"{incomeTax:,.2f}", f"{netPay:,.2f}")
        totalEmployees += 1
        totalHours += hours
        totalGrossPay += gPay
        totalTax += incomeTax
        totalNetPay += netPay

        empTotals["totEmp"] = totalEmployees
        empTotals["totHours"] = totalHours
        empTotals["totGross"] = totalGrossPay
        empTotals["totTax"] = totalTax
        empTotals["totNet"] = totalNetPay

def printTotals(empTotals):
    print(f'Total Number of Employees: {empTotals["totEmp"]}')
    print(f'Total hours of the Employees: {empTotals["totHours"]}')
    print(f'Total Gross Pay of Employees: {empTotals["totGross"]}')
    print(f'Total Tax of Employees: {empTotals["totTax"]}')
    print(f'Total Net Pay of Employees: {empTotals["totNet"]}')
    
if __name__ == "__main__":
    empDetailList = []
    empTotal = {}
    while True:
        empName = getEmpName()
        if (empName.lower() == "end"):
            break
        fromDate, endDate = getDatesWorked()
        hours = getHoursWorked()
        hourlyRate = gethourlyRate()
        taxRate = getTaxRate()
        empDetail = []
        empDetail.insert(0, fromDate)
        empDetail.insert(1, empDate)
        empDetail.insert(2, empName)
        empDetail.insert(3, hours)
        empDetail.insert(4, hourlyRate)
        empDetail.insert(5, taxRate)
        empDetailList.append(empDetai)
    printInfo(empDetailList)
    printTotals(empTotals)
