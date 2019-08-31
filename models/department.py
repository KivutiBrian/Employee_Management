from main import db

class DepartmentModel(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=True, unique=True)
    employee = db.relationship('EmployeeModel', backref='department', lazy=True )

    # this is is a static method
    def create(self):
        db.session.add(self)
        db.session.commit()

    # check if dpt exist
    @classmethod
    def check_dept_exist(cls,dpt_name):
        record = cls.query.filter_by(name=dpt_name)

        # print(cls.query.filter_by(name=dpt_name))

        if record.first():
            return True
        else:
            return False

    # fecth all departments
    @classmethod
    def fetch_all_departments(cls):
        return cls.query.all()

    # fetch department by id
    @classmethod
    def fetch_by_id(cls,dpt_id):
        return cls.query.filter_by(id=dpt_id).first()