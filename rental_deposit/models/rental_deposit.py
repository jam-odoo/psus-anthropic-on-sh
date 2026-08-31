from odoo import fields, models


class RentalDeposit(models.Model):
    _name = 'rental.deposit'
    _description = "Rental Deposit"

    name = fields.Char(required=True)
    rental_order_id = fields.Many2one('sale.order', string="Rental Order")
    currency_id = fields.Many2one(
        'res.currency',
        default=lambda self: self.env.company.currency_id,
    )
    amount = fields.Monetary(currency_field='currency_id')
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('held', "Held"),
            ('refunded', "Refunded"),
        ],
        default='draft',
        required=True,
    )
