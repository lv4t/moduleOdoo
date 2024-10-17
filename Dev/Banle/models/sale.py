from odoo import models, fields, api

class SaleOrder(models.Model):
    _name = 'retail.sale.order'
    _description = 'Sale Order'

    name = fields.Char(string='Đơn hàng', required=True)
    customer_id = fields.Many2one('retail.customer', string='Khách hàng', required=True)
    date_order = fields.Datetime(string='Ngày bán', required=True, default=fields.Datetime.now)
    total_amount = fields.Float(string='Tổng thanh toán', compute='_compute_total_amount', store=True)
    order_line = fields.One2many('retail.sale.order.line', 'order_id', string='Order Lines')
    transaction_id = fields.Many2one('retail.transaction', string='Giao Dịch')

    @api.depends('order_line.price_total')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_total for line in order.order_line)
            # Create or update the related transaction
            transaction = self.env['retail.transaction'].search([('id', '=', order.transaction_id.id)], limit=1)
            if transaction:
                transaction.amount = order.total_amount
            else:
                transaction = self.env['retail.transaction'].create({
                    'name': 'Income from Sale Order %s' % order.name,
                    'date': order.date_order,
                    'amount': order.total_amount,
                    'transaction_type': 'income',
                })
                order.transaction_id = transaction.id

class SaleOrderLine(models.Model):
    _name = 'retail.sale.order.line'
    _description = 'Sale Order Line'

    order_id = fields.Many2one('retail.sale.order', string='Đơn hàng', required=True)
    product_id = fields.Many2one('retail.warehouse', string='Sản phẩm ', required=True)
    quantity = fields.Float(string='KL(kg)', required=True)
    product_name = fields.Many2one('retail.warehouse', string='Mã sản phẩm', store=True, readonly=True)
    price_unit = fields.Float(string='Giá bán ', related='product_id.sale_price', store=True, readonly=True)
    price_total = fields.Float(string='Total Price', compute='_compute_price_total', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit

    @api.model
    def create(self, vals):
        record = super(SaleOrderLine, self).create(vals)
        product = record.product_id
        if product.quantity >= record.quantity:
            product.quantity -= record.quantity
        else:
            raise ValueError('Không đủ hàng không kho: %s' % product.name)
        return record

    def write(self, vals):
        for record in self:
            if 'quantity' in vals:
                product = record.product_id
                new_quantity = vals.get('quantity', 0)
                if new_quantity > record.quantity:  # Increase quantity
                    diff = new_quantity - record.quantity
                    if product.quantity >= diff:
                        product.quantity -= diff
                    else:
                        raise ValueError('Không đủ hàng trong kho: %s' % product.name)
                elif new_quantity < record.quantity:  # Decrease quantity
                    diff = record.quantity - new_quantity
                    product.quantity += diff
            return super(SaleOrderLine, self).write(vals)
