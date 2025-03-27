from odoo import fields, models
from datetime import datetime
from dateutil import relativedelta

class Property(models.Model):
    _name = "estate_property" #nom donné à la table en DB
    _description = "to store the information related to the properties"

    id = fields.Integer(
        required=True, 
        default=lambda self: self.default_name())
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

    