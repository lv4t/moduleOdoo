{
    'name': 'Warehouse Management',
    'version': '1.0',
    'category': 'Warehouse',
    'summary': 'Module to manage agricultural products in warehouse',
    'depends': ['base'],
    'data': [
        'security/warehouse_security.xml',
        'security/ir.model.access.csv',
        'views/pepper_views.xml',
        'views/cashew_views.xml',
        'views/coffee_views.xml',
        'views/warehouse_summary_views.xml',
        'views/warehouse_menu.xml',
    ],
    'installable': True,
    'application': True,
}
