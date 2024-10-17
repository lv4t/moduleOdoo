from odoo import models, fields

class ExportRevenue(models.Model):
    _name = 'my_module.export_revenue'
    _description = 'Monthly Export Revenue'

    month = fields.Date(string='Tháng', required=True)
    revenue = fields.Float(string='Doanh thu xuất khẩu (VNĐ)', required=True)
