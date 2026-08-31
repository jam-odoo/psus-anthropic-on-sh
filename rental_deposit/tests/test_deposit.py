from odoo.tests.common import TransactionCase


class TestDeposit(TransactionCase):

    def test_manager_can_read(self):
        manager = self.env['res.users'].create({
            'name': "Deposit Manager",
            'login': 'deposit_manager',
            'group_ids': [(4, self.env.ref('rental_deposit.group_deposit_manager').id)],
        })

        deposit = self.env['rental.deposit'].create({
            'name': "Deposit A",
            'amount': 150.0,
        })

        self.env.invalidate_all()
        deposit_as_manager = deposit.with_user(manager)
        self.assertEqual(deposit_as_manager.read(['amount'])[0]['amount'], 150.0)
