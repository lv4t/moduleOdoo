from odoo import models, fields

class ExportBatch(models.Model):
    _name = 'export.batch'
    _description = 'Export Batch'

    name = fields.Char(string='Batch Name', required=True)
    product_id = fields.Many2one('export.warehouse', string='Product', required=True)
    quantity = fields.Float(string='Quantity (kg)', required=True)
    create_date = fields.Datetime(string='Create Date', default=fields.Datetime.now)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped')
    ], string='State', default='draft')
