from odoo import http
from odoo.addons.library_app.controllers.main import Books


class Members(http.Controller):

    @http.route("/biblioteca/usuarios")
    def list(self, **kwargs):
        Member = http.request.env["library.member"]
        members = Member.search([])
        return http.request.render(
            "library_member.member_list_template",
            {"members": members}
        )
