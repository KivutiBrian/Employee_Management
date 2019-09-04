from main import db

class EmployeeModel(db.Model):
    __tablename__ = 'employees'
    id = db.Column(db.Integer, primary_key=True)
    fullName = db.Column(db.String(), nullable=False)
    gender = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    phoneNumber = db.Column(db.String(), nullable=False)
    nationalId = db.Column(db.String(), nullable=False, unique=True)
    kraPin = db.Column(db.String(), nullable=False, unique=True)
    basicSalary = db.Column(db.Float, nullable=False)
    benefits = db.Column(db.Float, nullable=False)
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'))
    payrolls = db.relationship('PayrollModel', backref='payroll', lazy=True)

    # CREATE
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def check_nationalId_exists(cls,natId):
        record = cls.query.filter_by(nationalId=natId)

        if record.first():
            return True
        else:
            return False

    # fetch all employees
    @classmethod
    def fetch_all(cls):
        return  cls.query.all()

    @classmethod
    def fetch_emp_by_id(cls,id):
        return cls.query.filter_by(id=id).first()

    # edit by id
    @classmethod
    def edit_employee_by_id(cls,id,name=None,gender=None,email=None,phone=None,nationalId=None,kra=None,basic=None,benefits=None,dptid=None):
        record = cls.query.filter_by(id=id).first()

        if record:
            record.fullName = name
            record.gender = gender
            record.email = email
            record.phoneNumber = phone
            record.nationalId = nationalId
            record.kraPin = kra
            record.basicSalary = basic
            record.benefits = benefits
            record.department_id = dptid
            db.session.commit()
            return True
        else:
            return False

    # delete
    @classmethod
    def delete_by_id(cls, id):
        record = cls.query.filter_by(id=id)

        if record.first():
            record.delete()
            db.session.commit()
            return True
        else:
            return False