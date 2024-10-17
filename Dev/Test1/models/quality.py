# models/quality.py

from odoo import models, fields

class QualityCheck(models.Model):
    _name = 'agri.export.quality'
    _description = 'Agricultural Export Quality Check'

    name = fields.Char(string='Kiểm tra chất lượng', required=True)
    product_id = fields.Many2one('agri.export.product', string='Sản phẩm')
    check_date = fields.Date(string='Ngày kiểm tra')
    result = fields.Selection([
        ('pass', 'Đạt'),
        ('fail', 'Chưa đạt'),
    ], string='Kết quả', required=True, default='pass')
