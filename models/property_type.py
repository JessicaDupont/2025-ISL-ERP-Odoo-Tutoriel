# 1. Imports
from odoo import fields, models

# 2. Classe avec _name, _description, _order
class PropertyType(models.Model):
    _name = "estate_property_type"
    _description = "A property type is, for example, a house or an apartment."
    _order = "name asc"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    id = fields.Integer(required=True, default=lambda self: self.default_name(), index=True)
    name = fields.Char(required=True)

    # 3.2. dates / datetime

    # 3.3. relations
    property_ids = fields.One2many("estate_property", "property_type_id", string="Properties")

    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange