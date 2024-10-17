# models/sale_order_line.py
from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _name = 'retail.sale.order.line'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('retail.sale.order', string='Order Reference', required=True)
    product_id = fields.Many2one('retail.product', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price_unit = fields.Float(string='Unit Price', required=True)
    price_total = fields.Float(string='Total Price', compute='_compute_price_total', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit
