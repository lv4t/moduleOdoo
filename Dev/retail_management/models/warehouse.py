from odoo import models, fields

class Warehouse(models.Model):
    _name = 'retail.warehouse'
    _description = 'Warehouse Management'

    name = fields.Char(string='Warehouse Name', required=True)
    product_type = fields.Selection([
        ('pepper', 'Pepper'),
        ('cashew', 'Cashew'),
        ('coffee', 'Coffee')
    ], string='Product Type', required=True)
    product_id = product_type,
    purchase_price = fields.Float(string='Purchase Price', required=True)
    sale_price = fields.Float(string='Sale Price', required=True)
    quantity = fields.Float(string='Quantity (kg)', required=True)
    location = fields.Char(string='Location')
