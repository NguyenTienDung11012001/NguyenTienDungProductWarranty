from odoo import fields, models, api, _
from odoo.exceptions import ValidationError
from datetime import date

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    product_warranty = fields.Char(string='Warranty Code', compute='_compute_warranty_code')
    date_from = fields.Date(string='From', required=True)
    date_to = fields.Date(string='To', required=True)
    remaining_time = fields.Char(string='Remaining', compute='_compute_remaining', store=True)

    @api.constrains('date_from', 'date_to')
    def _check_date_from(self):
        for rec in self:
            if rec.date_from > rec.date_to:
                raise ValidationError(_('Date from cannot greater than date to'))

    @api.depends('date_from', 'date_to')
    def _compute_warranty_code(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                start = rec.date_from.strftime("%d%m%y")
                end = rec.date_to.strftime("%d%m%y")
                war = f"PWR/{str(start)}/{str(end)}"
                rec.product_warranty = war
            else:
                rec.product_warranty = ''

    @api.depends('date_to')
    def _compute_remaining(self):
        for rec in self:
            if rec.date_to and rec.date_to > date.today():
                days = rec.date_to - date.today()
                rec.remaining_time = f'{days.days} days'
            else:
                rec.remaining_time = False

# group = env.ref('sale.send_invoice_cron')
# group.users = [(6, 0, [2, 3, 4])]