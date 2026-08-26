from odoo import models, fields, api
from datetime import datetime



class AcademicsMaster(models.Model):
    _name = 'academics.master'
    _description = 'Academics Master'

    course = fields.Selection([
        ('mbbs cbme', 'MBBS-CBME'),

        ('mbbs old', 'MBBS-OLD'),
    ],
        string="Course",
        default='mbbs cbme', )

    academic_year = fields.Selection(
        [
            ('2024-25', '2024-25'),
            ('2025-26', '2025-26'),
            ('2026-27', '2026-27'),
            ('2027-28', '2027-28'),
        ],
        string='Academic Year'
    )

    subject = fields.Selection([
        ('anatomy', 'Anatomy'),
        ('biochemistry', 'Biochemistry'),
        ('physiology', 'Physiology'),
        ('psm', 'PSM'),
        ('pathology', 'Pathology'),
        ('microbiology', 'Microbiology'),
        ('pharmacology', 'Pharmacology'),
        ('fmt', 'FMT'),
        ('surgery', 'Surgery'),
        ('medicine', 'Medicine'),
        ('obgy', 'OBGY'),
        ('orthopedics', 'Orthopedics'),
        ('ent', 'ENT'),
        ('ophthalmology', 'Ophthalmology'),
    ], string='Subject', required=True)

    def action_open_wizard(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Academics Wizard',
            'res_model': 'timetable.import.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_academic_id': self.id,
            }
        }



    # academic_year_id = fields.Many2one(
    #     'academic.year',
    #     string='Academic Year'
    # )

    line_ids = fields.One2many(
        'academics.line',
        'timetable_id',
        string='Timetable Lines'
    )

class AcademicsLine(models.Model):
    _name = 'academics.line'
    _description = 'Weekly Timetable Line'

    timetable_id = fields.Many2one(
        'academics.master',
        string='Timetable'
    )


    

    subject_id = fields.Many2one(
        'subject.master',
        string='Subject'
    )

    faculty_id = fields.Many2one(
        'res.partner',
        string='Faculty'
    )

    start_time = fields.Char(string='Start Time')
    end_time = fields.Char(string='End Time')

    subject = fields.Selection([
        ('anatomy', 'Anatomy'),
        ('biochemistry', 'Biochemistry'),
        ('physiology', 'Physiology'),
        ('psm', 'PSM'),
        ('pathology', 'Pathology'),
        ('microbiology', 'Microbiology'),
        ('pharmacology', 'Pharmacology'),
        ('fmt', 'FMT'),
        ('surgery', 'Surgery'),
        ('medicine', 'Medicine'),
        ('obgy', 'OBGY'),
        ('orthopedics', 'Orthopedics'),
        ('ent', 'ENT'),
        ('ophthalmology', 'Ophthalmology'),
    ], string='Subject', required=True)

    day = fields.Selection([
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
    ], string='Day')
