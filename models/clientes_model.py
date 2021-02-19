from odoo import models, fields, api
from odoo.exceptions import ValidationError

class clientes_model(models.Model):
    _name = 'fruteria.clientes_model'   
    _description = 'fruteria.clientes_model'
    _sql_constraints = [("sql_cons_check_dni_clientes_model","UNIQUE(dni)","Error en cliente. El dni del cliente ya existe!"),
                     ("sql_cons_check_id_clientes_model","UNIQUE(id_clientes)","Error en cliente. El id  del cliente ya existe!"),]

    id_clientes = fields.Char(string="Id_clientes",size=9,help="Id de los clientes",required=True,index=True)
    name = fields.Char(string="Nombre", size=20, help="nombre del clientes",required=True)
    apellidos = fields.Char(string="Apellidos", size=20, help="apellidos del clientes",required=True)
    dni = fields.Char(string="DNI",size=9,help="DNI",required=True)
    descripcion = fields.Text(string="Descripcion",help="Descripcion del clientes",required=True)
    Direccion = fields.Char(string="Direccion de los clientes", help="Descripcion de los clientes")
    email = fields.Char(string="Direccion de email", help="el email de clientes",size=100,required=True)
    tlf = fields.Char(string="telefono",help="telefono de client",size=9,required=True)
    facturas = fields.One2many("fruteria.fac_model","cliente", string="Facturas")
    tra= fields.Many2one("fruteria.trabajadores_model", string="Trabajadores")
    foto=fields.Binary(string="foto",help="fotografia cliente")

    @api.constrains("tlf")
    def checkTelf(self):
          if len(self.tlf) != 9:
               raise ValidationError("Error en teléfono. Debe contener 9 dígitos")

    @api.constrains('dni')
    def validate_dni(self):
        if not self.check_DNI(self.dni):
            raise ValidationError("Error en DNI!!!!")
    
    def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X':'0', 'Y':'1', 'Z':'2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni)%23] == dig_control
        return False
    @api.constrains("email")
    def _comprobarEmail(self):
        if "@" and "." not in self.email:
            raise ValidationError("El email no es correcto. Debe contener al menos @ y .")       