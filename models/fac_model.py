from odoo import models, fields, api
from datetime import datetime, date
class fac_model(models.Model):
    _name = 'fruteria.fac_model'
    _description = 'fruteria.fac_model'
 

    name = fields.Char(string="Referencia", required=True)
    fecha = fields.Date(string="Fecha", required=True, default=date.today())
    cliente = fields.Many2one("fruteria.clientes_model", string="Cliente")
    detallef = fields.One2many("fruteria.detfac_model","facturas_id", string="Facturas")
    base = fields.Float(string="Base", store=True,compute="_calc_base")
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)
    total = fields.Float(string="Total", store=True,compute="_calc_iva")
    active = fields.Boolean(readonly=True, default=True)

    @api.depends('detallef')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        resta=0
        for i in self.detallef:
            suma += i.productos_id.precio*i.cantidad
            resta += i.productos_id.stock-i.cantidad
        self.base = suma
        self.detallef.productos_id.stock = resta
    @api.depends('iva', 'base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)
   
              

    def eliminaHistorial(self):
        historialSocios = self.search([("active","=","False")])
        for rec in historialSocios:
            rec.unlink()
    
        