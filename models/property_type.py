# 1. Imports
from odoo import fields, models, api

# 2. Classe avec _name, _description, _order
class PropertyType(models.Model):
    _name = "estate.property.type"
    _description = "A property type is, for example, a house or an apartment."
    _order = "sequence, name asc"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    id = fields.Integer(required=True, default=lambda self: self.default_name(), index=True)
    name = fields.Char(required=True)

    # 3.2. dates / datetime

    # 3.3. relations
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Offers")
    
    # 3.4. calculés
    offer_count = fields.Integer(compute="_compute_offer_count")

    # 3.5. techniques
    sequence = fields.Integer()

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            record.offer_count = len(record.offer_ids)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)

    # 5.4. @onchange