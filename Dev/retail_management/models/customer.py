from odoo import models, fields

class Customer(models.Model):
    _name = 'retail.customer'
    _description = 'Customer Management'

    name = fields.Char(string='Tên khách hàng', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Số điện thoại')
    address = fields.Char(string='Địa chỉ')
