from odoo import models, fields

class Product(models.Model):
    _name = 'retail.product'
    _description = 'Product Management'

    name = fields.Char(string='Tên hàng', required=True)
    category = fields.Char(string='Phân loại')
    description = fields.Text(string='Description')
    price = fields.Float(string='Giá nhập')
    price1 = fields.Float(string='Giá xuất')
    stock_quantity = fields.Integer(string='Tồn kho', required=True)
