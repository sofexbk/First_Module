from odoo import api,fields,models

class Continent(models.Model):
    _name="continent.continent"
    _description = "Continent of QUBY"

    continent=fields.Char(string="Continent")
    city= fields.Char(string="City")

