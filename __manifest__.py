{
    'name': 'Estate',
    'version': '1.0',
    'author': 'Jessica Dupont',
    'depends': ['base'],  # Dépendance minimale pour fonctionner avec Odoo
    'data': [
        #security
        'security/security.xml',
        'security/ir.model.access.csv',
        #data
        'data/estate.property.type.csv',
        'data/estate.property.tags.csv',
        #demo
        'demo/estate.property.csv',
        'demo/estate.property.offer.csv',
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
