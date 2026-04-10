from odoo import models, fields, api



class AdmissionMaster(models.Model):
    _name = 'admission.master'
    _description = 'Admission Master'

    partner_id = fields.Many2one('res.partner', "Name")
    academic_year = fields.Selection(
        [
            ('2024-25', '2024-25'),
            ('2025-26', '2025-26'),
            ('2026-27', '2026-27'),
            ('2027-28', '2027-28'),
        ],
        string='Academic Year'
    )


