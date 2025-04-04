{
    'name': 'Estate',
    'version': '1.0',
    'summary': 'Module de gestion immobilière',
    'description': 'Un module Odoo pour gérer les biens immobiliers.',
    'author': 'Jessica Dupont',
    'license': 'LGPL-3',
    'category': 'Sales',
    'depends': ['base'],  # Dépendance minimale pour fonctionner avec Odoo
    'data': [
        #security
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        #data
        #wizard
        #views & report
        'views/estate_property_views.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tags_views.xml',
        'views/estate_property_offer_views.xml',
        'views/estate_menus.xml',#last in list
    ],
    'application': True
}
