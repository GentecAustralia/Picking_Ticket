# -*- coding: utf-8 -*-


{
    'name': 'Picking Ticket 2019-02-15 1219A)',
    'version': '12.0.0.0',
    'category': 'Accounting',
    'summary': 'Picking Ticket with BoM',
    'description': """ Picking Ticket with BoM
""",
    'depends': ['sale','purchase','stock','Au_In12'],
    'data': [
        'report/custom_report.xml',
        'report/custom_stock_picking_report.xml',
        ],
    'demo': [],
    'js': [],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    "images":['static/description/Banner.png'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
