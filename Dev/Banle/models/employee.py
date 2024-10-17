from odoo import models, fields, api
from datetime import datetime, timedelta

class Employee(models.Model):
    _name = 'retail.employee'
    _description = 'Employee'

    name = fields.Char(string='Tên nhân viên', required=True)
    employee_id = fields.Char(string='Mã nhân viên', required=True)
    attendance_ids = fields.One2many('retail.attendance', 'employee_id', string='Điểm danh')
    salary = fields.Float(string='Lương cơ bản (VNĐ)')
    work_location = fields.Many2one('retail.branch', string='Nơi làm việc', required=True)
    total_salary = fields.Float(string='Lương thực nhận (VNĐ)', compute='_compute_total_salary')
    personal_info_id = fields.One2many('retail.personalinfo', 'employee_id', string='Thông tin cá nhân')

    @api.depends('attendance_ids')
    def _compute_total_salary(self):
        for employee in self:
            total_days = sum(attendance.is_present for attendance in employee.attendance_ids)
            employee.total_salary = employee.salary * total_days

class Attendance(models.Model):
    _name = 'retail.attendance'
    _description = 'Attendance'

    employee_id = fields.Many2one('retail.employee', string='Nhân viên', required=True)
    date = fields.Date(string='Ngày', required=True, default=fields.Date.context_today)
    is_present = fields.Boolean(string='Có mặt', default=True)

class PersonalInfo(models.Model):
    _name = 'retail.personalinfo'
    _description = 'Personal Information'

    employee_id = fields.Many2one('retail.employee', string='Nhân viên', required=True)
    date_of_birth = fields.Date(string='Ngày sinh')
    cccd = fields.Char(string='Căn cước')
    address = fields.Char(string='Địa chỉ')
    phone_number = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
    emergency_contact = fields.Char(string='Liên hệ khẩn cấp')
