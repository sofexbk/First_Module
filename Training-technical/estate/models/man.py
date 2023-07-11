from odoo import api,fields,models

class Travel(models.Model):
    _name="travel.travel"
    _description = "travel QUBY"

    name=fields.Char(string="Name")
    descreption = fields.Char(string="Descreption")
    date_start=fields.Date(string="Date Start")
    date_end=fields.Date(string="Date End")
