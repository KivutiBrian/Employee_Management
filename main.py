# imports
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_sqlalchemy import SQLAlchemy

# importing the configs
from config.configs import Config,DevelopmentConfig,ProductionConfig

# import the payroll
from resources.employeeClass import Employee

# init flask
app = Flask(__name__)

# setting the app to use to development config
app.config.from_object(DevelopmentConfig)

# SQLALCHEMY
db = SQLAlchemy(app)

# models
from models.department import DepartmentModel
from  models.employee import EmployeeModel
from models.payroll import PayrollModel


@app.before_first_request
def create_tables():
    db.create_all()

# home route
@app.route('/')
def home():
    return render_template('homepage.html')

# departments route
@app.route('/departments', methods=['GET','POST'])
def departments():

    # fetching all departments and store them in a variable called all_my_depts
    all_my_depts = DepartmentModel.fetch_all_departments()

    # print(type(all_my_depts))

    # for x in all_my_depts:
    #     print(x.name)

    if request.method == 'POST':
        # fetch the user's input from the modal/form
        dept = request.form['fullName']

        # check if a department alread exists
        if DepartmentModel.check_dept_exist(dept):
            # if true warn the user it already exists
            flash('The department already', 'danger')
            return redirect(url_for('departments'))
        else:
            # if it is false, add the record to the database

            record = DepartmentModel(name=dept)
            record.create()

            flash('Department successfully added', 'success')

            return redirect(url_for('departments'))

    return render_template('departments.html', madepts=all_my_depts)


@app.route('/department/employees/<int:id>', methods=['GET','POST'])
def department_employees(id):

    dpt_emp = DepartmentModel.fetch_by_id(id)

    employees = dpt_emp.employee

    return render_template('departmentemp.html', wafanyakazi=employees,
                           dep=dpt_emp)

# employees
@app.route('/employees', methods=['GET','POST'])
def employees():

    all_my_depts = DepartmentModel.fetch_all_departments()

    allemps = EmployeeModel.fetch_all()
    # print(type(allemps))

    if request.method == 'POST':
        name = request.form['fullName']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        deptId = request.form['department']
        natId = request.form['natId']
        kraPin = request.form['krapin']
        basicsalary = request.form['basicsalary']
        benefits = request.form['benefits']

        if EmployeeModel.check_nationalId_exists(natId):
            print('already exists')
            return redirect(url_for('employees'))
        else:
            emp = EmployeeModel(fullName=name,gender=gender,email=email,phoneNumber=phone,nationalId=natId,
                                department_id=deptId,kraPin=kraPin,basicSalary=basicsalary,benefits=benefits)

            emp.create_record()

            print('success')

            return redirect(url_for('employees'))

    return render_template('employees.html', madepts=all_my_depts, employees= allemps)

@app.route('/employee/edit/<int:id>', methods=['POST'])
def edit_employees(id):
    if request.method == 'POST':
        name = request.form['fullName']
        gender = request.form['gender']
        email = request.form['email']
        phone = request.form['phone']
        deptId = request.form['department']
        natId = request.form['natId']
        kraPin = request.form['krapin']
        basicsalary = request.form['basicsalary']
        benefits = request.form['benefits']

        update = EmployeeModel.edit_employee_by_id(id=id,name=name,gender=gender,
                                                   email=email,phone=phone,
                                                   nationalId=natId,kra=kraPin,basic=basicsalary,
                                                   benefits=benefits,dptid=deptId)

        if update:
            print('update successful')
            return redirect(url_for('employees'))
        else:
            print('record not found')
            return redirect(url_for('employees'))

@app.route('/employee/delete/<int:id>', methods=['POST'])
def delete_employee(id):
    delete = EmployeeModel.delete_by_id(id)

    try:
        if delete:
            print('Successfully deleted')
            return redirect(url_for('employees'))
    except Exception as e :
        print('Unable to delete record at this this time')

# # payroll
# @app.route('/payrolls/<int:id>', methods=['GET','POST'])
# def payroll(id):
#     employee = EmployeeModel.fetch_emp_by_id(id)
#
#     return render_template('payroll.html', employees=employee)

@app.route('/generate/payroll/<int:id>', methods=['GET','POST'])
def generate_payroll(id):
    # fetch an employee by the id
    employee = EmployeeModel.fetch_emp_by_id(id)
    print(type(employee))

    mapayroll = PayrollModel.fetch_by_id(id)
    print(type(mapayroll))

    if request.method == 'POST':
        basic = float(request.form['basic'])
        benefits = float(request.form['benefits'])
        month = request.form['month']
        emp_id = request.form['emp_id']

        # create an object the the Employee class that we created as the task assignment on the python basics
        pay = Employee(basic_salary=basic,benefits=benefits)

        # gross salary = basic + benefits
        gross = pay.calculate_gross_salary()
        print('GROSS SALARY:',gross)

        nssf = pay.calculate_nssf()
        print('NSSF CONTRIBUTION:',nssf)

        # taxable income
        taxable_income = pay.calculate_taxable_income() #the income after pension deduction = grossSalary - nssfContribution
        print('INCOME AFTER PENSION DEDUCTION(TAXABLE INCOME)', taxable_income)

        # PAYEE
        paye = pay.calculate_payee() #tax on the taxable income
        print('PAYE(Tax on taxable income):', paye)

        # Relief
        personal_relief = pay.personal_relief
        print('PERSONAL RELIEF:', personal_relief)

        # tax payable: ie PAYEE
        tax_payable = pay.calculate_tax_payable()
        print('TAX PAYABLE(PAYEE):', tax_payable)

        # nhif contribution
        nhif_contribution = pay.calculate_nhif()
        print('NHIF CONTRIBUTION:',nhif_contribution)

        # net pay: carry home pay
        net_salary = pay.calculate_net_salary()
        print('NET SALARY(CARRY HOME PAY):',net_salary)

        # sending to database
        emp_payroll = PayrollModel(month=month,gross=gross,nssf=nssf,nhif=nhif_contribution,taxable_income=taxable_income,
                                   payee=paye,personal_relief=personal_relief,tax_payable=tax_payable,net_salary=net_salary,
                                   employee_id=emp_id)

        # insert the record to the db
        emp_payroll.create_record()



    return render_template('payroll.html', employees=employee, payroll=mapayroll)




if __name__ == '__main__':
    app.run(debug=True)