from odoo import api, fields, models


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
    damage_cost = fields.Monetary(
        currency_field='currency_id',
        help="Cost of damages to deduct from the deposit before refunding.",
    )
    refundable_amount = fields.Monetary(
        currency_field='currency_id',
        compute='_compute_refundable_amount',
        store=True,
    )
    state = fields.Selection(
        selection=[
            ('draft', "Draft"),
            ('held', "Held"),
            ('refunded', "Refunded"),
        ],
        default='draft',
        required=True,
    )

    @api.depends('amount', 'damage_cost')
    def _compute_refundable_amount(self):
        for deposit in self:
            deposit.refundable_amount = deposit.amount - deposit.damage_cost
