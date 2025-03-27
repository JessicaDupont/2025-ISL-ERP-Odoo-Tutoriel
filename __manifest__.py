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
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'application': True
}
