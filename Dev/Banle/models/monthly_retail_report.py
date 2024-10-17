from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from dateutil.relativedelta import relativedelta
import datetime
import logging

_logger = logging.getLogger(__name__)

class MonthlyRetailReport(models.Model):
    _name = 'monthly.retail.report'
    _description = 'Báo cáo doanh thu hàng tháng'

    month = fields.Date(string='Tháng', required=True)
    revenue_pepper = fields.Float(string='Doanh thu Tiêu', compute='_compute_revenue', store=True)
    revenue_cashew = fields.Float(string='Doanh thu Điều', compute='_compute_revenue', store=True)
    revenue_coffee = fields.Float(string='Doanh thu Cà phê', compute='_compute_revenue', store=True)
    total_revenue = fields.Float(string='Tổng doanh thu', compute='_compute_total_revenue', store=True)
    line_ids = fields.One2many('monthly.retail.report.line', 'report_id', string='Chi tiết doanh thu')

    @api.depends('revenue_pepper', 'revenue_cashew', 'revenue_coffee')
    def _compute_total_revenue(self):
        for record in self:
            record.total_revenue = record.revenue_pepper + record.revenue_cashew + record.revenue_coffee

    @api.constrains('month')
    def _check_month(self):
        for record in self:
            if not isinstance(record.month, datetime.date):
                raise ValidationError(_("Trường 'Tháng' phải là một ngày hợp lệ."))

    @api.depends('month')
    def _compute_revenue(self):
        for record in self:
            try:
                if not record.month:
                    raise ValueError(_("Trường 'Tháng' không được để trống"))

                _logger.info(f"Tính toán doanh thu cho tháng: {record.month}")
                start_date = record.month.replace(day=1)
                end_date = start_date + relativedelta(months=1, days=-1)

                orders = self.env['retail.sale.order'].search([
                    ('date_order', '>=', start_date),
                    ('date_order', '<=', end_date)
                ])

                revenue_pepper = revenue_cashew = revenue_coffee = 0

                for order in orders:
                    for line in order.order_line:
                        product_type = line.product_id.product_type
                        if product_type == 'pepper':
                            revenue_pepper += line.price_total
                        elif product_type == 'cashew':
                            revenue_cashew += line.price_total
                        elif product_type == 'coffee':
                            revenue_coffee += line.price_total

                record.revenue_pepper = revenue_pepper
                record.revenue_cashew = revenue_cashew
                record.revenue_coffee = revenue_coffee

                _logger.info(f"Doanh thu đã được tính toán: Tiêu={revenue_pepper}, Điều={revenue_cashew}, Cà phê={revenue_coffee}")

            except Exception as e:
                _logger.error(f"Lỗi khi tính toán doanh thu cho bản ghi {record.id}: {str(e)}")
                record.revenue_pepper = record.revenue_cashew = record.revenue_coffee = 0

    @api.model
    def create(self, vals):
        record = super(MonthlyRetailReport, self).create(vals)
        record._create_report_lines()
        return record

    def write(self, vals):
        result = super(MonthlyRetailReport, self).write(vals)
        for record in self:
            record._create_report_lines()
        return result

    def _create_report_lines(self):
        self.ensure_one()
        self.line_ids.unlink()
        self.env['monthly.retail.report.line'].create([
            {'report_id': self.id, 'product_type': 'pepper', 'revenue': self.revenue_pepper},
            {'report_id': self.id, 'product_type': 'cashew', 'revenue': self.revenue_cashew},
            {'report_id': self.id, 'product_type': 'coffee', 'revenue': self.revenue_coffee},
        ])

class MonthlyRetailReportLine(models.Model):
    _name = 'monthly.retail.report.line'
    _description = 'Chi tiết báo cáo doanh thu hàng tháng'

    report_id = fields.Many2one('monthly.retail.report', string='Báo cáo', required=True, ondelete='cascade')
    product_type = fields.Selection([
        ('pepper', 'Tiêu'),
        ('cashew', 'Điều'),
        ('coffee', 'Cà phê')
    ], string='Loại nông sản', required=True)
    revenue = fields.Float(string='Doanh thu', required=True)
class MonthlyRevenueSummary(models.Model):
    _name = 'monthly.revenue.summary'
    _description = 'Monthly Revenue Summary'