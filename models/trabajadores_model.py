from odoo import models, fields, api
from odoo.exceptions import ValidationError

class trabajadores_model(models.Model):
    _name = 'fruteria.trabajadores_model'   
    _description = 'fruteria.trabajadores_model'
    _sql_constraints = [("sql_cons_check_id_trabajadores_trabajadores_model","UNIQUE(id_trabajadores)","Error en cliente. El dni id_trabajadores trabajadores ya existe!"),]

    id_trabajadores = fields.Char(string="Id_trabajadores",size=9,help="Id de los trabajadores")
    name = fields.Char(string="Nombre", size=20, help="nombre del trabajadores")
    apellidos = fields.Char(string="Apellidos", size=100, help="nombre del trabajadores")
    dni = fields.Char(string="DNI",size=9,help="DNI")
    descripcion = fields.Text(string="Descripcion",help="Descripcion del producto")
    Direccion = fields.Char(string="Direccion de los proveedores", help="Descripcion de los proveedores")
    email = fields.Char(string="Direccion de email", help="el email de proveedores",size=100)
    tlf = fields.Char(string="telefono",help="telefono de trabajadores")
    sueldo = fields.Float(string="Sueldo", help="sueldo de los trabajadores")
    cargo = fields.Char(string="Cargo",help="el cargo que ocupa en la empresa",size=10)
   
    clientes = fields.One2many("fruteria.clientes_model","tra")

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