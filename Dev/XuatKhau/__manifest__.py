{
    'name': 'Export Agriculture',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Module for managing agricultural exports',
    'description': """
        This module manages agricultural products, export orders, customers, and employees.
    """,
    'author': 'Your Name',
    'website': 'http://www.yourcompany.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/warehouse_views.xml',
        'views/export_order_views.xml',
        'views/customer_views.xml',
        'views/employee_views.xml',
        'views/batch_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
