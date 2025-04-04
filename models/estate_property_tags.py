from odoo import fields, models

class PropertyTags(models.Model):
    _name = "estate_property_tags"
    _description = "A property tag is, for example, a property which is “cozy” or “renovated”."

    id = fields.Integer(
        required=True, 
        default=lambda self: self.default_name(), 
        index=True)
    name = fields.Char(
        required=True)