from odoo import models, fields, api
from calendar import monthrange


class ProductMonthlySalesSummary(models.Model):
    _name = 'product.monthly.sales.summary'
    _description = 'Tổng Kết Doanh Thu Theo Tháng Cho Từng Sản Phẩm'

    product_id = fields.Many2one('export.warehouse', string='Sản Phẩm', required=True)
    month = fields.Selection([(str(num), str(num)) for num in range(1, 13)], string='Tháng', required=True)
    year = fields.Char(string='Năm', required=True)
    total_quantity = fields.Float(string='Tổng Số Lượng (kg)', compute='_compute_totals', store=True)
    total_revenue = fields.Float(string='Tổng Doanh Thu', compute='_compute_totals', store=True)

    @api.depends('product_id', 'month', 'year')
    def _compute_totals(self):
        for record in self:
            if record.product_id and record.month and record.year:
                start_date = f'{record.year}-{record.month.zfill(2)}-01'
                last_day = monthrange(int(record.year), int(record.month))[1]
                end_date = f'{record.year}-{record.month.zfill(2)}-{last_day}'

                orders = self.env['export.order.line'].search([
                    ('product_id', '=', record.product_id.id),
                    ('order_id.order_date', '>=', start_date),
                    ('order_id.order_date', '<=', end_date)
                ])

                record.total_quantity = sum(line.quantity for line in orders)
                record.total_revenue = sum(line.price_total for line in orders)
