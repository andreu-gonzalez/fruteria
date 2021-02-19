from odoo import models, fields, api


class detfac_model(models.Model):
    _name = 'fruteria.detfac_model'
    _description = 'fruteria.detfac_model'

    
    facturas_id = fields.Many2one("fruteria.fac_model", "Factura")
    productos_id = fields.Many2one("fruteria.producto_model", "Productos")
    cantidad = fields.Integer(string="Cantidad", default=1, required=True)

