from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate_property_type"
    _description = "A property type is, for example, a house or an apartment."

    name = fields.Char(
        required=True)