{
    'name': 'Estate',
    'version': '1.0',
    'author': 'Jessica Dupont',
    'depends': ['base'],  # Dépendance minimale pour fonctionner avec Odoo
    'data': [
        #security
        'security/estate_security.xml',
        'security/ir.model.access.csv',
        #data
        'data/estate_property_type.csv',
        'data/estate_property_tags.csv',
        #demo
        'demo/estate_property.csv',
        'demo/estate_property_offer.csv',
        #wizard
        #views & report
        'views/property_type_views.xml',
        'views/property_tags_views.xml',
        'views/property_views.xml',
        'views/property_offer_views.xml',
        'views/_menus.xml',#last in list
    ],
    'installable' : True,
    'application': True
}
