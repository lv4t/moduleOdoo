{
    'name': 'Test xuat khau',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý xuất khẩu nông sản',
    'description': 'Module để quản lý kho, đơn hàng, khách hàng và nhân viên cho xuất khẩu nông sản.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/export_customer_views.xml',
        'views/export_order_views.xml',
        'views/hr_views.xml',
        'views/inventory_views.xml',
        'views/financial_views.xml',
        'views/quality_views.xml',
        'views/shipping_views.xml',
        'views/supplier_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,


}