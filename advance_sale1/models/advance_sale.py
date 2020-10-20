# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'
    customer_discount_code = fields.Text()



class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'
    discount_code = fields.Text('Discount Code', related='partner_id.customer_discount_code')
    total_discount = fields.Monetary()

    @api.onchange('amount_untaxed', 'discount_code')
    def _calculate_total_discount(self):
        if self.discount_code and "VIP_" in self.discount_code:
            discount_rate = int(str(self.discount_code).replace('VIP_', ''))
            if discount_rate and self.amount_untaxed:
                self.total_discount = self.amount_untaxed * discount_rate / 100






