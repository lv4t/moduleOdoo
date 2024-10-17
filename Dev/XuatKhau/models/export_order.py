from odoo import models, fields, api

class ExportOrder(models.Model):
    _name = 'export.order'
    _description = 'Export Order'

    name = fields.Char(string='Đơn hàng', required=True)
    customer_id = fields.Many2one('export.customer', string='Khách hàng', required=True)
    employee_id = fields.Many2one('export.employee', string='Nhân viên phụ trách', required=True)
    order_date = fields.Datetime(string='Ngày đặt hàng', required=True, default=fields.Datetime.now)
    shipping_method = fields.Selection([
        ('sea', 'Đường biển'),
        ('air', 'Đường hàng không'),
        ('land', 'Đường bộ')
    ], string='Phương thức vận chuyển', required=True)
    state = fields.Selection([
        ('draft', 'Chưa vận chuyển'),
        ('shipped', 'Đã vận chuyển')
    ], string='Tình trạng đơn hàng', default='draft')
    order_line = fields.One2many('export.order.line', 'order_id', string='Order Lines')
    total_amount = fields.Float(string='Tổng thanh toán', compute='_compute_total_amount', store=True)

    @api.depends('order_line.price_total')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = sum(line.price_total for line in order.order_line)

class ExportOrderLine(models.Model):
    _name = 'export.order.line'
    _description = 'Export Order Line'

    order_id = fields.Many2one('export.order', string='Order Reference', required=True)
    product_id = fields.Many2one('export.warehouse', string='Product', required=True)
    quantity = fields.Float(string='Số lượng (kg)', required=True)
    price_unit = fields.Float(string='Giá bán', related='product_id.sale_price', store=True, readonly=True)
    price_total = fields.Float(string='Total Price', compute='_compute_price_total', store=True)

    @api.depends('quantity', 'price_unit')
    def _compute_price_total(self):
        for line in self:
            line.price_total = line.quantity * line.price_unit

    @api.model
    def create(self, vals):
        record = super(ExportOrderLine, self).create(vals)
        product = record.product_id
        if product.quantity >= record.quantity:
            product.quantity -= record.quantity
        else:
            raise ValueError('Không đủ hàng trong kho: %s' % product.name)
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
            return super(ExportOrderLine, self).write(vals)
