from wtforms import Form, StringField, SelectField, IntegerField, validators, DateField
from wtforms.validators import Regexp


class UUIDForm(Form):
    uuid = StringField("UUID", [Regexp("^([A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}"
                                       "(,[A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12}){0,})$",
                                       message="Invalid UUID")])


class PasswordForm(Form):
    password = StringField("Password", [Regexp("^(\w{4,64})$", message="Invalid Password")])


class LoginForm(PasswordForm):
    username = StringField("Username", [Regexp("^(\w{4,64})$", message="Invalid Username")])


class TaskTypeForm(Form):
    name = StringField("Name", [Regexp("^(\w{4,64})$", message="Invalid Name")])


class ReasonForm(Form):
    reason = StringField("Reason", [Regexp("^(.{4,64})$", message="Invalid Reason")])


class PermForm(Form):
    permission = SelectField("Permission", choices=[('admin','admin'),('supervisor','supervisor'),
                                                    ('employee','employee'),('manager','manager')])


class RegisterForm(LoginForm,PermForm):
    telephone = StringField("Telephone",[Regexp("^((13[0-9])|(14[5|7])|(15([0-3]|[5-9]))|(18[0,5-9]))\\d{8}$",
                                                message="Invalid Telephone")])
    sex = SelectField("Sex", choices=[('m','m'),('f','f')])


class AuditStateForm(UUIDForm):
    state = SelectField("State", choices=[('audit', 'audit'),('noaudit', 'noaudit')])


class CheckStateForm(UUIDForm):
    state = SelectField("State", choices=[('checkin', 'checkin'),('checkout', 'checkout')])


class DateForm(Form):
    date = DateField("Date")


class AuditForm(DateForm):
    state = SelectField("State", choices=[('audit', 'audit'), ('noaudit', 'noaudit')])
    permission = SelectField("Permission", choices=[('employee', 'employee'), ('supervisor', 'supervisor')])
    #date = StringField("Date", [Regexp("^(\d{4}-\d{1,2}-\d{1,2})$", message="Invalid Date")])


class PwdForm(Form):
    originalpwd = StringField("Password", [Regexp("^(\w{4,64})$", message="Invalid Password")])
    updatepwd = StringField("Password", [Regexp("^(\w{4,64})$", message="Invalid Password")])


class AddTaskForm(Form):
    username = StringField("Username", [Regexp("^(\w{4,64})$", message="Invalid Username")])


class AddBookArrangementTask(Form):
    assignor_id = StringField("Assignor_id", [Regexp("^([A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12})$",
                                                       message="Invalid UUID Format")])
    #area = StringField("Area", [Regexp("^.{3,200}$", message="Invalid area Format")])
    dt_task = SelectField("Dt_task", choices=[('daily', 'daily'), ('temporary', 'temporary')])
    tasktype = SelectField("TaskType", choices=[('图书整理', '图书整理'), ('倒架统计', '倒架统计'),
                                                ('图书回架', '图书回架'), ('图书盘点', '图书盘点'),
                                                ('错架率抽样', '错架率抽样'), ('分拣系统', '分拣系统')])

class GetArea(Form):
    tasktype = SelectField("TaskType", choices=[('图书整理', '图书整理'), ('倒架统计', '倒架统计'),
                                                ('图书回架', '图书回架'), ('图书盘点', '图书盘点'),
                                                ('错架率抽样', '错架率抽样')])



class SelectTaskDetails(Form):
    # uuid = StringField("Assignor_id", [Regexp("^([A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12})$",
    #                                                  message="Invalid UUID Format")])
    uuid = StringField("Assignor_id", [Regexp("^([A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12})$",
                                                       message="Invalid UUID Format")])


class ReviewOneTask(Form):
    status = SelectField("Status", choices=[('0', '0'), ('1', '1')])


class GetAllUncheckedTask(Form):
    oneDate = DateField("Date")


class DateForm(Form):
    date = StringField("Date", [Regexp("^(\d{4}-\d{1,2}-\d{1,2})$", message="Invalid Password")])


class UpdatePwdForm(PasswordForm, UUIDForm):
    None
    pass


class ItemForm(Form):
    type = StringField("Type", [Regexp("^(.{2,12})$", message="Invalid Type")])
    item = StringField("Item", [Regexp("^(.{2,12})$", message="Invalid Item")])
    score = IntegerField("Score", [validators.NumberRange(min=1, max=100)])
    percentage = StringField("Percentage", [Regexp("^(\d{1,3}\%)$", message="Invalid Percentage")])
    standard = StringField("Standard", [Regexp("^(.{4,100})$", message="Invalid Standard")])


class SubmitInspectForm(Form):
    audit = StringField("UUID", [Regexp("^([A-Fa-f0-9]{8}-([A-Fa-f0-9]{4}-){3}[A-Fa-f0-9]{12})$",
                                        message="Invalid UUID")])
    content = StringField("Content", [Regexp("^(.{10,250})$", message="Invalid Content")])

