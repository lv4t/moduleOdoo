{
    'name': 'Banle',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Module for managing retail operations',
    'depends': ['base','sale', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/warehouse_views.xml',
        'views/transaction_views.xml',
        'views/sale_views.xml',
        'views/customer_views.xml',
        'views/employee_views.xml',
        'views/sale_order_line_views.xml',
        'views/retail_transaction_views.xml',
        'views/branch_views.xml',
        'views/menu_views.xml',

    ],
    'installable': True,
    'application': True,
}
