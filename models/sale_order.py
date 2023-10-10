from odoo import fields, models, api
from datetime import date


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    so_warranty_discount = fields.Monetary(string='Warranty Discount', compute='_compute_waranty')

    @api.depends('order_line')
    def _compute_waranty(self):
        for rec in self.order_line:
            print(rec.product_id.remaining_time)
            start = rec.product_id.date_from
            end = rec.product_id.date_to
            if start and end and start <= date.today() <= end:
                rec.product_warranty_discount = 0
            else:
                rec.product_warranty_discount = rec.price_unit * 10 / 100

        for rec in self:
            rec.so_warranty_discount = 0
            for i in rec.order_line:
                rec.so_warranty_discount += i.product_warranty_discount



class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_warranty_discount = fields.Float(string="Warranty Discount")
    remaining_time = fields.Char(string='Remaining', related='product_id.remaining_time')
