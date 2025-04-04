from odoo import fields, models

class Property(models.Model):
    _name = "estate_property_offer"
    _description = "A property offer is an amount a potential buyer offers to the seller. The offer can be lower or higher than the expected price."

    price = fields.Float()
    status = fields.Selection([
        ("0", "New"),
        ("1", "Accepted"),
        ("2", "Refused")],
        copy=False)
    partner_id = fields.Many2one("res.partner", 
        string="Buyer")
    property_id = fields.Many2one("estate_property", 
        string="Property")