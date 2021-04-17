{
    "name": """POS Mobile UI""",
    "summary": """Your Point of Sale in the Mobile Version""",
    "category": "Point of Sale",
    "images": ["images/pos_mobile.png"],
    "version": "12.0.1.2.2",
    "application": False,
    "author": "Ganar Ganar",
    "support": "soporte@ganargan.ar",
    "license": "Other OSI approved licence",  # MIT
    "depends": ["point_of_sale", "pos_debranding"],
    "external_dependencies": {"python": [], "bin": []},
    "data": ["views/pos_mobile_template.xml", "views/pos_mobile_view.xml"],
    "qweb": ["static/src/xml/pos.xml"],
    "installable": True,
}
