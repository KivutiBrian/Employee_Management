from main import db

class PayrollModel(db.Model):
    __tablename__ = 'payrolls'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(), nullable=False)
    gross = db.Column(db.Float, nullable=False)
    nssf = db.Column(db.Float, nullable=False)
    nhif = db.Column(db.Float, nullable=False)
    taxable_income = db.Column(db.Float, nullable=False)
    payee = db.Column(db.Float, nullable=False)
    personal_relief = db.Column(db.Float, nullable=False)
    tax_payable = db.Column(db.Float, nullable=False)
    net_salary = db.Column(db.Float, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))

    # create
    def create_record(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def fetch_by_id(cls,id):
        return cls.query.filter_by(id=id).first()



