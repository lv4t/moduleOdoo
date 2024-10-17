{
    'name': 'Retail Management',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module for managing retail operations',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu_views.xml',
        'views/warehouse_views.xml',
        'views/sale_views.xml',
        'views/customer_views.xml',
        'views/employee_views.xml',
        'views/branch_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
