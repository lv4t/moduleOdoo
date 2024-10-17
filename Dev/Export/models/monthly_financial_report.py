from odoo import models, fields, api
from calendar import monthrange

class MonthlyFinancialReport(models.Model):
    _name = 'monthly.financial.report'
    _description = 'Monthly Financial Report'

    month = fields.Selection([(str(num), str(num)) for num in range(1, 13)], string='Tháng', required=True)
    year = fields.Char(string='Năm', required=True)
    total_income_usd = fields.Float(string='Tổng thu (USD)', compute='_compute_total_income_usd', store=True)
    total_cost_usd = fields.Float(string='Tổng chi phí (USD)', compute='_compute_total_cost_usd', store=True)
    total_profit_usd = fields.Float(string='Tổng lợi nhuận (USD)', compute='_compute_total_profit_usd', store=True)
    total_income_vnd = fields.Float(string='Tổng thu (VND)', compute='_compute_total_income_vnd', store=True)
    total_cost_vnd = fields.Float(string='Tổng chi phí (VND)', compute='_compute_total_cost_vnd', store=True)
    total_profit_vnd = fields.Float(string='Tổng lợi nhuận (VND)', compute='_compute_total_profit_vnd', store=True)
    exchange_rate = fields.Float(string='Tỷ giá (USD/VND)', required=True, default=25295.00)  # Ví dụ tỷ giá USD/VND là 23000

    @api.depends('month', 'year')
    def _compute_total_income_usd(self):
        for record in self:
            if record.month and record.year:
                start_date = f'{record.year}-{record.month}-01'
                last_day = monthrange(int(record.year), int(record.month))[1]
                end_date = f'{record.year}-{record.month}-{last_day}'
                financial_records = self.env['export.financial'].search([
                    ('date', '>=', start_date),
                    ('date', '<=', end_date)
                ])
                record.total_income_usd = sum(fin.total_amount for fin in financial_records)

    @api.depends('month', 'year')
    def _compute_total_cost_usd(self):
        for record in self:
            if record.month and record.year:
                start_date = f'{record.year}-{record.month}-01'
                last_day = monthrange(int(record.year), int(record.month))[1]
                end_date = f'{record.year}-{record.month}-{last_day}'
                financial_records = self.env['export.financial'].search([
                    ('date', '>=', start_date),
                    ('date', '<=', end_date)
                ])
                record.total_cost_usd = sum(fin.cost_shipping + fin.cost_product + fin.cost_other for fin in financial_records)

    @api.depends('total_income_usd', 'total_cost_usd')
    def _compute_total_profit_usd(self):
        for record in self:
            record.total_profit_usd = record.total_income_usd - record.total_cost_usd

    @api.depends('total_income_usd', 'exchange_rate')
    def _compute_total_income_vnd(self):
        for record in self:
            record.total_income_vnd = record.total_income_usd * record.exchange_rate

    @api.depends('total_cost_usd', 'exchange_rate')
    def _compute_total_cost_vnd(self):
        for record in self:
            record.total_cost_vnd = record.total_cost_usd * record.exchange_rate

    @api.depends('total_profit_usd', 'exchange_rate')
    def _compute_total_profit_vnd(self):
        for record in self:
            record.total_profit_vnd = record.total_profit_usd * record.exchange_rate
