from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta
from odoo.exceptions import UserError

class Property(models.Model):
    _name = "estate_property" #nom donné à la table en DB
    _description = "to store the information related to the properties"

    id = fields.Integer(
        required=True, 
        default=lambda self: self.default_name(), 
        index=True)
    name = fields.Char(
        required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False, 
        default=datetime.today()+relativedelta.relativedelta(months=3))
    expected_price = fields.Float(
        required=True)
    selling_price = fields.Float(
        copy=False, 
        readonly=True)
    
    bedrooms = fields.Integer(
        default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection([
        ("N","North"), 
        ("S","South"), 
        ("E","East"), 
        ("W","West")])
    
    active = fields.Boolean(
        default=True)
    status = fields.Selection([
        ("0", "New"), 
        ("1", "Received"), 
        ("2", "Accepted"), 
        ("3", "Sold"), 
        ("4", "Cancelled")], 
        string ="status", 
        default="0", 
        required=True, 
        copy=False)
    
    property_type_id = fields.Many2one("estate_property_type", string="Type")
    buyer_id = fields.Many2one("res.partner", string="Buyer", copy=False)
    seller_id = fields.Many2one("res.partner", string="Seller", copy=False)
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)
    
    property_tags_ids = fields.Many2many("estate_property_tags", string="Tags")
    offer_ids = fields.One2many("estate_property_offer", "property_id", string="Offers")

    _sql_constraints = [
        ('check_expected_price', 'CHECK(expected_price >= 0)', 'A property expected price must be strictly positive'),
        ('check_selling_price', 'CHECK(selling_price >= 0)', 'A property selling price must be positive'),
        ('unique_tags', 'unique(property_tags_ids)', 'A property tag name must be unique'),
        ('unique_type', 'unique(property_type_id)', 'A property type name must be unique'),
    ]

    total_area = fields.Integer(compute="_compute_total_area")
    @api.depends("living_area", "garden_area")
    def _compute_total_area(self):
        for record in self:
            record.total_area = record.living_area + record.garden_area

    best_price = fields.Float(compute="_compute_best_price")
    @api.depends("offer_ids.price")
    def _compute_best_price(self):
        for record in self:
            prices = record.offer_ids.mapped('price')
            record.best_price = max(prices) if prices else 0.0
    
    @api.onchange("garden")
    def _onchange_garden(self):
        if(self.garden == True):
            self.garden_area = 10
            self.garden_orientation = "N"
        else:
            self.garden_area = 0
            self.garden_orientation = ""
    
    def action_property_sold(self):
        for record in self:
            if(record.status == "4"):
                raise UserError("Solded properties cannot be cancel.")
            record.status = "3"
        return True
    
    def action_property_cancel(self):
        for record in self:
            if(record.status == "3"):
                raise UserError("Canceled properties cannot be sold.")
            record.status = "4"
        return True
    