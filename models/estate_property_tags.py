# 1. Imports
from odoo import fields, models

# 2. Classe avec _name, _description, _order
class PropertyTags(models.Model):
    _name = "estate_property_tags"
    _description = "A property tag is, for example, a property which is “cozy” or “renovated”."
    _order = "name asc"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    id = fields.Integer(required=True, default=lambda self: self.default_name(), index=True)
    name = fields.Char(required=True)

    # 3.2. dates / datetime

    # 3.3. relations

    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange

