{
    'name': 'Partner customization',
    'summary': 'Additional fields in res.partner',
    'category': 'Extra Tools',

    'license': 'Other proprietary',
    'author': 'Kitworks Systems',
    'website': 'https://kitworks.systems/',

    'version': '12.0.0.0.2',
    'depends': ['base', 'contacts', ],

    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_view.xml',
    ],
    'application': False,
    'installable': True,
}
