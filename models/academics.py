from odoo import models, fields, api



class StudentMaster(models.Model):
    _name = 'academics.master'
    _description = 'Academics Master'

    partner_id = fields.Many2one('res.partner', "Name")


