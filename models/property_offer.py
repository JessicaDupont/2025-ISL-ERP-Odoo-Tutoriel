# 1. Imports
from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta
from odoo.exceptions import UserError

# 2. Classe avec _name, _description, _order
class PropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "A property offer is an amount a potential buyer offers to the seller. The offer can be lower or higher than the expected price."
    _order = "price desc"

    # 3. Champs
    # 3.1. simples (Char, Float, Integer, Boolean, Text, etc.)
    price = fields.Float()
    validity = fields.Integer(default="7")

    # 3.2. dates / datetime
    create_date = fields.Datetime(default=lambda self: fields.Datetime.now())

    # 3.3. relations
    partner_id = fields.Many2one("res.partner", string="Buyer")
    property_id = fields.Many2one("estate.property", string="Property")
    property_type_id = fields.Many2one(related="property_id.property_type_id", comodel_name="estate.property.type", store=True)

    # 3.4. calculés
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    open_offer = fields.Boolean(related="property_id.open_offer", store=True)
    
    # 3.5. techniques
    status = fields.Selection([
        ("0", "New"),
        ("1", "Accepted"),
        ("2", "Refused")],
        copy=False)

    # 4. Contraintes SQL
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price >= 0)', 'An offer price must be strictly positive'),
    ]

    # 5. Méthodes
    # 5.1. calculs (@api.depends)
    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta.relativedelta(days=record.validity)
    @api.depends("date_deadline", "create_date")
    def _inverse_date_deadline(self):
        for record in self:
            delta = record.date_deadline - record.create_date.date()
            record.validity = delta.days

    # 5.2. contraintes (@api.constrains)

    # 5.3. métier (actions)
    def action_offer_accept(self):
        for record in self:
            property = record.property_id
            if(property.status == "3"):
                raise UserError("You can't accept a other offer.")
            
            record.status = "1"
            property.selling_price = record.price
            property.buyer_id = record.partner_id
            property.status = "2"
            property.open_offer = False

            offers = property.offer_ids.filtered(lambda o: o.id != record.id)
            for other in offers:
                other.status = "2"
        return True
    
    def action_offer_refuse(self):
        for record in self:
            record.status = "2"
        return True

    # 5.4. @onchange
    