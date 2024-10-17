# models/shipping.py

from odoo import models, fields

class Shipping(models.Model):
    _name = 'agri.export.shipping'
    _description = 'Agricultural Export Shipping'

    name = fields.Char(string='Shipping Name', required=True)

    start_date = fields.Date(string='Ngày bắt đầu')
    end_date = fields.Date(string='Ngày đến theo dự kiến')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('transit', 'Đang vận chuyển'),
        ('delivered', 'Đã hoàn thành'),
        ('cancel', 'Đã hủy'),
    ], string='Trạng thái vận chuyển', default='draft', required=True)

