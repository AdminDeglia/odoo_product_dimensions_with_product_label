# -*- coding: utf-8 -*-
from odoo import models, fields

class CustomProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout'

    print_format = fields.Selection(
        selection_add=[('2x7xprice', 'Valenziana 70x100')],
        ondelete={'2x7xprice': 'set default'}
    )
