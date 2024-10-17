from odoo import models, fields

class Branch(models.Model):
    _name = 'retail.branch'
    _description = 'Branch Management'

    name = fields.Char(string='Branch Name', required=True)
    address = fields.Char(string='Address')
