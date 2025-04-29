# 1. Imports
from odoo import models

# 2. Classe avec _name, _description, _order
class EstateProperty(models.Model):
    _inherit = "estate.property"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)

    # 3.2. dates / datetime

    # 3.3. relations

    # 3.4. calculés

    # 3.5. techniques

    # 4. Contraintes SQL

    # 5. Méthodes
    # 5.1. calculs (@api.depends)

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)
    def action_property_sold(self):
        print("✅ COUCOUCOUCOUCOUCOU !!!!! action_property_sold appelée depuis estate_account")
        return super().action_property_sold()

    # 5.4. @onchange
