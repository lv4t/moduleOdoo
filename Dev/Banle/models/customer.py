from odoo import models, fields, api

class Customer(models.Model):
    _name = 'retail.customer'
    _description = 'Customer Management'

    name = fields.Char(string='Customer Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    address = fields.Char(string='Address')
    points = fields.Integer(string='Points', default=0)

    @api.model
    def add_points(self, customer_id, points):
        customer = self.browse(customer_id)
        if customer:
            customer.points += points
            return customer.points
        return 0

    @api.model
    def remove_points(self, customer_id, points):
        customer = self.browse(customer_id)
        if customer and customer.points >= points:
            customer.points -= points
            return customer.points
        return 0




