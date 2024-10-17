# models/warehouse.py
from odoo import models, fields

class Warehouse(models.Model):
    _name = 'warehouse.management'
    _description = 'Warehouse Management'

    name = fields.Char(string='Product Name', required=True)
    product_type = fields.Selection([
        ('pepper', 'Pepper'),
        ('cashew', 'Cashew'),
        ('coffee', 'Coffee'),
    ], string='Product Type', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    location = fields.Char(string='Location')
