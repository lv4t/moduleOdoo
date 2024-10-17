from odoo import models, fields

class Employee(models.Model):
    _name = 'retail.employee'
    _description = 'Employee Management'

    name = fields.Char(string='Employee Name', required=True)
    job_title = fields.Char(string='Job Title')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    branch_id = fields.Many2one('retail.branch', string='Branch')
