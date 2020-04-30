# -*- coding: utf-8 -*-

from odoo import fields, models, api, exceptions, _
import logging, re
#Get the logger
_logger = logging.getLogger(__name__)



class imagen_order(models.Model):
    _name = 'sale.imagen'
    image = fields.Binary("Image")
    name = fields.Char(
        string='Title image')
    imagen_id= fields.Many2one('sale.order','imagen_order', readonly=False)

class saleorderimagen(models.Model):

    _inherit = 'sale.order'
    imagen_order = fields.One2many('sale.imagen','imagen_id', string='Image', readonly=False)