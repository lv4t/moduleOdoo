# models/models.py

from odoo import models, fields, api

class AgriculturalExportInventory(models.Model):
    _name = 'agri.export.inventory'
    _description = 'Inventory Management'

    name = fields.Char(string='Tên')
    product_id = fields.Many2one(string='Sản phẩm', required = True)
    location = fields.Many2one(string='Địa chỉ', required = True)
    quantity = fields.Float(string='Sản lượng', required = True)
