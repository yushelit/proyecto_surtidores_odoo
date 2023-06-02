# -*- coding: utf-8 -*-
# from odoo import http


# class Surtidores(http.Controller):
#     @http.route('/surtidores/surtidores', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/surtidores/surtidores/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('surtidores.listing', {
#             'root': '/surtidores/surtidores',
#             'objects': http.request.env['surtidores.surtidores'].search([]),
#         })

#     @http.route('/surtidores/surtidores/objects/<model("surtidores.surtidores"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('surtidores.object', {
#             'object': obj
#         })
