# models/financial.py

from odoo import models, fields

class Financial(models.Model):
    _name = 'agri.export.financial'
    _description = 'Agricultural Export Financial Management'

    name = fields.Char(string='Tài liệu tài chính', required=True)
    document_date = fields.Date(string='Ngày ')
    amount = fields.Float(string='Số lượng')
    description = fields.Text(string='Mô tả')
