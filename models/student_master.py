from odoo import models, fields, api



class StudentMaster(models.Model):
    _name = 'student.master'
    _description = 'Student Master'

    partner_id = fields.Many2one('res.partner', "Name")


