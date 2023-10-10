# -*- coding: utf-8 -*-
{
    'name': "ProductWarranty",

    'summary': """
        Manage product warranty
        """,

    'description': """
        Manage product warranty
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_template_view.xml',
        'views/sale_order_view.xml',
    ],
}
