# models/export_customer.py

from odoo import models, fields

class ExportCustomer(models.Model):
    _name = 'agri.export.customer'
    _description = 'Agricultural Export Customer'

    name = fields.Char(string='Tên khách hàng', required=True)
    country_id = fields.Many2one('res.country', string='Quốc gia')
    contact_info = fields.Text(string='Thông tin liên hệ')
