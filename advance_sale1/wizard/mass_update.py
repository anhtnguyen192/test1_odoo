from odoo import models, fields, api

class MassUpdate(models.TransientModel):
    _name = 'mass.update'
    discount_code = fields.Text()

    def mass_update(self):
        active_ids = self._context.get('active_ids', []) or []
        for record in self.env['res.partner'].browse(active_ids):
            record.customer_discount_code = self.discount_code