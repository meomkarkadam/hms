from odoo import models, fields

class MedicalStore(models.Model):
    _name = 'medical.store'
    _description = 'Medical Store'

    name = fields.Char(string='Store Name', required=True)
    location = fields.Char(string='Location')
    contact_no = fields.Char(string='Contact Number')
    email = fields.Char(string='Email')
    manager = fields.Char(string='Store Manager')
    product_id = fields.Many2one('product.product', string='Medicine Name')
    medicine_ids = fields.One2many(
        comodel_name="medical.medicine",
        inverse_name="store_id",
        string="Medicines"
    )


class Medicine(models.Model):
    _name = 'medical.medicine'
    _description = 'Medicine'

    store_id = fields.Many2one(
        comodel_name="medical.store",
        string="Store"
    )

    name = fields.Char(string="Medicine Name")
    product_id = fields.Many2one('product.product', string='MC')


    # Add any other relevant fields for medicine below

    # @api.model
    # def check_expiry(self):
    #     today = fields.Date.today()
    #     expired_medicines = self.search([('expiry_date', '<', today)])
    #     return expired_medicines
