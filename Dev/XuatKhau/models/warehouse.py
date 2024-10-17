from odoo import models, fields

class Warehouse(models.Model):
    _name = 'export.warehouse'
    _description = 'Warehouse'

    name = fields.Char(string='Tên sản phẩm', required=True)
    product_type = fields.Selection([
        ('pepper', 'Tiêu'),
        ('cashew', 'Điều'),
        ('coffee', 'Cà phê')
    ], string='Loại sản phẩm', required=True)
    quantity = fields.Float(string='Số lượng (kg)', required=True)
    purchase_price = fields.Float(string='Giá nhập (VNĐ)', required=True)
    sale_price = fields.Float(string='Giá bán (VNĐ)', required=True)
    description = fields.Text(string='Mô tả sản phẩm')
