from odoo import models, fields, api


class Warehouse(models.Model):
    _name = 'retail.warehouse'
    _description = 'Warehouse'

    product_name = fields.Char(string='Mã sản phẩm', required=True)
    name = fields.Selection(
        [('Kho BP', 'Kho BP'), ('Kho Q9', 'Kho Q9'), ('Kho TĐ', 'Kho TĐ')],
        string='Tên kho', required=True
    )
    product_type = fields.Selection(
        [('pepper', 'Tiêu'), ('cashew', 'Điều'), ('coffee', 'Cà phê')],
        string='Loại nông sản', required=True
    )
    product_id = fields.Many2one('product.product', string='Sản phẩm', required=True)
    product_subtype = fields.Selection(
        selection=[],
        string='Phân loại sản phẩm'
    )
    date = fields.Date(string='Ngày nhập kho', required = True)
    purchase_price = fields.Float(string='Giá nhập (VNĐ/Kg)', required=True)
    sale_price = fields.Float(string='Giá bán (VNĐ/Kg)', required=True)
    quantity = fields.Float(string='Số lượng sản phẩm (kg)', required=True)

    @api.onchange('product_type')
    def _onchange_product_type(self):
        subtype_selection = []
        if self.product_type == 'pepper':
            subtype_selection = [('green_pepper', 'Tiêu xanh'), ('black_pepper', 'Tiêu đen')]
        elif self.product_type == 'cashew':
            subtype_selection = [('processed_cashew', 'Điều chế biến'), ('unprocessed_cashew', 'Điều chưa chế biến')]
        elif self.product_type == 'coffee':
            subtype_selection = [('robusta', 'Robusta'), ('arabica', 'Arabica'), ('moka', 'Moka')]

        self.product_subtype = False  # Clear the current value of product_subtype
        self._fields['product_subtype'].selection = subtype_selection

    @api.model
    def fields_get(self, allfields=None, attributes=None):
        res = super(Warehouse, self).fields_get(allfields, attributes)
        if 'product_subtype' in res:
            res['product_subtype']['selection'] = [
                ('green_pepper', 'Tiêu xanh'),
                ('black_pepper', 'Tiêu đen'),
                ('processed_cashew', 'Điều chế biến'),
                ('unprocessed_cashew', 'Điều chưa chế biến'),
                ('robusta', 'Robusta'),
                ('arabica', 'Arabica'),
                ('moka', 'Moka'),
            ]
        return res
