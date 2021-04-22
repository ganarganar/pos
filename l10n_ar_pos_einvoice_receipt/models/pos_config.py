##############################################################################
# For copyright and license notices, see __manifest__.py file in module root
# directory
##############################################################################

from odoo import api, fields, models, _

class pos_config(models.Model):

    _inherit = "pos.config"

    invoice_by_default = fields.Boolean(
        "Automatic invoicing",
        help="If checked, sales will be invoiced by default",
        default=True
    )
    pdf_invoice_download = fields.Boolean(
        "PDF invoice download",
        help="If checked, a PDF copy of the invoice will be downloaded",
        default=False
    )
    show_cashier_info = fields.Boolean(
        "Show cashier info",
        default=True
    )
    show_contact_info = fields.Boolean(
        "Show contact info",
        default=True
    )
    show_customer_vat = fields.Boolean(
        "Show customer VAT",
        default=True
    )
    show_invoice_number = fields.Boolean(
        "Show invoice number",
        default=True
    )