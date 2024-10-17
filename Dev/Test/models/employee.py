from odoo import models, fields

class Employee(models.Model):
    _name = 'my_module.employee'
    _description = 'Employee'

    name = fields.Char(string='Tên', required=True)
    position = fields.Char(string='Chức vụ')
    personal_info = fields.Text(string='Thông tin cá nhân')
    salary = fields.Float(string='Mức lương')
