from odoo import api, fields, models, tools, _


class UpdateCodeWizard(models.TransientModel):
    _name = 'update.warranty.wizard'

    date_from = fields.Date('Start Date')
    date_to = fields.Date('End Date')

    def multi_update(self):
        ids = self.env.context['active_ids']  # selected record ids
        res_partner = self.env['product.template'].browse(ids)
        new_data = {}

        if self.date_from:
            new_data['date_from'] = self.date_from
        if self.date_to:
            new_data['date_to'] = self.date_to

        res_partner.write(new_data)
