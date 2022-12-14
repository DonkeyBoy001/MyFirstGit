from wtforms import Form, StringField
from wtforms.validators import Regexp


class GetStudentInformationForm(Form):
    # 学生编号为10位数字
    student_id = StringField(validators=[Regexp(regex=r'^[0-9]{10}$', message='The student number should be 10 digits.')])
