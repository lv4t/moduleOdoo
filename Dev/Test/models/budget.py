from odoo import models, fields, api

class Budget(models.Model):
    _name = 'my_module.budget'
    _description = 'Budget'

    month = fields.Date(string='Tháng', required=True)
    retail_revenue_id = fields.Many2one('my_module.retail_revenue', string='Doanh thu bán lẻ')
    export_revenue_id = fields.Many2one('my_module.export_revenue', string='Doanh thu xuất khẩu')
    taxes = fields.Float(string='Thuế (VNĐ)')
    employee_salary = fields.Float(string='Lương nhân viên (VNĐ)')
    other_expenses = fields.Float(string='Chi phí khác (VNĐ)')
    total_revenue = fields.Float(string='Doanh thu tổng cộng (VNĐ)', compute='_compute_total_revenue')

    @api.depends('retail_revenue_id', 'export_revenue_id', 'taxes', 'employee_salary', 'other_expenses')
    def _compute_total_revenue(self):
        for record in self:
            retail_revenue = record.retail_revenue_id.revenue if record.retail_revenue_id else 0.0
            export_revenue = record.export_revenue_id.revenue if record.export_revenue_id else 0.0
            record.total_revenue = retail_revenue + export_revenue - record.taxes - record.employee_salary - record.other_expenses
