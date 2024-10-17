{
    'name': 'Xuat khau',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Quản lý xuất khẩu nông sản',
    'description': 'Module để quản lý kho, đơn hàng, khách hàng và nhân viên cho xuất khẩu nông sản.',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/warehouse_views.xml',
        'views/export_order_views.xml',
        'views/customer_views.xml',
        'views/employee_views.xml',
        'views/attendance_views.xml',
        'views/finance_views.xml',
        'views/monthly_financial_report_views.xml',
        'views/test_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,


}