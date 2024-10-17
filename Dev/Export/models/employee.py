from odoo import models, fields, api
from datetime import datetime

class Attendance(models.Model):
    _name = 'export.attendance'
    _description = 'Employee Attendance'

    employee_id = fields.Many2one('export.employee', string='Nhân viên', required=True)
    check_in = fields.Datetime(string='Giờ vào', default=fields.Datetime.now)
    check_out = fields.Datetime(string='Giờ ra')
    state = fields.Selection([
        ('checked_in', 'Đã vào'),
        ('checked_out', 'Đã ra')
    ], string='Trạng thái', default='checked_in')

    @api.model
    def create(self, vals):
        attendance = super(Attendance, self).create(vals)
        attendance.employee_id.write({'last_attendance': datetime.now()})
        return attendance

    def check_out_employee(self):
        for record in self:
            if record.state == 'checked_in':
                record.write({
                    'check_out': datetime.now(),
                    'state': 'checked_out'
                })

class PersonalInfo(models.Model):
    _name = 'export.personalinfo'
    _description = 'Personal Information'

    employee_id = fields.Many2one('export.employee', string='Nhân viên', required=True)
    date_of_birth = fields.Date(string='Ngày sinh')
    address = fields.Char(string='Địa chỉ')
    phone_number = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    emergency_contact = fields.Char(string='Liên hệ khẩn cấp')

class Employee(models.Model):
    _name = 'export.employee'
    _description = 'Employee'

    name = fields.Char(string='Tên nhân viên', required=True)
    employee_id = fields.Char(string='Mã nhân viên', required=True)
    job_position = fields.Char(string='Chức vụ')
    salary = fields.Float(string='Lương')
    info = fields.Char(string='Thông tin', required=True)
    attendance_ids = fields.One2many('export.attendance', 'employee_id', string='Điểm danh')
    last_attendance = fields.Datetime(string='Điểm danh lần cuối')
    personal_info_ids = fields.One2many('export.personalinfo', 'employee_id', string='Thông tin cá nhân')
