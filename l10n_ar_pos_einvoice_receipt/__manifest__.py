##############################################################################
#
#    Copyright (C) 2021  Ganar Ganar  (https://ganargan.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    "name": "Point Of Sale eInvoice Receipt",
    "summary": """Allows to print receipts as electronic invoices.""",
    "license": "AGPL-3",
    "version": "13.0.1.1.0",
    "author": "Ganar Ganar",
    "support": "soporte@ganargan.ar",
    "category": "Point of sale",
    "depends": [
        "point_of_sale",
        "l10n_ar_afipws_fe"
    ],
    "data": [
        "views/l10n_ar_pos_einvoice_receipt_templates.xml",
        "views/pos_config_view.xml"
    ],
    "qweb": [
        "static/src/xml/pos.xml"
    ],
    "website": "https://github.com/ganar-gan-ar/pos",
    "installable": True
}
