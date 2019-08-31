class Employee:
  basicSalary = 0
  benefits = 0
  grossSalary = 0
  netSalary = 0
  nssfDeduction = 0
  nhifContribution = 0
  taxCharged = 0

  # constructor
  def __init__(self,basic_salary, benefits ):
    self.basicSalary = basic_salary
    self.benefits = benefits
    self.calculate_gross_salary()
    self.calculate_nssf()
    self.calculate_nhif()
    self.calculate_taxable_income()
    self.calculate_payee()

  # calculate the gross-salary
  def calculate_gross_salary(self):
    self.grossSalary = self.basicSalary + self.benefits
    return self.grossSalary

  # calculate nssf Deduction
  def calculate_nssf(self):
    if 0 < self.grossSalary <= 6000:
      nssf = 0.06 * self.grossSalary
      self.nssfDeduction = nssf
      return nssf
    elif 6000 < self.grossSalary < 18000 :
      remainder = self.grossSalary - 6000
      nssf = 6000 * 0.06 + remainder * 0.06
      self.nssfDeduction = nssf
      return nssf
    elif self.grossSalary > 18000:
      nssf = 6000 * 0.06 + 12000 * 0.06
      self.nssfDeduction = nssf
      return nssf

  # calculate nhif Deduction
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
      return
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
    # net_taxable_income = Gross_salary - deductions
    deductions = self.nssfDeduction
    # print(deductions)
    nti = self.grossSalary - deductions
    self.netSalary = nti
    return nti

  # calculate PAYEE
  def calculate_payee(self):

    tier1 = 12298
    tier2 = 11587
    tier3 = 11587
    tier4 = 11587

    if self.netSalary <= 12298:
      tax = self.netSalary * 0.1
      self.taxCharged = tax
      return tax
    elif 12299 <= self.netSalary <= 23885:
      remainder = self.netSalary - 12298
      tax = tier1 * 0.1 + 0.15 * remainder
      self.taxCharged = tax

      return tax




emp1 = Employee(15000,  0 )
print('Gross Pay',emp1.calculate_gross_salary())
print('NSSF',emp1.nssfDeduction)
print('NHIF',emp1.nhifContribution)
print('Taxable income (net pay)',emp1.netSalary)
print('tax charged',emp1.taxCharged)

