# models/export_order.py

from odoo import models, fields

class ExportOrder(models.Model):
    _name = 'agri.export.order'
    _description = 'Agricultural Export Order'

    name = fields.Char(string='Đơn hàng', required=True)
    customer_id = fields.Many2one('res.partner', string='Khách hàng')
    order_date = fields.Date(string='Ngày tạo đơn')
    shipping_date = fields.Date(string='Ngày vận chuyển')
    state = fields.Selection([
        ('draft', 'Nháp'),
        ('confirmed', 'Đã xác nhận'),
        ('done', 'Đã hoàn thành'),
        ('cancel', 'Đã hủy'),
    ], string='Status', default='draft', required=True)
