from odoo import models, fields, api, exceptions

class ExportFinancial(models.Model):
    _name = 'export.financial'
    _description = 'Export Financial'

    order_id = fields.Many2one('export.order', string='Đơn hàng', required=True)
    description = fields.Char(string='Mô tả', required=True)
    cost_shipping = fields.Float(string='Chi phí vận chuyển', required=True)
    cost_product = fields.Float(string='Chi phí sản phẩm', related='order_id.cost_product', store=True, readonly=True)
    cost_other = fields.Float(String='Chi phí khác', required=True)
    total_amount = fields.Float(string='Tổng thanh toán', related='order_id.total_amount', store=True, readonly=True)
    total_profit = fields.Float(string='Tổng thu', compute='_compute_total_profit', store=True)
    date = fields.Date(string='Ngày', required=True, default=fields.Date.today)

    @api.depends('total_amount', 'cost_shipping', 'cost_product', 'cost_other')
    def _compute_total_profit(self):
        for record in self:
            record.total_profit = record.total_amount - (record.cost_shipping + record.cost_product + record.cost_other)

    @api.model
    def create(self, vals):
        record = super(ExportFinancial, self).create(vals)
        order = record.order_id
        if record.cost_shipping:
            order.cost += record.cost_shipping
        if record.cost_product:
            order.cost += record.cost_product
        if record.cost_other:
            order.cost += record.cost_other
        return record
