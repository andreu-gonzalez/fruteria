from odoo import models, fields, api
from odoo.exceptions import ValidationError

class producto_model(models.Model):
    _name = 'fruteria.producto_model'   
    _description = 'fruteria.producto_model'

    id_productos = fields.Char(string="Id_productos",size=9,help="Id de los productos",required=True)
    name = fields.Char(string="Nombre", size=20, help="nombre del producto",required=True)
    descripcion = fields.Text(string="Descripcion",help="Descripcion del producto",required=True)
    procedencia = fields.Selection(string="Procedencia",help="Procedencia del producto",selection=[('valencia','valencia'),('castellon', 'castellon'),('alicante', 'alicante')])
    stock = fields.Integer(string="Cantidad",help="Cantidad de productos",required=True)
    detallef = fields.One2many("fruteria.detfac_model","productos_id","Facturas")   
    produc= fields.Many2many("fruteria.proveedores_model", string="Provedores")
    precio=fields.Float(string="Precio",required=True)

    @api.constrains("precio")
    def checkPrecio(self):
          self.ensure_one()
          if self.precio <= 0:
               raise ValidationError("Precio de producto erróneo!")

    @api.constrains("stock")
    def actualizaSalario(self):
          self.ensure_one()
          if self.stock <= 0:
               raise ValidationError("La cantidad debe contener un valor positivo")  