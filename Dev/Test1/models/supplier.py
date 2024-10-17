# models/supplier.py

from odoo import models, fields

class Supplier(models.Model):
    _name = 'agri.export.supplier'
    _description = 'Agricultural Export Supplier'

    name = fields.Char(string='Nhà cung cấp', required=True)
    country_id = fields.Many2one('res.country', string='Quốc gia')
    contact_info = fields.Text(string='Thông tin liên lạc')
