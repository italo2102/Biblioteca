from odoo import fields, models


class CheckoutStage(models.Model):
    _name = "library.checkout.stage"
    _description = "Checkout Stage"
    _order = "sequence"

    name = fields.Char()
    sequence = fields.Integer(default=10)
    fold = fields.Boolean()
    active = fields.Boolean(default=True)
    state = fields.Selection(
        [
            ("new", "Solicitado"),
            ("open", "Prestado"),
            ("done", "Retornado"),
            ("cancel", "Cancelado"),
        ],
        default="new",
    )
