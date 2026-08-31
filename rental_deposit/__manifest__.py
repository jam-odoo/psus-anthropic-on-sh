{
    'name': "Rental Deposit",
    'summary': "Track security deposits for rental orders",
    'category': 'Sales/Rental',
    'version': '19.0.1.0.0',
    'depends': ['sale_renting'],
    'data': [
        'security/rental_deposit_groups.xml',
        'security/ir.model.access.csv',
        'views/rental_deposit_views.xml',
    ],
    'license': 'LGPL-3',
}
