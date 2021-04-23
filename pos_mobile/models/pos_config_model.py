##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    auto_mobile = fields.Boolean(
        "Auto Mobile View",
        help="Switch to Mobile view automatically depending on device",
        default=True,
    )
