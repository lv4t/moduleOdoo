# models/customer.py
from odoo import models, fields

class ExportCustomer(models.Model):
    _name = 'export.customer'
    _description = 'Khách hàng'

    name = fields.Char(string='Tên khách hàng', required=True)
    address = fields.Char(string='Địa chỉ liên hệ', required=True)
    country = fields.Char(string='Quốc gia', required=True)
    contact_info = fields.Char(string='Thông tin liên lạc', required=True)
