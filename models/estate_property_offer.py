from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta
from odoo.exceptions import UserError

class PropertyOffer(models.Model):
    _name = "estate_property_offer"
    _description = "A property offer is an amount a potential buyer offers to the seller. The offer can be lower or higher than the expected price."

    price = fields.Float()
    status = fields.Selection([
        ("0", "New"),
        ("1", "Accepted"),
        ("2", "Refused")],
        copy=False)
    
    partner_id = fields.Many2one("res.partner", string="Buyer")
    property_id = fields.Many2one("estate_property", string="Property")

    create_date = fields.Datetime(default=lambda self: fields.Datetime.now())
    validity = fields.Integer(default="7")
    date_deadline = fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    _sql_constraints = [
        ('check_offer_price', 'CHECK(price >= 0)', 'An offer price must be strictly positive'),
    ]

    @api.depends("validity", "create_date")
    def _compute_date_deadline(self):
        for record in self:
            record.date_deadline = record.create_date + relativedelta.relativedelta(days=record.validity)
    @api.depends("date_deadline", "create_date")
    def _inverse_date_deadline(self):
        for record in self:
            delta = record.date_deadline - record.create_date.date()
            record.validity = delta.days
    
    def action_offer_accept(self):
        for record in self:
            property = record.property_id
            if(property.status == "3"):
                raise UserError("You can't accept a other offer.")
            
            record.status = "1"
            property.selling_price = record.price
            property.buyer_id = record.partner_id
            property.status = "2"

            offers = property.offer_ids.filtered(lambda o: o.id != record.id)
            for other in offers:
                other.status = "2"
        return True
    
    def action_offer_refuse(self):
        for record in self:
            record.status = "2"
        return True