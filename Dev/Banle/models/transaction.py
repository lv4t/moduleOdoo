from odoo import models, fields, api
from datetime import date
from calendar import monthrange

class RetailTransaction(models.Model):
    _name = 'retail.transaction'
    _description = 'Transaction'

    name = fields.Char(string='Mô tả', required=True)
    date = fields.Date(string='Ngày', default=date.today(), required=True)
    amount = fields.Float(string='Số tiền', required=True)
    transaction_type = fields.Selection([
        ('income', 'Income'),
        ('expense', 'Expense')
    ], string='Loại Giao Dịch', required=True)
    employee_id = fields.Many2one('retail.employee', string='Nhân viên')
    note = fields.Text(string='Ghi chú')
    total_income_from_sales = fields.Float(string='Tổng Thu Nhập từ Bán Hàng', compute='_compute_total_income_from_sales', store=True)
    cost = fields.Float(string='Chi Phí', required=True)

    @api.depends('date')
    def _compute_total_income_from_sales(self):
        for record in self:
            sales = self.env['retail.sale.order'].search([('date_order', '=', record.date)])
            total_income = sum(sale.total_amount for sale in sales)
            record.total_income_from_sales = total_income
