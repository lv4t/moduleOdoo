# models/employee.py
from odoo import models, fields

class ExportEmployee(models.Model):
    _name = 'export.employee'
    _description = 'Nhân viên phụ trách'

    name = fields.Char(string='Tên nhân viên', required=True)
    employee_id = fields.Char(string='Mã nhân viên', required=True)
    job_position = fields.Char(string='Vị trí công việc', required=True)
    contact_info = fields.Char(string='Thông tin liên lạc', required=True)
