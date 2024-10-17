from odoo import models, fields, api

class WarehouseSummary(models.Model):
    _name = 'warehouse.summary'
    _description = 'Warehouse Summary'

    name = fields.Char(string='Name', default='Warehouse Summary')
    total_pepper = fields.Integer(string='Total Pepper', compute='_compute_totals')
    total_cashew = fields.Integer(string='Total Cashew', compute='_compute_totals')
    total_coffee = fields.Integer(string='Total Coffee', compute='_compute_totals')
    total_stock_quantity = fields.Integer(string='Total Stock Quantity', compute='_compute_totals')
    total_stock_weight = fields.Float(string='Total Stock Weight', compute='_compute_totals')

    @api.depends('total_pepper', 'total_cashew', 'total_coffee')
    def _compute_totals(self):
        pepper_model = self.env['warehouse.pepper']
        cashew_model = self.env['warehouse.cashew']
        coffee_model = self.env['warehouse.coffee']

        total_pepper = sum(pepper_model.search([]).mapped('stock_quantity'))
        total_cashew = sum(cashew_model.search([]).mapped('stock_quantity'))
        total_coffee_quantity = sum(coffee_model.search([]).mapped('stock_quantity'))
        total_coffee_weight = sum(coffee_model.search([]).mapped('quantity' * coffee_model.search([]).mapped('weight_unit')))

        for record in self:
            record.total_pepper = total_pepper
            record.total_cashew = total_cashew
            record.total_coffee = total_coffee_quantity
            record.total_stock_quantity = total_pepper + total_cashew + total_coffee_quantity
            record.total_stock_weight = total_coffee_weight
