# EMPLOYEE CLASS
class Employee:
    basicSalary = 0
    benefits = 0
    grossSalary = 0 #Income before pensionable deduction
    taxableIncome = 0
    nssfContribution = 0
    nhifContribution = 0
    payee = 0 #PAYE : Tax on taxable income
    personal_relief = 1408
    total_tax_payable = 0
    netSalary = 0


  # constructor
    def __init__(self,basic_salary, benefits ):
        self.basicSalary = basic_salary
        self.benefits = benefits
        self.calculate_gross_salary()
        self.calculate_nssf()
        self.calculate_nhif()
        self.calculate_taxable_income()
        self.calculate_payee()
        self.calculate_taxable_income()
        self.calculate_net_salary()

  # calculate the gross-salary (bs + benefits)
    def calculate_gross_salary(self):
        # GROSS_SALARY = BASIC_SALARY + BENEFITS
        grossSalary = self.basicSalary + self.benefits

        self.grossSalary = grossSalary

        return grossSalary

  # calculate NSSF pension contribution
    def calculate_nssf(self):
        if 0 < self.grossSalary <= 6000:
          nssf = 0.06 * self.grossSalary
          self.nssfContribution = nssf
          return nssf
        elif 6000 < self.grossSalary < 18000 :
          remainder = self.grossSalary - 6000
          nssf = 6000 * 0.06 + remainder * 0.06
          self.nssfContribution = nssf
          return nssf
        elif self.grossSalary > 18000:
          nssf = 6000 * 0.06 + 12000 * 0.06
          self.nssfContribution = nssf
          return nssf

  # calculate NHIF Contribution
    def calculate_nhif(self):
        if 0 <= self.grossSalary <= 5999: # 0 - 5999
          nhif = 150
          self.nhifContribution = nhif
          return nhif
        elif 6000 <= self.grossSalary <= 7999: #6000 - 7999
          nhif = 300
          self.nhifContribution = nhif
          return nhif
        elif 8000 <= self.grossSalary <= 11999:
          nhif = 400
          self.nhifContribution = nhif
          return nhif
        elif 12000 <= self.grossSalary <= 14999: #12000 - 14999
          nhif = 500
          self.nhifContribution = nhif
          return nhif
        elif 15000 <= self.grossSalary < 19999: #15000 - 19999
          nhif = 600
          self.nhifContribution = nhif
          return nhif

    # calculate the NET SALARY
    def calculate_taxable_income(self):
        # net_taxable_income = Gross_salary -(NSSF pension contribution)

        nti = self.grossSalary - self.nssfContribution  # nti - net taxable income

        # Set the taxable income( income after pension deductions)
        self.taxableIncome = nti

        return nti

    # calculate PAYEE
    def calculate_payee(self):

        tier1 = 12298
        tier2 = 11587
        tier3 = 11587
        tier4 = 11587

        if self.taxableIncome <= 12298:
          tax = self.taxableIncome * 0.1
          self.payee = tax
          return tax
        elif 12299 <= self.taxableIncome <= 23885:
          remainder = self.taxableIncome - 12298
          tax = tier1 * 0.1 + 0.15 * remainder
          self.payee = tax
          return tax

    # calculate the net tax of the relief
    def calculate_tax_payable(self):

        # tax_payable = payee(the tax on taxable income) - personal_relief

        tax_payable = self.payee - self.personal_relief

        self.total_tax_payable = tax_payable

        return tax_payable

    # calculate net pay ie carry home pay
    def calculate_net_salary(self):

        # net_salary = Taxable_income - deductions
        net_sal = self.taxableIncome - (self.nhifContribution + self.total_tax_payable)

        return  net_sal


# emp1 = Employee(15000,  0 )
# print('Gross Pay',emp1.calculate_gross_salary())
# print('NSSF',emp1.nssfDeduction)
# print('NHIF',emp1.nhifContribution)
# print('Taxable income (net pay)',emp1.netSalary)
# print('tax charged',emp1.taxCharged)

