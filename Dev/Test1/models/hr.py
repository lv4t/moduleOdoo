# models/hr.py

from odoo import models, fields

class Employee(models.Model):
    _name = 'agri.export.employee'
    _description = 'Agricultural Export Employee'

    name = fields.Char(string='Tên nhân viên', required=True)
    department_id = fields.Many2one('hr.department', string='Vị trí làm việc')
    job_title = fields.Char(string='Chức vụ')
    salary = fields.Float(string='Lương')
