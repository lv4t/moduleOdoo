from odoo import models, fields

class RetailRevenue(models.Model):
    _name = 'my_module.retail_revenue'
    _description = 'Monthly Retail Revenue'

    month = fields.Date(string='Tháng', required=True)
    revenue = fields.Float(string='Doanh thu bán lẻ (VNĐ)', required=True)
