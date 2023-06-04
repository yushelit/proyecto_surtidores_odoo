# -*- coding: utf-8 -*-
import re
from datetime import datetime

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import logging
import re

_logger = logging.getLogger(__name__)

# Modelo cliente
class cliente(models.Model):
    _name = 'surtidores.cliente'
    _description = 'surtidores.cliente'

    name = fields.Char(string="Nombre", required=True, help="Nombre")
    dni = fields.Char(string="DNI", required=True, help="DNI")
    apellidos = fields.Char(string="Apellidos", help="Apellidos")
    ciudad = fields.Char(string="Ciudad", help="Ciudad")
    edad = fields.Integer()
    foto = fields.Image(string="Foto", help="Añadir foto")
    direccion = fields.Text(string="Direccion", help="Dirección del Cliente", default='C/ ')
    fecha_registro = fields.Date(string='Fecha de registro', compute='_compute_fecha_registro', store=True)

    @api.constrains('dni')
    def _check_dni(self):
        regex = re.compile('^[0-9]{8}[a-z]\Z', re.I)
        for cliente in self:
            if regex.match(cliente.dni):
                _logger.info('DNI correto')
            else:
                raise ValidationError('Formato DNI incorrecto')

    @api.depends('name')
    def _compute_fecha_registro(self):
        for cliente in self:
            cliente.fecha_registro = datetime.now().strftime("%Y-%m-%d")

# Modelo Camion
class camion(models.Model):
    _name = 'surtidores.camion'
    _description = 'surtidores.camion'

    name = fields.Char(string="Nombre", help="Nombre")
    matricula = fields.Char(string="Matricula", required=True, help="Matricula")
    modelo = fields.Char(string="Modelo", help="Modelo")
    foto = fields.Image(string="Foto", help="Añadir foto")

    @api.constrains('matricula')
    def _check_dni(self):
        regex = re.compile('^\d{4}[A-Z]{3}\Z', re.I)
        for cliente in self:
            if regex.match(cliente.dni):
                _logger.info('Matricula correta')
            else:
                raise ValidationError('Formato de Matricula incorrecta')


# Modelo Productos
class producto(models.Model):
    _name = 'surtidores.producto'
    _description = 'surtidores.producto'

    tipo_combustible = fields.Selection([
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('metano', 'Metano'),
        ('queroseno', 'Queroseno'),
        ('tnt', 'TrinitroTolueno'),
        ('nt', 'NitroGlicerina'),
        ('etanol', 'Etanol'),
        ('pentano', 'Pentano'),
        ('butano', 'Butano'), ], string='Tipo de Combustible', required=True,
        default='gasolina')
    precio = fields.Float(string="Precio(€) por litro", help="Valor de un litro de combustrible en euros")

# Modelo Envase
class envase(models.Model):
    _name = 'surtidores.envase'
    _description = 'surtidores.envase'

    identificador = fields.Char(string="id", help="id")
    tipo_combustible = fields.Many2one("surtidores.producto", ondelete="set null", help="Combustible que llevara el envase")
    capacidad = fields.Selection([
        ('20', '20'),
        ('25', '25'),
        ('30', '30'),
        ('35', '35'),
        ('40', '40'),
        ('45', '45'),
        ('50', '50'),
        ('55', '55'),
        ('60', '60'), ], string='Capacidad', required=True,
        default='20')

# Modelo Viaje
class viaje(models.Model):
    _name = 'surtidores.viaje'
    _description = 'surtidores.viaje'

    origen = fields.Char(string="Origen", help="Origen")
    destino = fields.Char(string="Destino", help="Destino")
    cliente = fields.Many2one("surtidores.cliente")
    camion = fields.Many2one("surtidores.camion")
    envases = fields.Many2many("surtidores.envase")
