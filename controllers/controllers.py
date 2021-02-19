# -*- coding: utf-8 -*-
# from odoo import http


# class Fruteria(http.Controller):
#     @http.route('/fruteria/fruteria/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/fruteria/fruteria/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('fruteria.listing', {
#             'root': '/fruteria/fruteria',
#             'objects': http.request.env['fruteria.fruteria'].search([]),
#         })

#     @http.route('/fruteria/fruteria/objects/<model("fruteria.fruteria"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('fruteria.object', {
#             'object': obj
#         })
