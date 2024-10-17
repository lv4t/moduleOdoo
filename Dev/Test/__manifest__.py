{
    'name': 'Quản lý chung',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Manage employee information, retail and export revenues, and budgets.',
    'description': """
        This module allows you to manage employee information, track retail and export revenues, and calculate budgets.
    """,
    'author': 'Your Name',
    'website': 'https://yourwebsite.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views.xml',
        'views/retail_revenue_views.xml',
        'views/export_revenue_views.xml',
        'views/budget_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
