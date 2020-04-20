{
    'name': 'Partner customization',
    'summary': 'Additional phone number for Contact',
    'category': 'Extra Tools',

    'license': 'Other proprietary',
    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'version': '12.0.0.0.1',
    'depends': ['base', 'contacts', ],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'application': False,
    'installable': True,
}
