from odoo import models, fields, api
from odoo.exceptions import ValidationError

class proveedores_model(models.Model):
    _name = 'fruteria.proveedores_model'   
    _description = 'fruteria.proveedores_model'
    _sql_constraints = [("sql_cons_check_id_proveedores_proveedores_model","UNIQUE(id_proveedores)","Error en cliente. El dni id_proveedores proveedores ya existe!"),]

    id_proveedores = fields.Char(string="Id_proveedores",size=9,help="Id de los productos")
    name = fields.Char(string="Nombre", size=20, help="nombre del producto")
    descripcion = fields.Text(string="Descripcion",help="Descripcion del producto")
    Direccion = fields.Char(string="Direccion de los proveedores", help="Descripcion de los proveedores")
    email = fields.Char(string="Direccion de email", help="el email de proveedores",size=100)
    proveedores = fields.Many2many("fruteria.producto_model","produc",string="Producto")

    @api.constrains("email")
    def _comprobarEmail(self):
        if "@" and "." not in self.email:
            raise ValidationError("El email no es correcto. Debe contener al menos @ y .")    