# -*- coding: utf-8 -*-
# from odoo import http


# class AdvanceSale1(http.Controller):
#     @http.route('/advance_sale1/advance_sale1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/advance_sale1/advance_sale1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('advance_sale1.listing', {
#             'root': '/advance_sale1/advance_sale1',
#             'objects': http.request.env['advance_sale1.advance_sale1'].search([]),
#         })

#     @http.route('/advance_sale1/advance_sale1/objects/<model("advance_sale1.advance_sale1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('advance_sale1.object', {
#             'object': obj
#         })
