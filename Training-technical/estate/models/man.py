from odoo import api,fields,models

class Travel(models.Model):
    _name="travel.travel"
    _description = "travel QUBY"

    name=fields.Char(string="Name")
    descreption = fields.Char(string="Descreption")
