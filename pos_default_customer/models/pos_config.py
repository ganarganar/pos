##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import fields, models


class PosConfigInherit(models.Model):
    _inherit = "pos.config"

    partner_id = fields.Many2one(
        "res.partner",
        string="Default customer"
    )
