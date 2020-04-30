# -*- coding: utf-8 -*-
{
    'name': "Image in sale order",

    'summary': """
       This module adds images to each quote/order, then they will be displayed in an annex to the odoo report""",

    'description': """
            """,
    'price': 30,
    'currency': 'EUR',
    'author': "Binhex Systems Solutions",
    'website': "https://www.binhex.es/",
    'category': 'Sales',
    'version': '0.1',
    # any module necessary for this one to work correctly
    'depends' : ['product','sale'],
    # 'css':'static/css/knowstyle.css',
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'reports/image_sale_order_report.xml', 
        'view/saleorder.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
}
