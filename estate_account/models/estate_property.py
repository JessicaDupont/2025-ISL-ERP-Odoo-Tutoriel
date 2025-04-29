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
        result = super().action_property_sold()

        for property in self:
            if not property.buyer_id:
                print(f"⚠️impossible de facturer sans client")
                continue  
            
            # Recherche du journal de type vente
            journal = self.env['account.journal'].search([('type', '=', 'sale')], limit=1)
            if not journal:
                raise ValueError("Aucun journal de vente disponible")

            # Création d'une facture vide
            invoice = self.env['account.move'].create({
                'partner_id': property.buyer_id.id,
                'move_type': 'out_invoice',  # Facture client
                'journal_id': journal.id,
            })

            print(f"✅ Facture vide créée pour le bien {property.name} (ID: {invoice.id})")

        return result

    # 5.4. @onchange
