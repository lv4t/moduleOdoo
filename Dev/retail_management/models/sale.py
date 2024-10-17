from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'retail.sale.order'
    _description = 'Sale Order'

    name = fields.Char(string='Order Reference', required=True)
    customer_id = fields.Many2one('retail.customer', string='Customer', required=True)
    date_order = fields.Datetime(string='Order Date', required=True, default=fields.Datetime.now)
    total_amount = fields.Float(string='Total Amount', compute='_compute_total_amount', store=True)
    order_line = fields.One2many('retail.sale.order.line', 'order_id', string='Order Lines')

    @api.depends('order_line.price_total')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_total for line in order.order_line)

class SaleOrderLine(models.Model):
    _name = 'retail.sale.order.line'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('retail.sale.order', string='Order Reference', required=True)
    product_id = fields.Many2one('retail.warehouse', string='Product', required=True)
    quantity = fields.Integer(string='Quantity', required=True)
    price_unit = fields.Float(string='Unit Price', related='product_id.sale_price', store=True)
    price_total = fields.Float(string='Total Price', compute='_compute_price_total', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit
