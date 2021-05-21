##############################################################################
#
#    Copyright (C) 2021 Ganar Ganar (https://ganargan.ar)
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
    "name": """Point Of Sale Mobile Screen Support""",
    "summary": """Mobile Screen Support for POS""",
    "license": "AGPL-3",
    "version": "13.0.0.0.0",
    "author": "Ganar Ganar",
    "support": "soporte@ganargan.ar",
    "category": "Point of sale",
    "depends": [
        "point_of_sale",
    ],
    "data": [
        "views/pos_mobile_screen_template.xml",
        "views/pos_mobile_screen_assets.xml",
    ],
    "website": "https://github.com/ganarganar/pos",
    "installable": True
}
