from odoo import models, fields


class PosConfig(models.Model):
    _inherit = 'pos.config'
    iface_price_label = fields.Boolean(
        'Show price label button',
        help="Print price labels with this POS"
    )
