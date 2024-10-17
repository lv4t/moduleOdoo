from odoo import models, fields

class Cashew(models.Model):
    _name = 'warehouse.cashew'
    _description = 'Cashew Management'

    name = fields.Char(string='Product Name', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    weight_unit = fields.Selection([
        ('kg', 'Kg'),
        ('ton', 'Tons')
    ], string='Weight Unit', default='kg')
    location = fields.Char(string='Location')
    entry_date = fields.Date(string='Entry Date')  # Ngày nhập kho
    stock_quantity = fields.Integer(string='Stock Quantity')  # Số lượng tồn kho
