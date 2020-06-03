from odoo import fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    add_phone_partner_phone = fields.Char(string='Additional phone')
    add_phone_partner_company = fields.Char(string='Company')
