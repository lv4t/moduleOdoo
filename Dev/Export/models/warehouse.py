from odoo import models, fields

class Warehouse(models.Model):
    _name = 'export.warehouse'
    _description = 'Warehouse'


    product_type = fields.Selection([
        ('pepper', 'Tiêu hạt'),
        ('cashew', 'Điều Thô'),
        ('coffee', 'Cà phê ')
    ], string='Sản phẩm', required=True)
    quantity = fields.Float(string='Số lượng (Tấn)', required=True)
    purchase_price = fields.Float(string='Giá nhập (USD/Tấn)', required=True)
    sale_price = fields.Float(string='Giá bán (USD/Tấn)', required=True)
    description = fields.Text(string='Mô tả sản phẩm')
    date = fields.Date(string='Ngày nhập kho')
    quality = fields.Char(string='Chất lượng', required=True)
    supplier_id = fields.Char( string='Nhà cung cấp', required=True)