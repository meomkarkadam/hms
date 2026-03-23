from odoo import models, fields, api



class AdminMaster(models.Model):
    _name = 'admin.master'
    _description = 'Admin Master'

    partner_id = fields.Many2one('res.partner', "Name")


