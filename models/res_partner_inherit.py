from odoo import models, fields, api



class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner'

    partner_id = fields.Many2one('res.partner', "Name")
    # erp_id = fields.Many2one('student.enrollment', string="Student ID")



