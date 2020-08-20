# -*- coding: utf-8 -*-
{
    'name': "Image in sale order",

    'summary': """
       This module adds images to each quote/order, then they will be displayed in an annex to the odoo report""",

    'description': """
     This module adds images to each quote/order, then they will be displayed in an annex to the odoo report
            """,
    'price': 30,
    'currency': 'EUR',
    'author': "Binhex Systems Solutions",
    'website': "https://www.binhex.es/",
    'category': 'Sales',
    'license': 'AGPL-3',
    'version': '1.0.0',
    'depends' : ['product','sale'],
    'images': ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'reports/image_sale_order_report.xml', 
        'view/saleorder.xml'
    ],
    
    'installable': True,
    'application': True,
}
