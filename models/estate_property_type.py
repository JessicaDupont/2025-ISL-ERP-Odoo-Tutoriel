from odoo import fields, models

class PropertyType(models.Model):
    _name = "estate_property_type"
    _description = "A property type is, for example, a house or an apartment."

    id = fields.Integer(
        required=True, 
        default=lambda self: self.default_name(), 
        index=True)
    name = fields.Char(
        required=True)
    
    property_ids = fields.One2many(
        "estate_property", 
        "property_type_id", 
        string="Properties")