from odoo import models, fields

class ExportCustomer(models.Model):
    _name = 'export.customer'
    _description = 'Customer'

    name = fields.Char(string='Tên khách hàng', required=True)
    address = fields.Char(string='Địa chỉ')
    phone = fields.Char(string='Số điện thoại')
    email = fields.Char(string='Email')
