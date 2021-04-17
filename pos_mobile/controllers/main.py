import json

from odoo import http
from odoo.http import request
from odoo.osv.expression import AND
from odoo.addons.point_of_sale.controllers.main import PosController


class ControllerPos(PosController):
    @http.route()
    def pos_web(self, config_id=False, **k):
        response = super(ControllerPos, self).pos_web(config_id, **k)
        domain = [
                ("state", "=", "opened"),
                ("user_id", "=", request.session.uid),
                ("rescue", "=", False)
            ]
        
        if config_id:
            domain = AND([domain,[("config_id", "=", int(config_id))]])
    
        pos_session = request.env["pos.session"].sudo().search(domain, limit=1)

        if pos_session and pos_session.config_id.auto_mobile:
            session_info = request.env["ir.http"].session_info()
            session_info["user_context"]["pos_session_company_ids"] = pos_session.company_id.ids
            session_info["auto_mobile"] = True
            response.qcontext.update({
                "session_info": session_info,
                "login_number": pos_session.login(),
        })
        return response
